# AWS SNS Performance Experiment - MQ - Message Size

Notes: Given the message size limit for AWS SNS, the only test that couldn't be run on this system without deviating from the test parameters was the xlarge message tests.

Data: The data captured is automatically output by AWS Cloudwatch and provides all necessary Pub/Sub metrics for these experiments. By analyzing the output csv in excel, as well, as custom scripts, the resulting data is calculated using:
* AWS SNS Timestamps
* AWS SNS Dwell Time = the time between the publish timestamp and Amazon SNS endpoint timestamp
* Timestamps on our 'START' events on the Lambda containers

Infrastructure used:

Producer script (Ubuntu 20.04) -> AWS SNS topic -> AWX Lambda as Consumer (deployed to AWS Linux 2 container)

## 1 Producer - 1 Consumer - Tiny Message Size

| Metric                                   | Value |
| ---------------------------------------- | ----- |
| Processing Latency Min                   |   4965    |
| Processing Latency Max                   |    21105   |
| Processing Latency Average               |    1200  |
| Processing Latency Standard Deviation    |    1594   |
| Send Time Min                            |    26   |
| Send Time Max                            |    341   |
| Send Time Average                        |    61   |
| Send Time Standard Deviation             |     30  |
| Processing Throughput Min                |    1   |
| Processing Throughput Max                |    21   |
| Processing Throughput Average            |    10   |
| Processing Throughput Standard Deviation |    5   |
| Send Throughput Min                      |    4965   |
| Send Throughput Max                      |    21105   |
| Send Throughput Average                  |    12190   |
| Send Throughput Standard Deviation       |     2511  |

## 1 Producer - 1 Consumer - Small Message Size


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

## 1 Producer - 1 Consumer - Medium Message Size


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

## 1 Producer - 1 Consumer - Large Message Size


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

## 1 Producer - 1 Consumer - X-Large Message Size

**This test is not available due to message size constraints mentioned in the header notes.