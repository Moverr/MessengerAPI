
#!/usr/bin/env python
import pika


class  MessengerService:
    

    def __init__(self):
         self.rabbitMqConnection  =   pika.BlockingConnection(pika.ConnectionParameters('localhost'))
         self.channel = self.rabbitMqConnection.channel()
         self.channel.queue_declare(queue='v1.messenger')

    
    def sendMessage(self):
        self.channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
        print("[x] sent `Hello world!` ")
        self.rabbitMqConnection.close()

    def receiveMessage(self):
        self.channel.basic_consume(queue='v1.messenger', on_message_callback=self.callback, auto_ack=True)
    
 
    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)