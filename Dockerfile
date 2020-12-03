FROM python:3.9-alpine as builder
WORKDIR /src
COPY ./src .
ENTRYPOINT ["python", "main.py"]


FROM python:3.9-alpine as tester
WORKDIR /src
RUN pip install pytest
COPY ./src .
COPY ./tests .
ENTRYPOINT ["pytest"]