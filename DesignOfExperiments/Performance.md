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
6) The number of messages to produce (per worker thread)

For MQ's that run under multiple operating modes, run under the mode that is most reliable.
An example of this would be RabbitMQ which can use "at most once" and "at least once" delivery by choosing whether or not to use acknowledgements. [Reference](https://www.rabbitmq.com/reliability.html). You should choose "at least once".

For data collection, the program should output (to standard output) a CSV of message ID's, the time they were sent, and the acknowledge (ACK) response was received (if applicable).

Ex output:

```
1,1617516000,1617516005
2,1617516010,1617516015
...
```

The message ID's need to be unique so it may be a good idea to use a unique ID prefix per publisher (or publisher thread).

**Note:**: The reason we are using standard out is to prevent using file operations that could slow down the overall performance.

The program should terminate once all messages are sent and all acknowledgements are received.

Link to your program's usage here:

[Replace me](Replace me)

### Consumer Program

Design a **python** program utilizing your assigned MQ technology that consumes as many messages per second as possible (For example: `while true: consumeMessage()`)

The program should accept parameters to adjust:

1) The number of worker threads
2) Batch size (assuming your MQ supports batching)
  * 0 means batching turned off
3) The topic/queue name to consume from
4) The endpoint and port (if applicable) to connect to
5) The number of messages to consume

For MQ's that run under multiple operating modes, run under the mode that is most reliable.
An example of this would be RabbitMQ which can use "at most once" and "at least once" delivery by choosing whether or not to use acknowledgements. [Reference](https://www.rabbitmq.com/reliability.html). You should choose "at least once".

The consumer doesn't have to do anything with the message; only retrieve it.

The program should terminate once all messages are consumed.

For data collection, the program should output (to standard output) a CSV of message ID's, the time they were received, and the time they were acknowledged (if applicable).

Ex output:

```
1,1617516000,1617516005
2,1617516010,1617516015
...
```

Link to your program's usage here:

[Replace me](Replace me)

### Data Processor

Write a program that accepts a list of producer csv files and a list of consumer csv files. It should output 2 CSV's that marry up the matching ID's of messages and contains calculated results.

The first csv should contain the following durations:
* Processing latency - total duration in milliseconds from the time the message is sent to the time the message is received
* Send time - total duration in milliseconds from the time the message is sent to the time the message arrives at the broker/queue/system (this is likely the ACK received time)

## Hardware Configuration

Each test should be ran using Ubuntu 18.04 chameleon cloud VM's with 8 CPU and 32 GB of RAM. If these hardware specs aren't attainable, use the nearest available and document the configuration.

Each instance of a program should run on its own machine. For example, if the experiment calls for 2 instances of the producer program and 2 instances of the consumer program, there should be four machines total running one program each.

This does not account for redundancy/cluster configurations; those should be on separate machines as well.

# Experiment Configurations

## 1 Producer - 1 Consumer

Run your producer for 1000 messages, 1000 bytes each. Do not enable batching.

Ensure you run your program in such a way that the output is not lost. For example: `python main.py > results.csv`.

Run your consumer program with a matching configuration.

Place a link 