
import codecs
import json
import os
import time
import uuid


import redis


REDIS_PORT = 6379


class RedisPublisher:

    def __init__(self, hostname='localhost', topic='message'):
        self.r = redis.Redis(host=hostname, port=REDIS_PORT, db=0)
        self.topic = topic
        self.message_id = 0
        self.uuid = str(uuid.uuid4())
        self.role = 'publisher'
        self.csv_line = "{topic},{role},{uuid},{message_id},{time}"
        
    def publish(self, message):
        data = {}
        data['message_id'] = "{}".format(self.message_id)
        data['message'] = message
        data['time'] = time.time()
        data_string = json.dumps(data)
        self.r.publish(self.topic, data_string)
        sent_time = time.time()
        print(self.csv_line.format(topic=self.topic,
                                   role=self.role,
                                   uuid=self.uuid,
                                   message_id=self.message_id,
                                   time=sent_time))
        self.message_id += 1


class RedisSubscriber:

    def __init__(self, hostname='localhost', topic='message'):
        self.r = redis.Redis(host=hostname, port=REDIS_PORT, db=0)
        self.p = self.r.pubsub()
        self.topic = topic
        self.role = 'subscriber'
        self.uuid = str(uuid.uuid4())
        self.csv_line = "{topic},{role},{uuid},{message_id},{time}"
        self.p.subscribe(self.topic)

    def notify(self):
        data = None
        while not data:
            try:
                data = self.p.get_message()['data']
                data_decoded = codecs.decode(data, "utf-8")
                data_json = json.loads(data_decoded)
                recv_time = time.time()
                print(self.csv_line.format(topic=self.topic,
                                   role=self.role,
                                   uuid=self.uuid,
                                   message_id=data_json["message_id"],
                                   time=recv_time))
                return travel_time
            except:
                pass
