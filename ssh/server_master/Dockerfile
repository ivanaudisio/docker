FROM ubuntu:16.04

# Installing openssh-server into our container to be able to ssh to other servers
RUN apt-get update && apt-get install -y openssh-server vim

# The command below creates a private and plublic key
# RUN ssh-keygen -b 2048 -t rsa -f /root/.ssh/id_rsa -q -N ""

RUN mkdir /var/run/sshd         # Creating privilege separation directory missing after installation.
COPY id_rsa /root
RUN chmod 400 /root/id_rsa      # Protecting private key by not making it accessible to others.

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]