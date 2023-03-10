import pika
from security.credentials import CredentialsProvider


class Consumer:
    def __init__(self, topic, queue, exclusive, auto_delete, durable, message_processor, socketio):
        self.topic = topic
        self.queue = queue
        self.exclusive = exclusive
        self.auto_delete = auto_delete
        self.durable = durable
        self.__message_processor = message_processor
        self.socketio = socketio

    def __message_callback(self, channel, method, properties, body):
        self.__message_processor(body)

        channel.basic_ack(delivery_tag=method.delivery_tag)

    def __consume_callback(self):
        parameters = pika.ConnectionParameters(host='rabbitmq', credentials=CredentialsProvider.get_credentials())

        connection = pika.BlockingConnection(parameters)

        channel = connection.channel()
        channel.basic_qos(prefetch_count=1)
        channel.exchange_declare(exchange=self.topic, exchange_type='fanout')
        result = channel.queue_declare(queue=self.queue, exclusive=self.exclusive, auto_delete=self.auto_delete,
                                       durable=self.durable)

        channel.queue_bind(queue=result.method.queue,
                           exchange=self.topic,
                           routing_key="")
        channel.basic_consume(on_message_callback=self.__message_callback,
                              queue=result.method.queue, auto_ack=False)

        channel.start_consuming()

    def consume(self):
        self.socketio.start_background_task(target=self.__consume_callback)