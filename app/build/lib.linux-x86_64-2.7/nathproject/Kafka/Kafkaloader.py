import socket

from confluent_kafka.cimpl import Producer


class Kafkaloader:

    def createProducer(self):
        conf = {'bootstrap.servers': "host1:9092,host2:9092",
                'client.id': socket.gethostname()}
        producer = Producer(conf)
        return producer
