import pika
from threading import Thread
from security.credentials import CredentialsProvider


class Publisher:
    def __init__(self, topic, routing_key, exchange_type):
        self.topic = topic
        self.routing_key = routing_key
        self.exchange_type = exchange_type

    def __callback(self, data):
        parameters = pika.ConnectionParameters(host='rabbitmq', credentials=CredentialsProvider.get_credentials())

        connection = pika.BlockingConnection(parameters)
        channel = connection.channel()
        channel.exchange_declare(exchange=self.topic, exchange_type=self.exchange_type)
        channel.basic_publish(
            exchange=self.topic,
            routing_key=self.routing_key,
            body=data)
        connection.close()

    def send(self, data):
        thread = Thread(target=self.__callback, args=(data,))
        thread.start()

        return thread
