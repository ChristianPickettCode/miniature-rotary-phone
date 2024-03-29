# Dockerfile

# pull the official docker image
FROM python:3.11.1-slim

# set work directory
WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .
