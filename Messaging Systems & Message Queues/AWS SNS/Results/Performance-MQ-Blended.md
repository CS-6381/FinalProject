# Performance Experiment - MQ - Actor Count and Message Size Blend


## Hardware Configuration

Each test should be ran using Ubuntu 18.04 chameleon cloud VM’s with 8 CPU and 32 GB of RAM. If these hardware specs aren’t attainable, use the nearest available and document the configuration.

# Experiment Configurations


| Producer Machines | Producer Instances | Consumer Machines | Consumer Instances | Message Size |
| ----------------- | ------------------ | ----------------- | ------------------ | ------------ |
| 1                 | 1                  | 1                 | 1                  | tiny         |
| 1                 | 1                  | 1                 | 5                  | small        |
| 1                 | 5                  | 1                 | 1                  | medium       |
| 3                 | 8                  | 3                 | 8                  | large        |
| 4                 | 25                 | 4                 | 25                 | x-large      |


## 1 Producer - 1 Consumer - Tiny Message Size


| Metric                                   | Value |
| ---------------------------------------- | ----- |
| Processing Latency Min                   |       |
| Processing Latency Max                   |       |
| Processing Latency Average               |       |
| Processing Latency Standard Deviation    |       |
| Send Time Min                            |       |
| Send Time Max                            |       |
| Send Time Average                        |       |
| Send Time Standard Deviation             |       |
| Processing Throughput Min                |       |
| Processing Throughput Max                |       |
| Processing Throughput Average            |       |
| Processing Throughput Standard Deviation |       |
| Send Throughput Min                      |       |
| Send Throughput Max                      |       |
| Send Throughput Average                  |       |
| Send Throughput Standard Deviation       |       |

## 1 Producer VM - 1 Consumer VM: 5 Instances - Small Message Size

Run one instance of your producer program on one VM. Configure your producer to always send the [small](./messages/small.txt) message.

Ensure you run your programs in such a way that the output is not lost. For example: `python main.py > results.csv`.

Run five consumer program instances on one VM.

Fill this table with the appropriate links:

| File Name      | Link |
| -------------- | ---- |
| producer1.csv  |      |
| consumer1.csv  |      |
| latencies.csv  |      |
| throughput.csv |      |

Calculate the following data using Excel or a custom program by analyzing the data in latencies.csv and throughput.csv

| Metric                                   | Value |
| ---------------------------------------- | ----- |
| Processing Latency Min                   |       |
| Processing Latency Max                   |       |
| Processing Latency Average               |       |
| Processing Latency Standard Deviation    |       |
| Send Time Min                            |       |
| Send Time Max                            |       |
| Send Time Average                        |       |
| Send Time Standard Deviation             |       |
| Processing Throughput Min                |       |
| Processing Throughput Max                |       |
| Processing Throughput Average            |       |
| Processing Throughput Standard Deviation |       |
| Send Throughput Min                      |       |
| Send Throughput Max                      |       |
| Send Throughput Average                  |       |
| Send Throughput Standard Deviation       |       |

## 1 Producer VM: 5 Instances - 1 Consumer VM: 1 Instance - Medium Message Size

Run five producer program instances on one VM. Configure the producers to always send the [medium](./messages/medium.txt) message.

Ensure you run your programs in such a way that the output is not lost. For example: `python main.py > results.csv`.

Run one instance of the consumer program on one VM.

Fill this table with the appropriate links:

| File Name      | Link |
| -------------- | ---- |
| producer1.csv  |      |
| consumer1.csv  |      |
| latencies.csv  |      |
| throughput.csv |      |

Calculate the following data using Excel or a custom program by analyzing the data in latencies.csv and throughput.csv

| Metric                                   | Value |
| ---------------------------------------- | ----- |
| Processing Latency Min                   |       |
| Processing Latency Max                   |       |
| Processing Latency Average               |       |
| Processing Latency Standard Deviation    |       |
| Send Time Min                            |       |
| Send Time Max                            |       |
| Send Time Average                        |       |
| Send Time Standard Deviation             |       |
| Processing Throughput Min                |       |
| Processing Throughput Max                |       |
| Processing Throughput Average            |       |
| Processing Throughput Standard Deviation |       |
| Send Throughput Min                      |       |
| Send Throughput Max                      |       |
| Send Throughput Average                  |       |
| Send Throughput Standard Deviation       |       |

## 3 Producer VM's: 8 Instances - 3 Consumers VM's: 8 Instances - Large Message Size

Run eight instances of your producer on three different machines (24 instances total). Configure your producers to always send the [large](./messages/large.txt) message.

Ensure you run your programs in such a way that the output is not lost. For example: `python main.py > results.csv`.

Run eight instances of your consumer program on three different machines as well.

Fill this table with the appropriate links:

| File Name      | Link |
| -------------- | ---- |
| producer1.csv  |      |
| producer2.csv  |      |
| producer3.csv  |      |
| consumer1.csv  |      |
| consumer2.csv  |      |
| consumer3.csv  |      |
| latencies.csv  |      |
| throughput.csv |      |

Calculate the following data using Excel or a custom program by analyzing the data in latencies.csv and throughput.csv

| Metric                                   | Value |
| ---------------------------------------- | ----- |
| Processing Latency Min                   |       |
| Processing Latency Max                   |       |
| Processing Latency Average               |       |
| Processing Latency Standard Deviation    |       |
| Send Time Min                            |       |
| Send Time Max                            |       |
| Send Time Average                        |       |
| Send Time Standard Deviation             |       |
| Processing Throughput Min                |       |
| Processing Throughput Max                |       |
| Processing Throughput Average            |       |
| Processing Throughput Standard Deviation |       |
| Send Throughput Min                      |       |
| Send Throughput Max                      |       |
| Send Throughput Average                  |       |
| Send Throughput Standard Deviation       |       |

## 4 Producer VM's: 25 Threads - 4 Consumer VM's: 25 Threads - X-Large Message Size

Run 25 instances of the producer program on four different VM's (100 instances total). Configure your producers to always send the [x-large](./messages/xlarge.txt) message.

Ensure you run your programs in such a way that the output is not lost. For example: `python main.py > results.csv`.

Run 25 instances of the consumer program on four different VM's (100 instances total).

Fill this table with the appropriate links:

| File Name      | Link |
| -------------- | ---- |
| producer1.csv  |      |
| producer2.csv  |      |
| producer3.csv  |      |
| producer4.csv  |      |
| consumer1.csv  |      |
| consumer2.csv  |      |
| consumer3.csv  |      |
| consumer4.csv  |      |
| latencies.csv  |      |
| throughput.csv |      |

Calculate the following data using Excel or a custom program by analyzing the data in latencies.csv and throughput.csv

| Metric                                   | Value |
| ---------------------------------------- | ----- |
| Processing Latency Min                   |       |
| Processing Latency Max                   |       |
| Processing Latency Average               |       |
| Processing Latency Standard Deviation    |       |
| Send Time Min                            |       |
| Send Time Max                            |       |
| Send Time Average                        |       |
| Send Time Standard Deviation             |       |
| Processing Throughput Min                |       |
| Processing Throughput Max                |       |
| Processing Throughput Average            |       |
| Processing Throughput Standard Deviation |       |
| Send Throughput Min                      |       |
| Send Throughput Max                      |       |
| Send Throughput Average                  |       |
| Send Throughput Standard Deviation       |       |
