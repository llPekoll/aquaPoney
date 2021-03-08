FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /back/requirements.txt
RUN pip install fastapi uvicorn

EXPOSE 8000