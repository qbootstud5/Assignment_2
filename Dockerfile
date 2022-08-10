FROM python:3.10.5-slim-buster

RUN mkdir /opt/project
WORKDIR /opt/project

COPY requirements.txt ./

# set PYTHONPATH so that it is possible to run in a container
ENV PYTHONPATH=.:..

RUN python3 -m pip install -r requirements.txt