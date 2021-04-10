#!/usr/bin/python3

from redisapi.redisclients import RedisSubscriber

HOSTNAME="129.114.25.240"

def main():
    loops = 1000
    sub = RedisSubscriber(hostname=HOSTNAME)
    run(sub, loops)
    
def run(sub, loops):
    for i in range(loops+1):
        sub.notify()


if __name__ == '__main__':
    main()
