
from asyncio.windows_events import NULL
from hashlib import new
import json
from flask import jsonify
import pika

from entities.Notification import Notification


class MessengerService:
    RABBITMQ_URL = 'localhost'
    RABBITMQ_QUEUE = 'v1.messenger'

    DATARECEIEVD = []

    def __init__(self):
        pass

    def initilize(self):
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()
        channel.queue_declare(queue=self.RABBITMQ_QUEUE)

        def callback(ch, method, properties, body):
            print(" [x] Received %r" % body)
            self.DATARECEIEVD.append(body)
        channel.basic_consume(queue=self.RABBITMQ_QUEUE,
                              on_message_callback=callback, auto_ack=True)

        print(' [*] Waiting for messages. To exit press CTRL+C')
        channel.start_consuming()

    def start_consuming(self):
        self.channel.basic_consume(
            queue=self.RABBITMQ_QUEUE, on_message_callback=self.callback, auto_ack=True)

    def sendMessage(self):

        xt = Notification()
        xt.set_notification_channel("EMAIL")
        xt.set__notification_body("TEST")
        xt.set_notificatiton_subect("TEST")
        xt.set_notification_template("template")
        # //this willbe interpreted
        # by the service intended,which is the channel determines which service
        xt.set_notification_recipients("recipient,recipient2,recipient")

        jsonStr = json.dumps(xt.toJSON())

        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()

        channel.queue_declare(queue=self.RABBITMQ_QUEUE)

        channel.basic_publish(
            exchange='', routing_key=self.RABBITMQ_QUEUE, body=jsonStr)
        print(" [x] Sent 'Hello World!'")
        connection.close()

    def receiveMessage(self):
        self.initilize()
        return self.DATARECEIEVD
