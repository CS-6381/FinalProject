# Performance Experiment

The goal of this experiment is to benchmark how this technology performs when hardware resources are plentiful.

## Preliminary Steps

### Producer Program

Design a program utilizing your assigned MQ technology that produces as many messages per second as possible (For example: `while true: produceMessage()`)

The program should accept parameters to adjust:

1) The number of worker threads
2) The message size (in bytes)
3) The number of messages published in a batch (assuming your MQ supports batching)
  * 0 means batching turned off
4) The topic/queue name to publish to
5) The endpoint and port (if applicable) to connect to
6) For MQ's that run under multiple operating modes, accept a mode parameter that is a number
  * 1 = mode 1, 2 = mode 2, etc
  * An example of this would be RabbitMQ which can use "at most once" and "at least once" delivery by choosing whether or not to use acknowledgements. [Reference](https://www.rabbitmq.com/reliability.html)

For data collection, the program should output (to standard output) a CSV of message ID's, the time they were sent, and the time they were acknowledged (if applicable)).

Ex output:

```
1,1617516000,1617516005
2,1617516010,1617516015
...
```

### Consumer Program

Design a program utili

## 1 Producer - 1 Consumer