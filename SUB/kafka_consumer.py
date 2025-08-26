from kafka import KafkaConsumer
import json
import datetime
from DAL.dal_mongo import DAL_mongo


class Kafka_consumer:

    def __init__(self, server, topic, DAL_mongo: DAL_mongo):
        self.server = server
        self.consumer_events = None
        self.topic = topic
        self.DAL_mongo = DAL_mongo


    def run_consumer_events(self):
        self.consumer_events = KafkaConsumer(self.topic,
                                 value_deserializer=lambda m: json.loads(m.decode('ascii')),
                                 bootstrap_servers=[self.server],
                                 consumer_timeout_ms= 20000)


    def save_events(self):
        if self.consumer_events is not None:
            for message in self.consumer_events:
                print(message.offset)
                data = {}
                timestamp = datetime.datetime.now()
                data = message.value
                data['timestamp'] = timestamp

                self.DAL_mongo.insert_one(data)









