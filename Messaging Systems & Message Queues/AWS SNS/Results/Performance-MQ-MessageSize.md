# AWS SNS Performance Experiment - MQ - Message Size

Notes: Given the message size limit for AWS SNS, the only test that couldn't be run on this system without deviating from the test parameters was the xlarge message tests.

Data: Output stored under '/test_results/size_tests/'. The data captured is automatically output by AWS Cloudwatch and provides all necessary Pub/Sub metrics for these experiments. By analyzing the output csv in excel, as well, as custom scripts, the resulting data is calculated using:
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
| Processing Latency Average               |    12000  |
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
| Processing Latency Min                   |    2502   |
| Processing Latency Max                   |   19352    |
| Processing Latency Average               |  12080     |
| Processing Latency Standard Deviation    |  1543     |
| Send Time Min                            |    27   |
| Send Time Max                            |    343   |
| Send Time Average                        |    63   |
| Send Time Standard Deviation             |    30   |
| Processing Throughput Min                |   1    |
| Processing Throughput Max                |   21    |
| Processing Throughput Average            |    10   |
| Processing Throughput Standard Deviation |    5   |
| Send Throughput Min                      |   2831    |
| Send Throughput Max                      |    19352   |
| Send Throughput Average                  |    11926   |
| Send Throughput Standard Deviation       |     2492  |

## 1 Producer - 1 Consumer - Medium Message Size


| Metric                                   | Value |
| ---------------------------------------- | ----- |
| Processing Latency Min                   |    8408   |
| Processing Latency Max                   |     22451  |
| Processing Latency Average               |    16691   |
| Processing Latency Standard Deviation    |     3255  |
| Send Time Min                            |    29   |
| Send Time Max                            |    386   |
| Send Time Average                        |    69   |
| Send Time Standard Deviation             |     31  |
| Processing Throughput Min                |   1    |
| Processing Throughput Max                |   19    |
| Processing Throughput Average            |     9  |
| Processing Throughput Standard Deviation |    5   |
| Send Throughput Min                      |    8491   |
| Send Throughput Max                      |    22181   |
| Send Throughput Average                  |      16479 |
| Send Throughput Standard Deviation       |    3433   |

## 1 Producer - 1 Consumer - Large Message Size


| Metric                                   | Value |
| ---------------------------------------- | ----- |
| Processing Latency Min                   |    7763   |
| Processing Latency Max                   |     22451  |
| Processing Latency Average               |     12212  |
| Processing Latency Standard Deviation    |     1640  |
| Send Time Min                            |    132   |
| Send Time Max                            |     534  |
| Send Time Average                        |     190  |
| Send Time Standard Deviation             |      45 |
| Processing Throughput Min                |    1   |
| Processing Throughput Max                |    10   |
| Processing Throughput Average            |    4   |
| Processing Throughput Standard Deviation |    2   |
| Send Throughput Min                      |    8905   |
| Send Throughput Max                      |    22451   |
| Send Throughput Average                  |    12351   |
| Send Throughput Standard Deviation       |    1931   |

## 1 Producer - 1 Consumer - X-Large Message Size

**This test is not available due to message size constraints mentioned in the header notes.