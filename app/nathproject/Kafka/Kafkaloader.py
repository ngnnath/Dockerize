import socket

from confluent_kafka import Producer, Consumer


class Kafkaloader:

    def createProducer(self):
        conf = {'bootstrap.servers': "localhost:9092",
                            'client.id': socket.gethostname()}
        producer = Producer(conf)
        return producer

    def createConsumer(self, group, topic):
        conf ={'bootstrap.servers': "localhost:9092", 'group.id': group, 'auto.offset.reset': 'earliest'}
        consumer = Consumer(conf);
        consumer.subscribe([topic])
        return consumer
