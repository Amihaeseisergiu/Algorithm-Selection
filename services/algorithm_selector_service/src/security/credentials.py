import os
import pika


class CredentialsProvider:
    @staticmethod
    def get_credentials():
        rabbitmq_user = os.environ["RABBITMQ_USER"]
        rabbitmq_pass = os.environ["RABBITMQ_PASS"]

        return pika.PlainCredentials(rabbitmq_user, rabbitmq_pass)
