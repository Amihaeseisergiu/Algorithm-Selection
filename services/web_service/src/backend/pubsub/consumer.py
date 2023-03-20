import pika
import time
from threading import Thread
from security.credentials import CredentialsProvider


class Consumer:
    def __init__(self, topic, exchange_type, queue, routing_key, exclusive, auto_delete, durable, message_processor,
                 socketio):
        self.topic = topic
        self.exchange_type = exchange_type
        self.queue = queue
        self.routing_key = routing_key
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

        while True:
            try:
                connection = pika.BlockingConnection(parameters)

                channel = connection.channel()
                channel.basic_qos(prefetch_count=1)
                channel.exchange_declare(exchange=self.topic, exchange_type=self.exchange_type)
                result = channel.queue_declare(queue=self.queue, exclusive=self.exclusive, auto_delete=self.auto_delete,
                                               durable=self.durable)

                channel.queue_bind(queue=result.method.queue,
                                   exchange=self.topic,
                                   routing_key=self.routing_key)
                channel.basic_consume(on_message_callback=self.__message_callback,
                                      queue=result.method.queue, auto_ack=False)

                try:
                    channel.start_consuming()
                except KeyboardInterrupt:
                    channel.stop_consuming()
                    connection.close()
                    break
            except pika.exceptions.ConnectionClosedByBroker:
                continue
            except pika.exceptions.AMQPConnectionError:
                continue
            except pika.exceptions.AMQPChannelError as err:
                break
            except:
                time.sleep(0.1)
                continue

    def consume(self):
        thread = Thread(target=self.__consume_callback)
        thread.start()
