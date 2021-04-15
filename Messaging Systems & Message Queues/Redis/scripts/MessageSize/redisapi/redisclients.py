
import codecs
import json
import time

import redis


REDIS_PORT = 6379


class RedisPublisher:

    def __init__(self, hostname='localhost', topic='message'):
        self.r = redis.Redis(host=hostname, port=REDIS_PORT, db=0)
        self.topic = topic
        self.message_id = 0
        
    def publish(self, message):
        data = {}
        data['message_id'] = self.message_id
        data['message'] = message
        data['time'] = time.time()
        data_string = json.dumps(data)
        self.r.publish(self.topic, data_string)
        self.message_id += 1


class RedisSubscriber:

    def __init__(self, hostname='localhost', topic='message'):
        self.r = redis.Redis(host=hostname, port=REDIS_PORT, db=0)
        self.p = self.r.pubsub()
        self.topic = topic
        self.p.subscribe(self.topic)

    def notify(self):
        data = self.p.get_message()['data']
        data_decoded = codecs.decode(data, "utf-8")
        data_json = json.loads(data_decoded)
        travel_time = time.time() - data_json['time']
        return travel_time
