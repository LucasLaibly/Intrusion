FROM python:3.9-slim

WORKDIR /app

COPY app/requirements.txt .

RUN pip install -r requirements.txt

COPY app/src/ .

CMD ["python", "./server.py"]