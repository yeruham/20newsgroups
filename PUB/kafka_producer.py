from kafka import KafkaProducer
import json


class Kafka_producer:

    def __init__(self, server):
        self.server = server
        self.producer = None


    def create_producer(self):
        if self.producer is None:
            self.producer = KafkaProducer(bootstrap_servers=[self.server],
                                     value_serializer=lambda x: json.dumps(x).encode('utf-8'))



    def close_producer(self):
        if self.producer is not None:
            self.producer.flush()
        self.producer = None


    def publish_messages(self, topic: str,title:str, data: list):
        if self.producer is not None:
            for d in data:
                message = {title: d}
                self.producer.send(topic, message)

