#!/usr/bin/python3

import sys 

from redisapi.redisclients import RedisSubscriber


def main():
    hostname = sys.argv[1] if len(sys.argv) > 1 else 'localhost'
    loops = 1000
    sub = RedisSubscriber(hostname=hostname)
    run(sub, loops)
    
def run(sub, loops):
    for i in range(loops+1):
        sub.notify()


if __name__ == '__main__':
    main()
