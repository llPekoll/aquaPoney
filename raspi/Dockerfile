FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN apt-get update
RUN apt-get upgrade
RUN apt-get install --no-cache bash\
                       python \
                       pkgconfig \
                       git \
                       gcc \
                       openldap \
                       libcurl \
                       python2-dev \
                       gpgme-dev \
                       libc-dev \

COPY ./requirements.txt /back/requirements.txt
RUN pip install adafruit_bme280 requests
WORKDIR /raspi

