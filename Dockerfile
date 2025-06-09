FROM python:3.11-slim-bookworm

RUN apt-get update && \
    apt-get install -y --no-install-recommends cron && \
    apt-get upgrade -y && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . .

RUN pip install --upgrade pip && pip install -r requirements.txt
RUN chmod +x manage.py

CMD ["sh", "-c", "python manage.py migrate && python manage.py crontab add && python manage.py runserver 0.0.0.0:8000"]
