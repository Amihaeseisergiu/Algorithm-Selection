import pika
import time
from threading import Thread
from security.credentials import CredentialsProvider


class Publisher:
    def __init__(self, topic):
        self.topic = topic

    def __callback(self, data, delay):
        time.sleep(delay)

        parameters = pika.ConnectionParameters(host='rabbitmq', credentials=CredentialsProvider.get_credentials())

        connection = pika.BlockingConnection(parameters)
        channel = connection.channel()
        channel.exchange_declare(exchange=self.topic, exchange_type='fanout')
        channel.basic_publish(
            exchange=self.topic,
            routing_key='',
            body=data)
        connection.close()

    def send(self, data, delay=0):
        thread = Thread(target=self.__callback, args=(data, delay,))
        thread.start()