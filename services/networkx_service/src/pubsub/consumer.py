import pika
from threading import Thread
from security.credentials import CredentialsProvider


class Consumer:
    def __init__(self, topic, message_processor):
        self.topic = topic
        self.message_processor = message_processor

    def _consume_callback(self):
        parameters = pika.ConnectionParameters(host='rabbitmq', credentials=CredentialsProvider.get_credentials())

        connection = pika.BlockingConnection(parameters)

        channel = connection.channel()
        channel.exchange_declare(exchange=self.topic, exchange_type='fanout')
        result = channel.queue_declare(queue="", exclusive=True, auto_delete=True)

        channel.queue_bind(result.method.queue,
                           exchange=self.topic,
                           routing_key="")
        channel.basic_qos(prefetch_count=1)
        channel.basic_consume(on_message_callback=self.message_processor,
                              queue=result.method.queue, auto_ack=True)

        channel.start_consuming()

    def consume(self):
        thread = Thread(target=self._consume_callback)
        thread.start()
