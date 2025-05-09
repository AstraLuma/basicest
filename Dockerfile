FROM docker.io/library/python:3
COPY . /opt/basicest
RUN pip install -e /opt/basicest