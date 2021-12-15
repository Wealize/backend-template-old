FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y --no-install-recommends \
    git gettext

RUN mkdir /code

WORKDIR /code

RUN pip install poetry
ADD pyproject.toml /code/
RUN poetry install
