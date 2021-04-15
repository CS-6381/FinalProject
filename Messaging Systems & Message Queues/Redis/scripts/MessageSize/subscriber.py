#!/usr/bin/python3

from redisapi.redisclients import RedisSubscriber


def main():
    sub = RedisSubscriber()
    run(sub)
    
def run(sub):
    while True:
        try:
            data = sub.notify()
            print(data)
        except Exception as e:
            pass

if __name__ == '__main__':
    main()
