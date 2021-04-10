#!/usr/bin/python3

import sys

from redisapi.redisclients import RedisPublisher



MESSAGE_DIR="/home/vagrant/FinalProject/DesignOfExperiments/messages/"
MESSAGE_SUFFIX = ".txt"

messages = [
    "small",
]



def main():
    loops = 1000
    file = messages[0]
        
    publisher = RedisPublisher()

    filename = MESSAGE_DIR + file + MESSAGE_SUFFIX
    
    with open(filename, "r") as f:
        data = f.read()
        
    run(publisher, data, loops)
    
def run(publisher, data, loops):
    count = 0
    for i in range(loops):
        publisher.publish(data)
        
if __name__ == '__main__':
    main()
