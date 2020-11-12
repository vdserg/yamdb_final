FROM python:3.8.6-slim-buster

WORKDIR /code
COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY . .

CMD python manage.py migrate --noinput && \
    gunicorn api_yamdb.wsgi:application --bind 0.0.0.0:8000