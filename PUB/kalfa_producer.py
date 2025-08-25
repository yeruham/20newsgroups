from kafka import KafkaProducer
import json
from newsgroups import newsgroups_interesting
from newsgroups import newsgroups_not_interesting


class Kalfa_producer:

    def __init__(self, server):
        self.server = server
        self.producer = self.get_producer()


    def get_producer(self):
        producer = KafkaProducer(bootstrap_servers=[self.server],
                                 value_serializer=lambda x:
                                 json.dumps(x).encode('utf-8'))
        return producer


    def close_producer(self):
        if self.producer is not None:
            self.producer.flush()
        self.producer = None


    def publish_message(self, topic, message):
        if self.producer is not None:
            self.producer.send(topic, message)

