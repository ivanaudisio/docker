############################################################
# Dockerfile
# Nexus Repository
############################################################

FROM sonatype/nexus3:3.5.1

USER root

RUN yum update -y
RUN yum install python-setuptools -y
RUN easy_install pip
Run pip install supervisor

COPY supervisord.conf /etc/
COPY create.sh /home/create.sh
COPY repositories.json /home/repositories.json

RUN touch /tmp/nexuslogs

CMD ["/usr/bin/supervisord"]
