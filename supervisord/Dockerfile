FROM ubuntu:latest
RUN apt-get update && \
    apt-get install -y supervisor && \
    apt-get install -y openssh-server && \
    mkdir -p /var/log/supervisor && \
    mkdir /var/run/sshd

COPY python_script.py /home
COPY supervisord.conf /etc

#RUN echo "[supervisord]" > /etc/supervisord.conf && \
#nodaemon=true
#
#[program:exim]
#command=/usr/sbin/exim -bd -q1h
#
#[program:mysqld]
#command=/usr/bin/mysqld_safe
#
#[program:httpd]
#command=/usr/sbin/apachectl -D FOREGROUND
#
#[program:pythonscript]
#command=python /home/python_script.py" >> /etc/supervisord.conf

CMD ["/usr/bin/supervisord"]