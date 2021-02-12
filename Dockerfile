FROM python:3.9-slim

COPY requirements.txt /

RUN pip install -r /requirements.txt

COPY data_app/ /app
WORKDIR /app

CMD ["python","./run.py"]