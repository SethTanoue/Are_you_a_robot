FROM python:3.11.0b3-bullseye

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN set -ex \
    && pip install --upgrade pip \
    && pip install -r /app/requirements.txt

ADD . .

CMD gunicorn myapp.wsgi:application --bind 0.0.0.0:$PORT