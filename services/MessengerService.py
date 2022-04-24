
#!/usr/bin/env python
from asyncio.windows_events import NULL
from hashlib import new
import json
from flask import jsonify
import pika

from entities.Notification import Notification


class MessengerService:
    RABBITMQ_URL = 'localhost'
    RABBITMQ_QUEUE = 'v2.messenger'

    DATARECEIEVD = []

    def __init__(self):
        self.initilize()
        # xt =  Notification()
        # xt.set_notification_channel("EMAIL")
        # xt.set__notification_body("TEST")
        # xt.set_notificatiton_subect("TEST")
        # xt.set_notification_template("template")
        # # # //this willbe interpreted
        # # # by the service intended,which is the channel determines which service
        # xt.set_notification_recipients("recipient,recipient2,recipient")

        # # notificationJSONData = json.dumps(xt.toJSON(),indent=4)
        # self.DATARECEIEVD.append(xt.toJSON())

    def initilize(self):
        self.rabbitMqConnection = pika.BlockingConnection(
            pika.ConnectionParameters(self.RABBITMQ_URL))
        self.channel = self.rabbitMqConnection.channel()
        self.channel.queue_declare(queue=self.RABBITMQ_QUEUE)

        self.start_consuming()
        self.channel.basic_consume(
            queue=self.RABBITMQ_QUEUE, on_message_callback=self.callback, auto_ack=True)

    def start_consuming(self):
        self.channel.start_consuming()

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
        self.channel.basic_publish(exchange='',
                                   routing_key=self.RABBITMQ_QUEUE,
                                   body=jsonStr)
        self.rabbitMqConnection.close()

        return "sent message"

    def receiveMessage(self):

        # self.DATARECEIEVD.append(xt)
        # str = json.dumps(self.DATARECEIEVD.isoformat())
        # ''.join([str(item) for item in self.DATARECEIEVD])
        return self.DATARECEIEVD

    def callback(self, ch, method, properties, body):
        self.DATARECEIEVD.append(body)
        print(" [x] Received %r" % body)
