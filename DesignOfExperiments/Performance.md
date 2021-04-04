# Performance Experiment

The goal of this experiment is to benchmark how this technology performs when hardware resources are plentiful.

## Preliminary Steps

### Producer Program

Design a **python** program utilizing your assigned MQ technology that produces as many messages per second as possible (For example: `while true: produceMessage()`)

The program should accept parameters to adjust:

1) The number of worker threads
2) The message size (in bytes)
3) Batch size (assuming your MQ supports batching)
  * 0 means batching turned off
4) The topic/queue name to publish to
5) The endpoint and port (if applicable) to connect to
6) For MQ's that run under multiple operating modes, accept a mode parameter that is a number
  * 1 = mode 1, 2 = mode 2, etc
  * An example of this would be RabbitMQ which can use "at most once" and "at least once" delivery by choosing whether or not to use acknowledgements. [Reference](https://www.rabbitmq.com/reliability.html)
7) The number of messages to produce (per worker thread)

For data collection, the program should output (to standard output) a CSV of message ID's, the time they were sent, and the acknowledge (ACK) response was received (if applicable).

Ex output:

```
1,1617516000,1617516005
2,1617516010,1617516015
...
```

### Consumer Program

Design a **python** program utilizing your assigned MQ technology that consumes as many messages per second as possible (For example: `while true: consumeMessage()`)

The program should accept parameters to adjust:

1) The number of worker threads
2) Batch size (assuming your MQ supports batching)
  * 0 means batching turned off
3) The topic/queue name to consume from
4) The endpoint and port (if applicable) to connect to
5) For MQ's that run under multiple operating modes, accept a mode parameter that is a number
  * 1 = mode 1, 2 = mode 2, etc
  * An example of this would be RabbitMQ which can use "at most once" and "at least once" delivery by choosing whether or not to use acknowledgements. [Reference](https://www.rabbitmq.com/reliability.html)
6) The number of messages to consume

The program should terminate once all messages are consumed.

For data collection, the program should output (to standard output) a CSV of message ID's, the time they were received, and the time they were acknowledged (if applicable).

Ex output:

```
1,1617516000,1617516005
2,1617516010,1617516015
...
```

## 1 Producer - 1 Consumer

