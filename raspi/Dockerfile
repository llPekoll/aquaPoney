FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN apt-get update
RUN apt-get upgrade
RUN apt-get install -y gcc
COPY ./requirements.txt /back/requirements.txt
RUN pip install adafruit_bme280 requests board
WORKDIR /raspi

