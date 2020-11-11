FROM python:3.8.5

RUN pip install --upgrade pip
WORKDIR /code
COPY . .
RUN pip install -r requirements.txt
