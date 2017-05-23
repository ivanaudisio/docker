## set up SSH public-key authentication to connect to a remote system

Using SSH public-key authentication to connect to a remote system is a robust, more secure alternative to logging in with an account password or passphrase. SSH public-key authentication relies on asymmetric cryptographic algorithms that generate a pair of separate keys (i.e., a key pair), one "private" and the other "public". You keep the private key a secret and store it on the computer you use to connect to the remote system. Conceivably, you can share the public key with anyone without compromising the private key; you store it on the remote system in a .ssh/authorized_keys directory.

### Set up SSH server on Ubuntu 16.04

**Step 1** – Update repositories.

`apt-get update`

**Step 2** – Install SSH Server

`apt-get install openssh-server`

### Basic Configuration

**Step 3** – After installation I will show how to configure ssh server. Open ssh config file with the following command:

`vim /etc/ssh/sshd_config`

**Step 4** – If you want to change ssh port you have to find ‘Port’ line and change the number of the port. For example I will change to 22222.

`Port 22222`

**Step 5** – We can set max login attempts to be 3. After 3 wrong login attempts you will disconect. This is very important for security of your server and this can be used for prevention from brute force attack (see my Theme 4). Add this line bellow Port:

`MaxAuthTries 3`

**Step 6** – Allow certain users to login on your server and deny all other users. I will add ‘zimbra’ users because my Zimbra Mail Serve should have access. For more information about Zimbra Mail Server configuration read theme 12. Add the following line at the end of the file and after that save the file /etc/ssh/sshd_config.

`AllowUsers root user1 user2`

**Step 7** – Restart ssh service with the following command:

`systemctl restart ssh` or `service ssh restart`

> **Note:** For docker the container needs to be restarted

**Step 8** – Show ssh status

`service ssh status`

### Advanced Configuration

This is the best way to protect from unauthorised access to your server. Unfortunately this is not the most convenient one, because you have to bring the key with you as it will be shown below.

**Step 9** – Create folder, change permission and navigate to new folder with the following commands:

`root@server:/# mkdir .ssh/; chmod 700 .ssh/; cd .ssh/;`

**Step 10** – Create folder, change permission and navigate to new folder with the following commands:

`root@server:/.ssh# touch authorized_keys; chmod 600 authorized_keys`

**Step 11** – Generate Keys – If you ‘Enter passphrase’ you must remember it and use it in the following steps:

```
root@server_master:/# ssh-keygen -t rsa
Generating public/private rsa key pair.
Enter file in which to save the key (/root/.ssh/id_rsa): 
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /root/.ssh/id_rsa.
Your public key has been saved in /root/.ssh/id_rsa.pub.
The key fingerprint is:
SHA256:tN+OeF8tBU9KbRoKXr650iiMi4+rGI5zlrzeONmnE9E root@server_master
The key's randomart image is:
+---[RSA 2048]----+
|                 |
|               . |
|     .  . . . + +|
|    . E. o + o O |
|     .  S . o o o|
|    .    . . o o |
|.. + . o  .o+ o .|
|+oBoooo o.+o.o . |
|o*=+**o..o.o+    |
+----[SHA256]-----+
```

> **Note:** To do this in one line of code we use the following:

`ssh-keygen -b 2048 -t rsa -f /root/.ssh/id_rsa -q -N ""`

**Step 12** – Append the public key to authorized_keys and remove the uploaded copy.

`root@server:/.ssh# cat id_rsa.pub >> authorized_keys`

**Step 13** – Edit the ssh server config file with nano /etc/ssh/sshd_config to make sure that public key authentication is enabled (it should be enabled by default):

`root@server:/.ssh# vim /etc/ssh/sshd_config`

**Step 14** – These entries must be set to YES.

```
RSAAuthentication yes
PubkeyAuthentication yes
```

**Step 15** – The following settings should be set to NO:

```
ChallengeResponseAuthentication no
PasswordAuthentication no
UsePAM no
```

**Step 16** – Restart ssh service with the following command:

`root@server:/.ssh# service ssh restart`

> Repeat these steps on all servers where we are granting access

> We can also grant access to specific users withing a server by repeating the steps under /home/username/.ssh/authorized_keys

**Step 17** – Now in order to connect to any of these servers we need to use the private key generated

`root@server_master: ssh -i /root/.ssh/id_rsa root@server`