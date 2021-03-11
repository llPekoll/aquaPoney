FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /back/requirements.txt
RUN pip install fastapi uvicorn tortoise-orm[asyncpg] jinja2 aiofiles

EXPOSE 8000