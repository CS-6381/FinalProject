#!/usr/bin/python3

import sys

from redisapi.redisclients import RedisPublisher



MESSAGE_DIR="/home/cc/official/FinalProject/DesignOfExperiments/messages/"
MESSAGE_SUFFIX = ".txt"

messages = [ "tiny", "small", "medium", "large", "xlarge" ]



def main():
    print("Starting...")
    hostname = sys.argv[1] if len(sys.argv) > 1 else 'localhost'
    file = sys.argv[2] if len(sys.argv) > 2 else 'small'
    loops = 1000 
    print("File:\t{}".format(file))
        
    publisher = RedisPublisher(hostname=hostname)

    filename = MESSAGE_DIR + file + MESSAGE_SUFFIX
    
    with open(filename, "r") as f:
        data = f.read()
        
    run(publisher, data, loops)
    
def run(publisher, data, loops):
    count = 0
    for i in range(loops):
        publisher.publish(data)

    publisher.done()

if __name__ == '__main__':
    main()
