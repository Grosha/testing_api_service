FROM python:3.8.6-slim-buster

COPY . /opt/car_service/
WORKDIR /opt/car_service

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN apt-get update && apt-get install -y build-essential
RUN apt-get update && apt-get install -y manpages-dev
RUN pip install --upgrade pip
RUN pip install psutil
RUN pip install pipenv
RUN pipenv install --dev
RUN echo $(ls)
RUN chmod 644 car_service.py

#CMD ["bash", "runner.sh"]