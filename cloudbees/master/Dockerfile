############################################################
# Dockerfile
# Install latest Jenkins
############################################################
FROM cloudbees/jenkins-enterprise:1.651.21.1
MAINTAINER ivan.audisio

USER root

RUN apt-get -q update &&\
    apt-get install python-mechanize -y &&\
    apt-get install -y supervisor && \
    mkdir -p /var/log/supervisor && \
    apt-get -q clean -y && rm -rf /var/lib/apt/lists/* && rm -f /var/cache/apt/*.bin

COPY configure_master.groovy /usr/share/jenkins/ref/init.groovy.d/
COPY configure_attach_cjoc.py /home/
COPY configure_attach_cjoc.groovy /home/
COPY supervisord.conf /etc/

EXPOSE 8080

CMD ["/usr/bin/supervisord"]
