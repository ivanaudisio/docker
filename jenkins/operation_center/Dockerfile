############################################################
# Dockerfile
# Install latest Jenkins
############################################################
FROM cloudbees/jenkins-operations-center:1.625.24.1
MAINTAINER ivan.audisio

USER root

RUN apt-get -q update &&\
    apt-get install python-mechanize -y &&\
    apt-get install -y supervisor && \
    mkdir -p /var/log/supervisor && \
    apt-get -q clean -y && rm -rf /var/lib/apt/lists/* && rm -f /var/cache/apt/*.bin

COPY configure_cjoc.groovy /usr/share/jenkins/ref/init.groovy.d/configure_cjoc.groovy
COPY configure_trial_license.py /home/
COPY supervisord.conf /etc/

EXPOSE 8080

ENTRYPOINT ["/usr/bin/supervisord"]
