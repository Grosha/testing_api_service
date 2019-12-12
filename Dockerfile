FROM python:3.7.5-slim-buster

COPY . /opt/car_service/
WORKDIR /opt/car_service

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN pip install --upgrade pip
RUN pip install pipenv
RUN pipenv install --dev
RUN echo $(ls)
RUN chmod 644 car_service.py
