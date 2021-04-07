# Performance Experiment - MQ - Message Size

The goal of this experiment is to benchmark how this technology performs when hardware resources are plentiful and the number of actors (publishers and subscribers) in the system varies.

Contact [@jmbeach](https://github.com/jmbeach) or [@laynemoseley](https://github.com/laynemoseley) for clarifications.

## Preliminary Steps

### Producer Program

Design a **python** program utilizing your assigned MQ technology that produces as many messages per second as possible (For example: `while true: produce_message()`)

For MQ’s that run under multiple operating modes, run under the mode that is most reliable.
An example of this would be RabbitMQ which can use “at most once” and “at least once” delivery by choosing whether or not to use acknowledgements. [Reference](https://www.rabbitmq.com/reliability.html). You should choose “at least once”.

For data collection, the program should output (to standard output) a CSV of message ID’s, the time they were sent, and the time the acknowledge (ACK) response was received (if applicable).

Ex output:

```
1,1617516000,1617516005
2,1617516010,1617516015
...
```

### Message Size

This test is similar to the Actor Count test, with one exception. We will run this test in 5 different modes with varying message size.

**Note:** The reason we are using standard out is to prevent using file operations that could slow down the overall performance.

The program should send 1,000 messages and then terminate once all messages are sent and all acknowledgements are received.

Link to your program’s usage here:

[Replace me](Replace me)

### Consumer Program

Design a **python** program utilizing your assigned MQ technology that consumes as many messages per second as possible (For example: `while true: consume_message()`)

For MQ’s that run under multiple operating modes, run under the mode that is most reliable.
An example of this would be RabbitMQ which can use “at most once” and “at least once” delivery by choosing whether or not to use acknowledgements. [Reference](https://www.rabbitmq.com/reliability.html). You should choose “at least once”.

The consumer doesn’t have to do anything with the message; only retrieve it.

The program should terminate once all messages are consumed.

For data collection, the program should output (to standard output) a CSV of message ID’s, the time they were received, and the time they were acknowledged (if applicable).

Ex output:

```
1,1617516000,1617516005
2,1617516010,1617516015
...
```

Link to your program’s usage here:

[Replace me](Replace me)

### Data Processor

The experiment designers will provide a program that accepts a list of producer csv files and a list of consumer csv files. It should output 2 CSV’s that marry up the matching ID’s of messages and contains calculated results.

The first csv should contain the following durations:
* Processing latency - total duration in milliseconds from the time the message is sent to the time the message is received
* Send time - total duration in milliseconds from the time the message is sent to the time the message arrives at the broker/queue/system (this is likely the ACK received time)

Ex:

```
1,15,8
2,8,4
...
```

The above output indicates that message 1 took 15ms to be fully processed and 8ms to be sent to the broker.

The second csv should output the number of messages sent in each second of the experiment and the number of messages received in each second of the experiment. This is the throughput.

```
1,15,30
2,8,16
...
```

The above output indicates that the end to end throughput in second 1 was 15 and the send to broker throughput in second 1 was 16.

Link to program pending.

## Hardware Configuration

Each test should be ran using Ubuntu 18.04 chameleon cloud VM’s with 8 CPU and 32 GB of RAM. If these hardware specs aren’t attainable, use the nearest available and document the configuration.

# Experiment Configurations

These are the configurations your program should be ran in.

| Producer Machines | Producer Instances | Consumer Machines | Consumer Instances | Message Size |
| --- | --- | --- | --- | --- |
| 1 | 1 | 1 | 1 | tiny |
| 1 | 1 | 1 | 1 | small |
| 1 | 1 | 1 | 1 | medium |
| 1 | 1 | 1 | 1 | large |
| 1 | 1 | 1 | 1 | x-large |

If possible, implement these configurations with redundancy enabled and document the configuration.

## Redundancy implementation Details

Place the redundancy implementation details here.

## 1 Producer - 1 Consumer

Run one instance of your producer program on one VM. The test should then be repeated for each message size, with a total of 5 test runs.

Ensure you run your programs in such a way that the output is not lost. For example: `python main.py > results.csv`.

Run your consumer program with a matching configuration.

Fill this table with the appropriate links:

| File Name | Link |
| --- | --- |
| producer1.csv | |
| consumer1.csv | |
| latencies.csv | |
| throughput.csv| |

Calculate the following data using Excel or a custom program by analyzing the data in latencies.csv and throughput.csv

| Metric | Value |
| --- | --- |
| Processing Latency Min | |
| Processing Latency Max | |
| Processing Latency Average | |
| Processing Latency Standard Deviation | |
| Send Time Min | |
| Send Time Max | |
| Send Time Average | |
| Send Time Standard Deviation | |
| Processing Throughput Min | |
| Processing Throughput Max | |
| Processing Throughput Average | |
| Processing Throughput Standard Deviation | |
| Send Throughput Min | |
| Send Throughput Max | |
| Send Throughput Average | |
| Send Throughput Standard Deviation | |
