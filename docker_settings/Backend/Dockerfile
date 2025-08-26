FROM python:3.12-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt .

RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY ./anifigure /app/anifigure

COPY ./docker_settings/Backend/app.sh /app/app.sh

RUN chmod +x /app/app.sh

EXPOSE 8000

ENTRYPOINT ["sh", "./app.sh"]
