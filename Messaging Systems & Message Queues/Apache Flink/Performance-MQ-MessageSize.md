# Performance Experiment - MQ - Message Size

The goal of this experiment is to benchmark how this technology performs when hardware resources are plentiful and the size of messages varies.

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

### Message Size

- This test will run in 5 different modes with varying message size.
- The program should perform an ETL operation on a file consisting of 1,000 repetitions of the prescribed messages and then terminate after placing the result in another location on the file system.

Link to program usage here:

[Instructions for Running Flink program](./README.md)

### Consumer Program

- There is no consumer program because Flink is not an messaging queue
- Flink can interact with messaging queues or datastores to transform and/or analyze data and then place the result on another queue or into a datastore 

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

[Data Processor](../../DesignOfExperiments/mq-data-processor/main.py)

## Hardware Configuration

Each test should be ran using Ubuntu 20.04 (CC-Ubuntu20.04) chameleon cloud VM’s with 8 CPU and 16 GB of RAM (m1.xlarge). If these hardware specs aren’t attainable, use the nearest available and document the configuration.

# Experiment Configurations

These are the configurations your program should be ran in. Although it is not shown, there should be a separate machine instance for the broker.

| Producer Machines | Producer Instances | Consumer Machines | Consumer Instances | Message Size |
| ----------------- | ------------------ | ----------------- | ------------------ | ------------ |
| 1                 | 1                  | 1                 | 1                  | tiny         |
| 1                 | 1                  | 1                 | 1                  | small        |
| 1                 | 1                  | 1                 | 1                  | medium       |
| 1                 | 1                  | 1                 | 1                  | large        |
| 1                 | 1                  | 1                 | 1                  | x-large      |

If possible, implement these configurations with redundancy enabled and document the configuration.

## Redundancy Implementation Details

- Redundancy was not included in testing for Flink 

## 1 Producer - 1 Consumer - Tiny Message Size

- Running one instance of data transformation program on one VM. Created a file that contains the content from [tiny](../../DesignOfExperiments/messages/tiny.txt), repeated 1000 times.
  - The resulting file is 45 KB and has 1000 lines
- This is done because Flink is meant to be a big data processor that can take data from a live stream or a batch to convert the data and/or run analytics
- Output is in the for os a `perf_n.csv`, where `n` varies from 0 - 9 - experiment was run 10 times
- There is no consumer program due to the fact that Flink is an ETL (extract, transform, load) tool. Instead the tests show how performant Flink is for moving data from one place on the file system to another
- The experiment is based on moving data locally on the host machine to isolate the pure performance of the tool for ETL processing without considering getting data from a queue or a datastore
- The `latencies.csv` represents how long it took for the entire ETL process, i.e.: grabbing data from the file system and moving it to another location within the same file system
- The `throughput.csv` does not very well represent any meaningful data since Flink is not a messaging tool and the only timestamps produced by the data transformation program are from the very beginning and end of the program

  | File Name      | Link |
  | -------------- | ---- |
  | producer.csv   | [record of time to perform entire data transformation](./Results/perf/tiny/perf_0.csv) |
  | latencies.csv  | [latencies](./Results/perf/tiny/latencies.csv) |
  | throughput.csv | [could not find a way to attach clock time per piece of data transformed](./Results/perf/tiny/throughput.csv) |

- Calculated data using Excel for `latencies.csv`

  | Metric                                   | Value |
  | ---------------------------------------- | ----- |
  | Processing Latency Min                   |   2269 ms   |
  | Processing Latency Max                   |   2558 ms   |
  | Processing Latency Average               |   2427.50 ms |
  | Processing Latency Standard Deviation    |   106 ms  |
  | Processing Throughput Min                | data not valuable |
  | Processing Throughput Max                | data not valuable |
  | Processing Throughput Average            | data not valuable |
  | Processing Throughput Standard Deviation | data not valuable |

## 1 Producer - 1 Consumer - Small Message Size

- Running one instance of data transformation program on one VM. Created a file that contains the content from [small](../../DesignOfExperiments/messages/small.txt), repeated 1000 times.
  - The resulting file is 299 KB and has 1000 lines
- This is done because Flink is meant to be a big data processor that can take data from a live stream or a batch to convert the data and/or run analytics
- Output is in the for os a `perf_n.csv`, where `n` varies from 0 - 9 - experiment was run 10 times
- There is no consumer program due to the fact that Flink is an ETL (extract, transform, load) tool. Instead the tests show how performant Flink is for moving data from one place on the file system to another
- The experiment is based on moving data locally on the host machine to isolate the pure performance of the tool for ETL processing without considering getting data from a queue or a datastore
- The `latencies.csv` represents how long it took for the entire ETL process, i.e.: grabbing data from the file system and moving it to another location within the same file system
- The `throughput.csv` does not very well represent any meaningful data since Flink is not a messaging tool and the only timestamps produced by the data transformation program are from the very beginning and end of the program

  | File Name      | Link |
  | -------------- | ---- |
  | producer.csv   | [record of time to perform entire data transformation](./Results/perf/small/perf_0.csv) |
  | latencies.csv  | [latencies](./Results/perf/small/latencies.csv) |
  | throughput.csv | [could not find a way to attach clock time per piece of data transformed](./Results/perf/small/throughput.csv) |

- Calculated data using Excel for `latencies.csv`

  | Metric                                   | Value |
  | ---------------------------------------- | ----- |
  | Processing Latency Min                   |   2355 ms   |
  | Processing Latency Max                   |   2660 ms   |
  | Processing Latency Average               |  2477.90 ms |
  | Processing Latency Standard Deviation    |  101.44 ms  |
  | Processing Throughput Min                | data not valuable |
  | Processing Throughput Max                | data not valuable |
  | Processing Throughput Average            | data not valuable |
  | Processing Throughput Standard Deviation | data not valuable |

## 1 Producer - 1 Consumer - Medium Message Size

- Running one instance of data transformation program on one VM. Created a file that contains the content from [medium](../../DesignOfExperiments/messages/medium.txt), repeated 1000 times.
  - The resulting file is 6866 KB and has 47,000 lines
- This is done because Flink is meant to be a big data processor that can take data from a live stream or a batch to convert the data and/or run analytics
- Output is in the for os a `perf_n.csv`, where `n` varies from 0 - 9 - experiment was run 10 times
- There is no consumer program due to the fact that Flink is an ETL (extract, transform, load) tool. Instead the tests show how performant Flink is for moving data from one place on the file system to another
- The experiment is based on moving data locally on the host machine to isolate the pure performance of the tool for ETL processing without considering getting data from a queue or a datastore
- The `latencies.csv` represents how long it took for the entire ETL process, i.e.: grabbing data from the file system and moving it to another location within the same file system
- The `throughput.csv` does not very well represent any meaningful data since Flink is not a messaging tool and the only timestamps produced by the data transformation program are from the very beginning and end of the program

  | File Name      | Link |
  | -------------- | ---- |
  | producer.csv   | [record of time to perform entire data transformation](./Results/perf/medium/perf_0.csv) |
  | latencies.csv  | [latencies](./Results/perf/medium/latencies.csv) |
  | throughput.csv | [could not find a way to attach clock time per piece of data transformed](./Results/perf/medium/throughput.csv) |

- Calculated data using Excel for `latencies.csv`
  
  | Metric                                   | Value |
  | ---------------------------------------- | ----- |
  | Processing Latency Min                   |   2695 ms   |
  | Processing Latency Max                   |   2944 ms   |
  | Processing Latency Average               |  2813.20 ms |
  | Processing Latency Standard Deviation    |   86.93 ms  |
  | Processing Throughput Min                | data not valuable |
  | Processing Throughput Max                | data not valuable |
  | Processing Throughput Average            | data not valuable |
  | Processing Throughput Standard Deviation | data not valuable |

## 1 Producer - 1 Consumer - Large Message Size

- Running one instance of data transformation program on one VM. Created a file that contains the content from [large](../../DesignOfExperiments/messages/large.txt), repeated 1000 times.
  - The resulting file is 160.548 MB and has 2,934,000 lines
- This is done because Flink is meant to be a big data processor that can take data from a live stream or a batch to convert the data and/or run analytics
- Output is in the for os a `perf_n.csv`, where `n` varies from 0 - 9 - experiment was run 10 times
- There is no consumer program due to the fact that Flink is an ETL (extract, transform, load) tool. Instead the tests show how performant Flink is for moving data from one place on the file system to another
- The experiment is based on moving data locally on the host machine to isolate the pure performance of the tool for ETL processing without considering getting data from a queue or a datastore
- The `latencies.csv` represents how long it took for the entire ETL process, i.e.: grabbing data from the file system and moving it to another location within the same file system
- The `throughput.csv` does not very well represent any meaningful data since Flink is not a messaging tool and the only timestamps produced by the data transformation program are from the very beginning and end of the program

| File Name      | Link |
| -------------- | ---- |
| producer.csv   | [record of time to perform entire data transformation](./Results/perf/large/perf_0.csv) |
| latencies.csv  | [latencies](./Results/perf/large/latencies.csv) |
| throughput.csv | [could not find a way to attach clock time per piece of data transformed](./Results/perf/large/throughput.csv) |

- Calculated data using Excel for `latencies.csv`

| Metric                                   | Value |
| ---------------------------------------- | ----- |
| Processing Latency Min                   |   14232 ms   |
| Processing Latency Max                   |   14891 ms   |
| Processing Latency Average               |  14598.60 ms |
| Processing Latency Standard Deviation    |  211.67 ms   |
| Processing Throughput Min                | data not valuable |
| Processing Throughput Max                | data not valuable |
| Processing Throughput Average            | data not valuable |
| Processing Throughput Standard Deviation | data not valuable |

## 1 Producer - 1 Consumer - X-Large Message Size

- Running one instance of data transformation program on one VM. Created a file that contains the content from [xlarge](../../DesignOfExperiments/messages/xlarge.txt), repeated 1000 times.
  - The resulting file is 785.06 MB and has 14,578,000 lines
- This is done because Flink is meant to be a big data processor that can take data from a live stream or a batch to convert the data and/or run analytics
- Output is in the for os a `perf_n.csv`, where `n` varies from 0 - 9 - experiment was run 10 times
- There is no consumer program due to the fact that Flink is an ETL (extract, transform, load) tool. Instead the tests show how performant Flink is for moving data from one place on the file system to another
- The experiment is based on moving data locally on the host machine to isolate the pure performance of the tool for ETL processing without considering getting data from a queue or a datastore
- The `latencies.csv` represents how long it took for the entire ETL process, i.e.: grabbing data from the file system and moving it to another location within the same file system
- The `throughput.csv` does not very well represent any meaningful data since Flink is not a messaging tool and the only timestamps produced by the data transformation program are from the very beginning and end of the program

| File Name      | Link |
| -------------- | ---- |
| producer.csv   | [record of time to perform entire data transformation](./Results/perf/large/perf_0.csv) |
| latencies.csv  | [latencies](./Results/perf/large/latencies.csv) |
| throughput.csv | [could not find a way to attach clock time per piece of data transformed](./Results/perf/large/throughput.csv) |

- Calculated data using Excel for `latencies.csv`

| Metric                                   | Value |
| ---------------------------------------- | ----- |
| Processing Latency Min                   |   58719 ms   |
| Processing Latency Max                   |   61981 ms   |
| Processing Latency Average               | 60449.80 ms  |
| Processing Latency Standard Deviation    |  1004.41 ms  |
| Processing Throughput Min                | data not valuable |
| Processing Throughput Max                | data not valuable |
| Processing Throughput Average            | data not valuable |
| Processing Throughput Standard Deviation | data not valuable |
