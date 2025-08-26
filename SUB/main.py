from fastapi import FastAPI
from contextlib import asynccontextmanager
import uvicorn
import os
from kafka_consumer import Kafka_consumer


KAFKA_SERVER = os.getenv("KAFKA_SERVER", "localhost:9092")
HOST = os.getenv("HOST", "localhost")
USER = os.getenv("USER", None)
PASSWORD = os.getenv("PASSWORD", None)
DB = os.getenv("DATABASE", "newsgroups")
COLLECTION = os.getenv("COLLECTION", "interesting")
EXPOSE_PORT = int(os.getenv("EXPOSE_PORT", "8082"))


app = FastAPI()









if __name__ == "__main__":
    CONSUMER = Kafka_consumer(KAFKA_SERVER)
    uvicorn.run(app, host="0.0.0.0", port=EXPOSE_PORT)