#!/usr/bin/env python
from multiprocessing import Pool
import pika
import threading
class Rabb(object):
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='hello')

    def send(self, msg):
        self.channel.basic_publish(exchange='', routing_key='hello', body=msg)
        print(" [x] Sent %r" + msg)

    def callback(self, ch, method, properties, body):
        print(" [x] Received %r" % body)

    def retrieve(self):
        self.channel.basic_consume(self.callback,
                      queue='hello',
                      no_ack=True)
        self.channel.start_consuming()
        
    def close(self):
        self.connection.close()



class Pt(object):
    def __init__(self):
        self.mq = Rabb()

    def startSend(self,max):
        for i in range(1,max):
            t = threading.Thread(target = self.mq.send, args = str(i))
            t.daemon = True
            t.start()
    def startReceive(self):
        self.mq.retrieve()

pt = Pt()
pt.startSend(1000**2)
