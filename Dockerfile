FROM python:3.9-alpine as builder
WORKDIR /src
COPY ./src .
ENTRYPOINT ["python", "main.py"]


FROM python:3.9-alpine as tester
WORKDIR /src
COPY test-requirements.txt .
RUN pip install -r test-requirements.txt
COPY ./src .
COPY ./tests .
ENTRYPOINT ["./run_tests.sh"]