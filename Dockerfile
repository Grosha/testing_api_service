FROM python:3.7.5-slim-buster
RUN apt-get upgrade && apt-get update && apt-get install git --yes

COPY . /opt/service/
WORKDIR /opt/service

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN pip install --upgrade pip
RUN pip install pipenv
RUN pipenv install --dev
