FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN rm -rf front/node_modules 
RUN rm -rf front/public/build 
RUN rm -rf front/package-lock.json 
RUN rm -rf front/yarn.lock 

RUN apt-get update
RUN apt-get install -y curl
RUN curl -sL https://deb.nodesource.com/setup_14.x | bash -
RUN apt-get install -y nodejs

RUN apt remove cmdtest
RUN apt remove yarn
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg |  apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" |  tee /etc/apt/sources.list.d/yarn.list
RUN apt-get update
RUN apt-get install yarn -y

RUN yarn --cwd /front/ install --frozen-lockfile
RUN yarn yarn --cwd /front/ run build

RUN rm public/build/bundle.css.map
RUN rm public/build/bundle.js.map

COPY ./requirements.txt /back/requirements.txt
RUN pip install fastapi uvicorn tortoise-orm[asyncpg] jinja2 aiofiles

EXPOSE 8000