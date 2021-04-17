

import os
import sys
import threading
import time
import uuid


import stomp


ACTIVEMQ_PORT = 61613


user = os.getenv("ACTIVEMQ_USER") or "admin"
password = os.getenv("ACTIVEMQ_PASSWORD") or "password"
host = os.getenv("ACTIVEMQ_HOST") or "localhost"
port = os.getenv("ACTIVEMQ_PORT") or 61613
destination = sys.argv[1:2] or ["/topic/event"]
destination = destination[0]


class ActiveMQPublisher:

    def __init__(self, hostname='localhost', topic='message'):
        self.conn = stomp.Connection(host_and_ports=[(host, port)])
        self.conn.set_listener('', self)
        self.conn.start()
        self.conn.connect(login=user, passcode=password)
        self.topic = '/topic/' + topic
        self.message_id = 0
        self.uuid = str(uuid.uuid4())
        self.role = 'publisher'
        self.send_times = []
        self.recv_times = []
        self.lock = 0
        self.conn.subscribe(destination="/topic/"+self.uuid, id=2, ack='auto')

    def publish(self, message):
        while self.lock == 1:
            pass
        if self.lock == 0:
            self.lock = 1
            mId = self.uuid
            data_string = mId+":"+message
            self.conn.send(body=data_string, destination=self.topic,
                       persistent='false')
            self.send_times.append(time.time())


    def notify(self):
        pass
        
    def done(self):
        self.conn.send(body="SHUTDOWN", destination=destination,
                       persistent='false')
        self.conn.disconnect()
        for x, y in zip(self.send_times, self.recv_times):
            print("{},{}".format(x,y))

    def on_message(self, headers, message):
        self.lock = 0
        self.recv_times.append(time.time())

        
            

