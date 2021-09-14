FROM python:3.9-alpine
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements /requirements
RUN pip install -r /requirements/local.txt
