"""Console script for nathproject."""
import socket
import sys
import click
from confluent_kafka.cimpl import Producer

from nathproject.Kafka.Kafkaloader import Kafkaloader
from nathproject.Util import Util
def acked(err, msg):
    if err is not None:
        print("Failed to deliver message: %s: %s" % (str(msg), str(err)))
    else:
        print("Message produced: %s" % (str(msg)))

@click.group(chain=True)
def main():
    pass

@main.command(help='create producer')
@click.option('--topic', nargs=1,required=True, type=str, help='topic where you want to write')
@click.option('--message', nargs=1,required=True, type=str, help='message to send')
def produce(topic, message):
    kafka = Kafkaloader();
    producer = kafka.createProducer();
    producer.produce(topic, key="key", value=message, callback=acked)
    producer.poll(1)

@main.command(help='create consumer')
@click.option('--group', nargs=1,required=True, type=str, help='group of the consumer')
@click.option('--topic', nargs=1,required=True, type=str, help='topic to listen')
def consume(group, topic):
    kafka = Kafkaloader();
    consumer = kafka.createConsumer(group, topic);
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            print("Consumer error: {}".format(msg.error()))
            continue
        print('Received message: {}'.format(msg.value().decode('utf-8')))
    consumer.close()


# @main.command()
# def createjson():
#     util = Util();
#     test = util.createJSON();
#     click.echo("JSON: " + test);
#     xml = util.readXMLFile();
#     for element in xml:
#         print(element.tag, element.attrib)
#     return 0

if __name__ == '__main__':
    main()
