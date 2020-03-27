FROM python:3.6-slim

EXPOSE 5000

WORKDIR /app

RUN mkdir -p /app/templates
RUN mkdir -p /app/static
COPY templates/* /app/templates
COPY static/* /app/static
COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY app.py /app
CMD python app.py
