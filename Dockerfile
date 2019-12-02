FROM python:3.7.5-slim-buster

COPY . /opt/tests/
WORKDIR /opt/tests

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN pip install --upgrade pip
RUN pip install pipenv
RUN pipenv install --dev
RUN chmod 644 car_service.py
