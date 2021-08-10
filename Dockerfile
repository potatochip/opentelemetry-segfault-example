FROM python:3.8-slim-buster as base
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000

