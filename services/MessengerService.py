
#!/usr/bin/env python
from asyncio.windows_events import NULL
import pika


 
class  MessengerService:
    RABBITMQ_URL='localhost'
    RABBITMQ_QUEUE='v1.messenger'

  

    def __init__(self):
         self.initilize()

    def initilize(self):
        self.rabbitMqConnection  =   pika.BlockingConnection(pika.ConnectionParameters(self.RABBITMQ_URL))
        self.channel = self.rabbitMqConnection.channel()
        self.channel.queue_declare(queue=self.RABBITMQ_QUEUE)

    
    def sendMessage(self):
        self.channel.basic_publish(exchange='',
                      routing_key=self.RABBITMQ_QUEUE,
                      body='Hello World!') 
        self.rabbitMqConnection.close()
        return "sent message"

    def receiveMessage(self):
        self.channel.basic_consume(queue=self.RABBITMQ_QUEUE, on_message_callback=self.callback, auto_ack=True)
    
 
    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)