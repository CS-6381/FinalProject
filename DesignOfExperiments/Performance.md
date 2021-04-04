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

For MQ’s that run under multiple operating modes, run under the mode that is most reliable.
An example of this would be RabbitMQ which can use “at most once” and “at least once” delivery by choosing whether or not to use acknowledgements. [Reference](https://www.rabbitmq.com/reliability.html). You should choose “at least once”.

For data collection, the program should output (to standard output) a CSV of message ID’s, the time they were sent, and the acknowledge (ACK) response was received (if applicable).

Ex output:

```
1,1617516000,1617516005
2,1617516010,1617516015
...
```

The message ID’s need to be unique so it may be a good idea to use a unique ID prefix per publisher (or publisher thread).

**Note:** The reason we are using standard out is to prevent using file operations that could slow down the overall performance.

The program should terminate once all messages are sent and all acknowledgements are received.

Link to your program’s usage here:

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

Write a program that accepts a list of producer csv files and a list of consumer csv files. It should output 2 CSV’s that marry up the matching ID’s of messages and contains calculated results.

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

**Note**: If this program is written properly, it could be used by all experimenters across technologies.

## Hardware Configuration

Each test should be ran using Ubuntu 18.04 chameleon cloud VM’s with 8 CPU and 32 GB of RAM. If these hardware specs aren’t attainable, use the nearest available and document the configuration.

Each instance of a program should run on its own machine. For example, if the experiment calls for 2 instances of the producer program and 2 instances of the consumer program, there should be four machines total running one program each.

This does not account for redundancy/cluster configurations; those should be on separate machines as well.

# Experiment Configurations

These are the configurations your program should be ran in.

| Producer Instances | Producer Threads | Consumer Instances | Consumer Threads | Message Count | Message Size (bytes)  | Batch Size |
| —-- | —-- | —-- | —-- | —-- | —-- | --— |
| 1 | 1 | 1 | 1 | 1000 | 1000 | 0 |
| 1 | 1 | 1 | 5 | 1000 | 1000 | 0 |
| 1 | 5 | 1 | 1 | 1000 | 1000 | 0 |
| 3 | 8 | 3 | 8 | 10000 | 5000 | 5 |
| 4 | 25 | 4 | 25 | 100000 | 10000 | 10 |


These tests are described in detail below and have placeholders for results.

## 1 Producer - 1 Consumer

Run your producer for 1000 messages, 1000 bytes each. Do not enable batching.

Ensure you run your program in such a way that the output is not lost. For example: `python main.py > results.csv`.

Run your consumer program with a matching configuration.

Fill this table with the appropriate links:

| File Name | Link |
| —-- | --— |
| producer1.csv | |
| consumer1.csv | |
| latencies.csv | |
| throughput.csv| |

Calculate the following data using Excel or a custom program by analyzing the data in latencies.csv and throughput.csv

| Metric | Value |
| —— | — |
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

## 1 Producer - 1 Consumer: 5 Threads

Run your producer for 1000 messages, 1000 bytes each. Do not enable batching.

Ensure you run your program in such a way that the output is not lost. For example: `python main.py > results.csv`.

Run your consumer program with a matching configuration except it should run with 5 worker threads.

Fill this table with the appropriate links:

| File Name | Link |
| — | — |
| producer1.csv | |
| consumer1.csv | |
| latencies.csv | |
| throughput.csv| |

Calculate the following data using Excel or a custom program by analyzing the data in latencies.csv and throughput.csv

| Metric | Value |
| —— | — |
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

## 1 Producer: 5 Threads - 1 Consumer: 1 Thread

Run your producer with 5 threads for 1000 messages, 1000 bytes each. Do not enable batching.

Ensure you run your program in such a way that the output is not lost. For example: `python main.py > results.csv`.

Run your consumer program with a matching configuration except it should run with 1 worker thread.

Fill this table with the appropriate links:

| File Name | Link |
| — | — |
| producer1.csv | |
| consumer1.csv | |
| latencies.csv | |
| throughput.csv| |

Calculate the following data using Excel or a custom program by analyzing the data in latencies.csv and throughput.csv

| Metric | Value |
| —— | — |
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

## 3 Producers: 8 Threads - 3 Consumers: 8 Threads

Run 3 instances of your producer on three different machines with 8 threads for 10000 messages, 5000 bytes each. Set the batch size to 5.

Ensure you run your programs in such a way that the output is not lost. For example: `python main.py > results.csv`.

Run your consumer programs with  matching configurations.

Fill this table with the appropriate links:

| File Name | Link |
| — | — |
| producer1.csv | |
| producer2.csv | |
| producer3.csv | |
| consumer1.csv | |
| consumer2.csv | |
| consumer3.csv | |
| latencies.csv | |
| throughput.csv| |

Calculate the following data using Excel or a custom program by analyzing the data in latencies.csv and throughput.csv

| Metric | Value |
| —— | — |
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

## 4 Producers: 25 Threads - 4 Consumers: 25 Threads

Run four instances of your producer on four different machines with 25 threads for 100000 messages, 10000 bytes each. Set the batch size to 10.

Ensure you run your programs in such a way that the output is not lost. For example: `python main.py > results.csv`.

Run your consumer programs with  matching configurations.

Fill this table with the appropriate links:

| File Name | Link |
| — | — |
| producer1.csv | |
| producer2.csv | |
| producer3.csv | |
| producer4.csv | |
| consumer1.csv | |
| consumer2.csv | |
| consumer3.csv | |
| consumer4.csv | |
| latencies.csv | |
| throughput.csv| |

Calculate the following data using Excel or a custom program by analyzing the data in latencies.csv and throughput.csv

| Metric | Value |
| —— | — |
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