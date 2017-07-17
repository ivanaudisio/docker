############################################################
# Dockerfile
# Jenkins Master
############################################################

FROM jenkins:latest

COPY plugins.txt /usr/share/jenkins/ref/
RUN /usr/local/bin/plugins.sh /usr/share/jenkins/ref/plugins.txt

USER root

RUN apt-get -q update &&\
    apt-get install -y supervisor && \
    mkdir -p /var/log/supervisor && \
    apt-get -q clean -y && rm -rf /var/lib/apt/lists/* && rm -f /var/cache/apt/*.bin

COPY custom.groovy /usr/share/jenkins/ref/init.groovy.d/custom.groovy
COPY supervisord.conf /etc/

CMD ["/usr/bin/supervisord"]
