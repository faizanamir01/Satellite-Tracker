# FROM python:3.8-slim-buster
FROM python:3.12-alpine3.18

ENV PYTHONUNBUFFERED = 1
WORKDIR /satellite

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt


