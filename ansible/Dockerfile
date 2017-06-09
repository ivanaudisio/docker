FROM ubuntu:16.04

RUN apt-get update && \
    yes | apt-get install software-properties-common && \
    apt-get install ansible -y && \
    mkdir /home/ansible && \
    apt-get install vim -y && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# http://ansible.pickle.io/post/86598332429/running-ansible-playbook-in-localhost
COPY hosts /etc/ansible/hosts
COPY helloworld.yml /home/ansible

CMD ["tail","-f","/dev/null"]
