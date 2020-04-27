"""Console script for nathproject."""
import sys
import click

from nathproject.Kafka.Kafkaloader import Kafkaloader
from nathproject.Util import Util


@click.command()
def main(args=None):
    """Console script for nathproject."""
    click.echo("Replace this message by putting your code into "
               "nathproject.cli.main")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    util = Util();
    test = util.createJSON();
    click.echo("JSON: " + test);
    xml = util.readXMLFile();
    for element in xml:
        print(element.tag, element.attrib)
    return 0


@click.command()
@click.option('--topic', nargs=1, type=str)
@click.option('--message', nargs=1, type=str)
def produce(topic, message):
    kafka = Kafkaloader();
    producer = kafka.createProducer();
    producer.produce(topic, key="1", value=message)

@click.command()
def test(self):
    print("test")


if __name__ == "__main__":
    sys.exit(produce())  # pragma: no cover
