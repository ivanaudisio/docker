# ANSIBLE

## Running the playbook

`cd /home/ansible`

`ansible-playbook helloworld.yml`

```
PLAY [all] *********

GATHERING FACTS *********
ok: [localhost]

TASK: [shell echo "hello world"] *********
changed: [localhost]

PLAY RECAP *********
localhost                  : ok=2    changed=1    unreachable=0    failed=0   
```

## Runnig on localhost

*Note:* This is already done inside the container

We do this by using the default inventory file /etc/ansible/hosts. 

Just add an entry for localhost as given below:

`localhost ansible_connection=local`

