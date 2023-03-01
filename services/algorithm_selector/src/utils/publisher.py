import pika
from algorithm_selector.src.security.credentials import CredentialsProvider


class Publisher:
    @staticmethod
    def publish(topic, data):
        parameters = pika.ConnectionParameters(host='rabbitmq', credentials=CredentialsProvider.get())

        connection = pika.BlockingConnection(parameters)
        channel = connection.channel()
        channel.exchange_declare(exchange=topic, exchange_type='fanout')
        channel.basic_publish(
            exchange=topic,
            routing_key='',
            body=data)
        connection.close()
