
#!/usr/bin/env python
import pika


class  MessengerService:
    

    def __init__(self, *args, **kwargs):
         self.rabbitMqConnection  =   pika.BlockingConnection(pika.ConnectionParameters('localhost'))
         self.channel = self.rabbitMqConnection.channel()

    
    def sendMessage(self):
        self.channel.queue_declare(queue='hello')
        self.channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
        print("[x] sent `Hello world!` ")
        self.rabbitMqConnection.close()

    def receiveMessage():
        pass
    
 
