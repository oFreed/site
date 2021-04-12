FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /shop/

COPY . /shop/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

