FROM python:3.10.0-alpine3.14

RUN pip install --upgrade pip
RUN pip install pipenv

WORKDIR /usr/src/app

COPY Pipfile .
COPY Pipfile.lock .

RUN apk add build-base
RUN apk add postgresql-dev
RUN pipenv install --system


COPY . .

RUN pip install -e .

CMD uvicorn main:app --host=0.0.0.0 --port=$PORT