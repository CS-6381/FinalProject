# Performance Experiment - MQ - Actor Count

The goal of this experiment is to benchmark how this technology performs when hardware resources are plentiful and the number of actors (publishers and subscribers) in the system varies.

Contact [@jmbeach](https://github.com/jmbeach) or [@laynemoseley](https://github.com/laynemoseley) for clarifications.

## Preliminary Steps

### Producer Program

Design a **python** program utilizing your assigned MQ technology that produces as many messages per second as possible (For example: `while true: produce_message()`). Each producer will produce messages to the same topic.

For MQ’s that run under multiple operating modes, run under the mode that is most reliable.
An example of this would be RabbitMQ which can use “at most once” and “at least once” delivery by choosing whether or not to use acknowledgements. [Reference](https://www.rabbitmq.com/reliability.html). You should choose “at least once”.

For data collection, the program should output (to standard output) a CSV of message send timestamps, and a timestamp of when the acknowledge (ACK) response was received (if your MQ does not support delivery gaurantees, you will need to take some extra measures. See "Notes for MQ's Without ACK" below).

Ex output:

```
1617516000,1617516005
1617516010,1617516015
...
```

Each message from the producer should be the exact same. A byte UTF-8 string of the following quote:

> There are not more than five primary colors (blue, yellow, red, white, and black), yet in combination they produce more hues than can ever been seen.

This is a quote from [Sun Tzu's Art of War](https://www.gutenberg.org/files/132/132-h/132-h.htm#:~:text=There%20are%20not%20more%20than%20five%20musical%20notes) and it's a fun, small, public-domain message that will ensure that everyone is using a message of the exact same size (149 bytes).

**Note:** The reason we are using standard out is to prevent using file operations that could slow down the overall performance.

The program should send 1,000 messages and then terminate once all messages are sent and all acknowledgements are received.

Link to your program’s usage here:

[Replace me](Replace me)

#### Notes For MQ's Without ACK

If your MQ does not support some sort of acknowledgement protocol that will ensure that the program does not advance until the message is fully received by the consumer, then you will need to do the following:

* Include the producer's ID with the message
    * How this ID is generated is up to you
* Upon receiving the message in the consumer, manually implement your own response back to the producer.
    * This can either be a direct response over the network to your program 
    * *OR*, you can make your producer also be a consumer and have it listen for messages with its ID

To include the ID with the message without adding a lot of processing overhead to your consumer, simply prefix the message with the ID followed by a colon.

Example:

```
192.168.1.100_PRODUCER1:There are not more than five primary colors (blue, yellow, red, white, and black), yet in combination they produce more hues than can ever been seen.
```

Then in the consumer, use an efficient algorithm to read the ID from the message. It doesn't need to read anything past the colon. The ID is only used to route the response back to the producer (either by broker or other means).

One downside to this approach is that all other MQ's will have only one topic, whereas this MQ will have `N + 1` topics (where N is the number of producers).

These extra steps will help us compare all of the technologies with less variance between them.

### Consumer Program

Design a **python** program utilizing your assigned MQ technology that consumes as many messages per second as possible (For example: `while true: consume_message()`). The consumer programs should all subscribe to the same topic.

For MQ’s that run under multiple operating modes, run under the mode that is most reliable.
An example of this would be RabbitMQ which can use “at most once” and “at least once” delivery by choosing whether or not to use acknowledgements. [Reference](https://www.rabbitmq.com/reliability.html). You should choose “at least once”.

The consumer doesn’t have to do anything with the message; only retrieve it. It also doesn't have to output anything.

The program should terminate once all messages are consumed.

Link to your program’s usage here:

[Replace me](Replace me)

### Data Processor

The experiment **designers** will provide a program that accepts a list of producer csv files. It should output 2 CSV’s that contain calculated results.

The first csv should contain the following duration:
* Processing latency - total duration in milliseconds from the time the message is sent to the time the message is received

Ex:

```
15
8
...
```

The above output indicates that message 1 took 15ms to be fully processed. The second line indicates that message 2 took 8ms to be fully processed

The second csv should output the number of messages sent in each second of the experiment. Because we are only collecting data from the producer, we are not differentiating between send and receive throughput, because they should be the same. The producer cannot move on to another message until it has received an ack from the consumer.

```
9
7
...
```

The above output indicates that the end to end throughput in second 1 was 9 messages per second. The second line indicates that in second 2, the throughput was 7 messages per second.

**Link to program pending.**

## Hardware Configuration

Each test should be ran using Ubuntu 20.04 (CC-Ubuntu20.04) chameleon cloud VM’s with 8 CPU and 16 GB of RAM (m1.xlarge). If these hardware specs aren’t attainable, use the nearest available and document the configuration.

# Experiment Configurations

These are the configurations your program should be ran in. Although it is not shown, there should be a separate machine instance for the broker.

| Producer Machines | Producer Instances | Consumer Machines | Consumer Instances |
| --- | --- | --- | --- |
| 1 | 1 | 1 | 1 |
| 1 | 1 | 1 | 5 |
| 1 | 5 | 1 | 1 |
| 3 | 8 | 3 | 8 |
| 4 | 25 | 4 | 25 |

If possible, implement these configurations with redundancy enabled and document the configuration.

These tests are described in detail below and have placeholders for results.

## Redundancy Implementation Details

Place the redundancy implementation details here.

## 1 Producer - 1 Consumer

Run one instance of your producer program on one VM.

Ensure you run your programs in such a way that the output is not lost. For example: `python main.py > results.csv`.

Run your consumer program with a matching configuration.

Generate `latencies.csv` and `throughput.csv` using the program provided by the experiment designers team.

Fill this table with the appropriate links:

| File Name | Link |
| --- | --- |
| producer.csv | |
| latencies.csv | |
| throughput.csv| |

Calculate the following data using Excel or a custom program by analyzing the data in latencies.csv and throughput.csv

| Metric | Value |
| --- | --- |
| Processing Latency Min | |
| Processing Latency Max | |
| Processing Latency Average | |
| Processing Latency Standard Deviation | |
| Processing Throughput Min | |
| Processing Throughput Max | |
| Processing Throughput Average | |
| Processing Throughput Standard Deviation | |

## 1 Producer VM - 1 Consumer VM: 5 Instances

Run one instance of your producer program on one VM.

Ensure you run your programs in such a way that the output is not lost. For example: `python main.py > results.csv`.

Run five consumer program instances on one VM.

Generate `latencies.csv` and `throughput.csv` using the program provided by the experiment designers team.

Fill this table with the appropriate links:

| File Name | Link |
| --- | --- |
| producer.csv | |
| latencies.csv | |
| throughput.csv| |

Calculate the following data using Excel or a custom program by analyzing the data in latencies.csv and throughput.csv

| Metric | Value |
| --- | --- |
| Processing Latency Min | |
| Processing Latency Max | |
| Processing Latency Average | |
| Processing Latency Standard Deviation | |
| Processing Throughput Min | |
| Processing Throughput Max | |
| Processing Throughput Average | |
| Processing Throughput Standard Deviation | |

## 1 Producer VM: 5 Instances - 1 Consumer VM: 1 Instance

Run five producer program instances on one VM.

Ensure you run your programs in such a way that the output is not lost. For example: `python main.py > results.csv`.

Run one instance of the consumer program on one VM.

Generate `latencies.csv` and `throughput.csv` using the program provided by the experiment designers team.

Fill this table with the appropriate links (There should be five CSV files in the producer CSV file folder):

| File Name | Link |
| --- | --- |
| producer CSV file Folder | |
| latencies.csv | |
| throughput.csv| |

Calculate the following data using Excel or a custom program by analyzing the data in latencies.csv and throughput.csv

| Metric | Value |
| --- | --- |
| Processing Latency Min | |
| Processing Latency Max | |
| Processing Latency Average | |
| Processing Latency Standard Deviation | |
| Processing Throughput Min | |
| Processing Throughput Max | |
| Processing Throughput Average | |
| Processing Throughput Standard Deviation | |

## 3 Producer VM's: 8 Instances - 3 Consumers VM's: 8 Instances

Run eight instances of your producer on three different machines (24 instances total).

Ensure you run your programs in such a way that the output is not lost. For example: `python main.py > results.csv`.

Run eight instances of your consumer program on three different machines as well.

Generate `latencies.csv` and `throughput.csv` using the program provided by the experiment designers team.

Fill this table with the appropriate links (There should be 24 CSV files in the producer CSV file folder):

| File Name | Link |
| --- | --- |
| producer CSV file folder | |
| latencies.csv | |
| throughput.csv| |

Calculate the following data using Excel or a custom program by analyzing the data in latencies.csv and throughput.csv

| Metric | Value |
| --- | --- |
| Processing Latency Min | |
| Processing Latency Max | |
| Processing Latency Average | |
| Processing Latency Standard Deviation | |
| Processing Throughput Min | |
| Processing Throughput Max | |
| Processing Throughput Average | |
| Processing Throughput Standard Deviation | |

## 4 Producer VM's: 25 Instances - 4 Consumer VM's: 25 Instances

Run 25 instances of the producer program on four different VM's (100 instances total).

Ensure you run your programs in such a way that the output is not lost. For example: `python main.py > results.csv`.

Run 25 instances of the consumer program on four different VM's (100 instances total).

Generate `latencies.csv` and `throughput.csv` using the program provided by the experiment designers team.

Fill this table with the appropriate links (Note: there should be 100 csv files in the producer csv file folder):

| File Name | Link |
| --- | --- |
| producer CSV file folder | |
| latencies.csv | |
| throughput.csv| |

Calculate the following data using Excel or a custom program by analyzing the data in latencies.csv and throughput.csv

| Metric | Value |
| --- | --- |
| Processing Latency Min | |
| Processing Latency Max | |
| Processing Latency Average | |
| Processing Latency Standard Deviation | |
| Processing Throughput Min | |
| Processing Throughput Max | |
| Processing Throughput Average | |
| Processing Throughput Standard Deviation | |
