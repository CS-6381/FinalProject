
import codecs
import json
import os
import threading
import time
import uuid


import redis


REDIS_PORT = 6379


class RedisPublisher:

    def __init__(self, hostname='localhost', topic='message'):
        self.r = redis.Redis(host=hostname, port=REDIS_PORT, db=0)
        self.p = self.r.pubsub()
        self.topic = topic
        self.message_id = 0
        self.uuid = str(uuid.uuid4())
        self.role = 'publisher'
        #self.csv_line = "{topic},{role},{uuid},{message_id},{time}"
        self.send_times = []
        self.recv_times = []
        self.p.subscribe(self.uuid)
        self.notify_thread = threading.Thread(target=self.notify_loop)
        
    def notify_loop(self):
        for i in range(1000+1):
            self.notify()
        for x, y in zip(self.send_times, self.recv_times):
            print("{},{}".format(x, y))

    def notify(self):
        data = None
        while not data:
            try:
                data = self.p.get_message()['data']
                data_decoded = codecs.decode(data, "utf-8")
                #data_json = json.loads(data_decoded)
                mId, message = data.split(":")
                if mId != self.uuid:
                    print("Something's wrong... id does not match uuid")
                else:
                    self.recv_times.append(time.time())
                return None
            except:
                pass
        

    def publish(self, message):
        mId = "{}".format(self.uuid)
        data_string = mId+":"+message
        self.r.publish(self.topic, data_string)
        self.send_time.append(time.time())
        


class RedisSubscriber:

    def __init__(self, hostname='localhost', topic='message'):
        self.r = redis.Redis(host=hostname, port=REDIS_PORT, db=0)
        self.p = self.r.pubsub()
        self.topic = topic
        self.role = 'subscriber'
        self.uuid = str(uuid.uuid4())
        self.p.subscribe(self.topic)

    def notify(self):
        data = None
        while not data:
            try:
                data = self.p.get_message()['data']
                data_decoded = codecs.decode(data, "utf-8")
                #data_json = json.loads(data_decoded)
                mId, message = data.split(":")
                self.r.publish(mId, "ok")
                return None
            except:
                pass
