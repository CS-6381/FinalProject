# AWS SNS Performance Experiment - MQ - Message Size

Notes: Given the message size limit for AWS SNS, the only test that couldn't be run on this system without deviating from the test parameters was the xlarge message tests.

Infrastructure used:

Producer script (Ubuntu 20.04) -> AWS SNS topic -> AWX Lambda as Consumer (deployed to AWS Linux 2 container)

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