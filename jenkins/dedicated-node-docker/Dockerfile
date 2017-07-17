############################################################
# Dockerfile
# Jenkins Node with Docker installed inside
############################################################

FROM docker:dind

RUN apk add --update \            # Update the index of available packages
    openjdk7-jre \                # Install JDK to connect node to Jenkins through JNLP
    supervisor \                  # Install Supervisord to run multiple services (docker and script to create/attach node)
    py-pip \                      # Install pip that is needed to install mechanize
    curl \                        # Install curl to execute REST API on master
    wget \                        # Install wget needed to get slave.jar file
    git \                         # Install git to be able to retrieve repositories upon testing
    && pip install mechanize      # Install mechanize to automate and validate that Jenkins is running

COPY supervisord.conf /etc/
COPY node-create.groovy /home/
COPY node-attach.py /home/

ENTRYPOINT ["/usr/bin/supervisord", "--nodaemon", "--configuration", "/etc/supervisord.conf"]
