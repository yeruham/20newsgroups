FROM python:3.11-slim

WORKDIR /app

ENV SERVER=broker

COPY requirements.txt .
RUN pip install -r requirements.txt

copy . .

EXPOSE 8081

CMD ["python","main.py"]