from fastapi import FastAPI
from contextlib import asynccontextmanager
import uvicorn
import os
import newsgroups as news
from kalfa_producer import Kalfa_producer


SERVER = os.getenv("SERVER", "localhost:9092")


@asynccontextmanager
async def lifespan(app: FastAPI):
    PRODUCER.create_producer()
    yield
    PRODUCER.close_producer()



app = FastAPI(lifespan=lifespan)


@app.get('/')
def root():
    return {"massage:": "api of producer news, by path /news it producer 20 news to two topics"}


@app.get('/news')
async def produces_news():

    tan_interesting = next(newsgroups_interesting)
    tan_not_interesting = next(newsgroups_not_interesting)

    PRODUCER.publish_messages('interesting' ,'massage' , tan_interesting)
    PRODUCER.publish_messages('not_interesting', 'massage', tan_not_interesting)




if __name__ == "__main__":

    PRODUCER = Kalfa_producer(SERVER)
    newsgroups_interesting = news.iter_data(news.get_newsgroups_interesting(), 10)
    newsgroups_not_interesting = news.iter_data(news.get_newsgroups_not_interesting(), 10)

    uvicorn.run(app, host="0.0.0.0", port=8081)

