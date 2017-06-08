FROM ubuntu:latest
RUN apt-get update && \
    apt-get install -y supervisor && \
    apt-get install -y openssh-server && \
    mkdir -p /var/log/supervisor && \
    mkdir /var/run/sshd

COPY python_script.py /home
COPY supervisord.conf /etc

#RUN echo "[supervisord]" > /etc/supervisord.conf && \
#    echo "nodaemon=true" >> /etc/supervisord.conf && \
#    echo "" >> /etc/supervisord.conf && \
#    echo "[program:exim]" >> /etc/supervisord.conf && \
#    echo "command=/usr/sbin/exim -bd -q1h" >> /etc/supervisord.conf && \
#    echo "" >> /etc/supervisord.conf && \
#    echo "[program:mysqld]" >> /etc/supervisord.conf && \
#    echo "command=/usr/bin/mysqld_safe" >> /etc/supervisord.conf && \
#    echo "" >> /etc/supervisord.conf && \
#    echo "[program:httpd]" >> /etc/supervisord.conf && \
#    echo "command=/usr/sbin/apachectl -D FOREGROUND" >> /etc/supervisord.conf && \
#    echo "" >> /etc/supervisord.conf && \
#    echo "[program:pythonscript]" >> /etc/supervisord.conf && \
#    echo "command=python /home/python_script.py" >> /etc/supervisord.conf

CMD ["/usr/bin/supervisord"]