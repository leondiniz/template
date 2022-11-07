FROM python:3.8-slim-buster


# set environment variables
ENV PYTHONWRITEBYTECODE 1
ENV PYTHONBUFFERED 1


# set working directory
WORKDIR /api
RUN mkdir app


# Install dependencies.
COPY requirements.txt app/
COPY requirements-test.txt app/


# install dependencies
RUN pip install --upgrade pip
RUN pip install -r app/requirements.txt
RUN pip install -r app/requirements-test.txt


# copy project
COPY app ./app
COPY tests ./tests
COPY scripts ./scripts
COPY .coveragerc .coveragerc
