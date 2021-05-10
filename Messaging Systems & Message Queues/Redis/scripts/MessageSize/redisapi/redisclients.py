
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
        self.send_times = []
        self.recv_times = []
        self.notify_threads = []
        self.p.subscribe(self.uuid)
        
    def done(self):
        # there could be an issue where len(y) > len(x)
        # we can trim off the first y value and pull all others earlier. 
        # not sure why this is happening, but could be related to that data value 1
        for x, y in zip(self.send_times, self.recv_times[1:]):
            print("{},{}".format(x, y))

    def notify(self):
        data = None
        for message in self.p.listen():
            if message.get("type") == "message":
                data = message.get("data")
                # other possible fix for time weirdness -- adjust to filter out noise
                if data == b'ok':
                    data_decoded = codecs.decode(data, "utf-8")
                    #print("got it")
                    self.recv_times.append(time.time())
                    return None

        

    def publish(self, message):
        self.notify_threads.append(threading.Thread(target=self.notify))
        self.notify_threads[-1].start()
        mId = self.uuid
        data_string = mId+":"+message
        self.r.publish(self.topic, data_string)
        self.send_times.append(time.time())
        self.notify_threads[-1].join() 


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
        for message in self.p.listen():
            if message.get("type") == "message":
                data = message.get("data")
                #print(data)
                data_decoded = codecs.decode(data, "utf-8")
                mId, message = data_decoded.split(":")
                self.r.publish(mId, "ok")
                return None

