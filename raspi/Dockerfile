FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /back/requirements.txt
RUN pip install adafruit_bme280 requests
WORKDIR /raspi

