FROM ubuntu:16.04

# Installing openssh-server into our container to be able to ssh to other servers
RUN apt-get update && apt-get install -y openssh-server vim && \
    mkdir /var/run/sshd # creating privilege separation directory missing

COPY id_rsa.pub /tmp

# modify password for root user & create .ssh folder
RUN echo 'root:password' | chpasswd && \
    mkdir /root/.ssh && \
    chmod 755 /root/.ssh/ && \
    cat /tmp/id_rsa.pub >> /root/.ssh/authorized_keys && \
    chmod 400 /root/.ssh/authorized_keys

# Create new user & create .ssh folder
RUN export NEW_USER=demo1 && \
    adduser --disabled-password --gecos "" $NEW_USER && \
    echo "$NEW_USER:password" | chpasswd && \
    mkdir /home/$NEW_USER/.ssh && \
    chmod 755 /home/$NEW_USER/.ssh/ && \
    chown $NEW_USER:$NEW_USER /home/$NEW_USER/.ssh && \
    cat /tmp/id_rsa.pub >> /home/$NEW_USER/.ssh/authorized_keys && \
    chown $NEW_USER:$NEW_USER /home/$NEW_USER/.ssh/authorized_keys && \
    chmod 400 /home/$NEW_USER/.ssh/authorized_keys

# Create new user
RUN export NEW_USER=demo2 && \
    adduser --disabled-password --gecos "" $NEW_USER && \
    echo "$NEW_USER:password" | chpasswd

RUN rm -f /tmp/id_rsa.pub   # Remove uploaded public key from /tmp

# Configure openssh-server
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config  # Permit root user to login remotely
RUN sed -i 's/#PasswordAuthentication yes/PasswordAuthentication no/' /etc/ssh/sshd_config
RUN sed -i 's/#UsePAM yes/UsePAM no/' /etc/ssh/sshd_config

# Set the users that can SSH into this machine
# RUN echo 'AllowUsers root demo1' >> /etc/ssh/sshd_config

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]