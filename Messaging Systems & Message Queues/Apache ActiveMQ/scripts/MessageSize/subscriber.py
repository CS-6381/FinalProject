#!/usr/bin/python3

import sys 

from activemqapi.activemqsubscriber import ActiveMQSubscriber


def main():
    hostname = sys.argv[1] if len(sys.argv) > 1 else 'localhost'
    loops = 1000
    sub = ActiveMQSubscriber(hostname=hostname)
    run(sub, loops)
    
def run(sub, loops):
    for i in range(loops+1):
        sub.notify()


if __name__ == '__main__':
    main()
