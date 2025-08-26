from fastapi import FastAPI
from contextlib import asynccontextmanager
import uvicorn
import os


from DAL.dal_mongo import DAL_mongo
from kafka_consumer import Kafka_consumer


KAFKA_SERVER = os.getenv("KAFKA_SERVER", "localhost:9092")
TOPIC = os.getenv("TOPIC", 'interesting')
EXPOSE_PORT = int(os.getenv("EXPOSE_PORT", "8082"))

HOST = os.getenv("HOST", "localhost")
USER = os.getenv("USER", None)
PASSWORD = os.getenv("PASSWORD", None)
DB = os.getenv("DATABASE", "newsgroups")
COLLECTION = os.getenv("COLLECTION", "interesting")


@asynccontextmanager
async def lifespan(app: FastAPI):
    DAL_mongo.open_connection()
    # delete all documents in collection for testing
    # DAL_mongo.delete_all()
    CONSUMER.run_consumer_events()
    CONSUMER.save_events()
    yield
    DAL_mongo.close_connection()


app = FastAPI(lifespan= lifespan)


@app.get('/')
def root():
    return {"message": f"API of {COLLECTION} mongodb with messages,"
                       f"to run consumer events go to path /run_consumer"
                       f" to get data go to path /data"}


@app.get('/run_consumer')
async def run_consumer_events():
    CONSUMER.run_consumer_events()
    CONSUMER.save_events()
    return {"message": "consumer events run 20000 ms"}



@app.get('/data')
async def get_data():
    try:
        data= DAL_mongo.get_all()
        return {"result ": data}
    except Exception as e:
        print("error : ", e)




if __name__ == "__main__":
    DAL_mongo = DAL_mongo(HOST, DB, COLLECTION, USER, PASSWORD)
    CONSUMER = Kafka_consumer(KAFKA_SERVER, TOPIC, DAL_mongo)
    uvicorn.run(app, host="0.0.0.0", port=EXPOSE_PORT)