FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./apps/api apps/api
COPY ./configs/api/requirements.txt configs/api/requirements.txt
WORKDIR apps/api

RUN pip install --upgrade -r /configs/api/requirements.txt
