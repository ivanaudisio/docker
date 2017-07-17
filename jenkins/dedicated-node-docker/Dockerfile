############################################################
# Dockerfile
# Jenkins Node with Docker installed inside
#
# Update the index of available packages
# Install JDK to connect node to Jenkins through JNLP
# Install Supervisord to run multiple services:
#   - Docker
#   - Python script to create node and attach it
# Install pip that is needed to install mechanize
# Install curl to execute REST API on master
# Install wget needed to get slave.jar file
# Install git to be able to retrieve repositories
# Install mechanize to validate that Jenkins is running
# Install docker compose
############################################################

FROM docker:dind

RUN apk add --update \
    openjdk7-jre \
    supervisor \
    py-pip \
    curl \
    wget \
    git \
    && pip install mechanize \
    && pip install docker-compose

COPY supervisord.conf /etc/
COPY node-create.groovy /home/
COPY node-attach.py /home/

ENTRYPOINT ["/usr/bin/supervisord", "--nodaemon", "--configuration", "/etc/supervisord.conf"]
