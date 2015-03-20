FROM ubuntu:14.04
MAINTAINER Sergei Orlov
RUN apt-get update && apt-get install -y python2.7 python-pip python-virtualenv
ADD ./funserver /opt/funserver/
WORKDIR /opt/funserver
RUN virtualenv venv
RUN venv/bin/pip install -r requirements.pip
EXPOSE 8002
CMD ./server start_foreground
