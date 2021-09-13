FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY ./requirements /requirements
RUN pip install -r /requirements/local.txt
COPY . /app/
WORKDIR /app
