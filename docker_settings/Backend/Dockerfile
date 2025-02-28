FROM python:3.12-slim

WORKDIR /app

ENV PYTHONUNBUFFERED 1

COPY requirements.txt .

COPY ../docker_settings/Backend/app.sh /app/config/app.sh

RUN chmod +x ./config/app.sh

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .
