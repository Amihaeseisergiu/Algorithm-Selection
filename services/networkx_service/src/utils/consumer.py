import threading
import pika
from networkx_service.src.security.credentials import CredentialsProvider


class Consumer(threading.Thread):
    def __init__(self, exchange, callback, *args, **kwargs):
        super(Consumer, self).__init__(*args, **kwargs)

        self.exchange = exchange
        self.callback = callback

    def run(self):
        parameters = pika.ConnectionParameters(host='rabbitmq', credentials=CredentialsProvider.get())

        connection = pika.BlockingConnection(parameters)

        channel = connection.channel()
        channel.exchange_declare(exchange=self.exchange, exchange_type='fanout')
        result = channel.queue_declare(queue="", exclusive=True, auto_delete=False)

        channel.queue_bind(result.method.queue,
                           exchange=self.exchange,
                           routing_key="")
        channel.basic_consume(on_message_callback=self.callback,
                              queue=result.method.queue, auto_ack=True)

        channel.start_consuming()
