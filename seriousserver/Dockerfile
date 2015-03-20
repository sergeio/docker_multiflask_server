FROM ubuntu:14.04
MAINTAINER Sergei Orlov
RUN apt-get update && apt-get install -y python2.7 python-pip python-virtualenv
ADD ./seriousserver /opt/seriousserver/
WORKDIR /opt/seriousserver
RUN virtualenv venv
RUN venv/bin/pip install -r requirements.pip
EXPOSE 8001
CMD ./server start_foreground
