# Performance Experiment - MQ - Actor Count and Message Size Blend


## Hardware Configuration

Each test should be ran using Ubuntu 18.04 chameleon cloud VM’s with 8 CPU and 32 GB of RAM. If these hardware specs aren’t attainable, use the nearest available and document the configuration.


## 1 Producer - 1 Consumer - Tiny Message Size


| Metric                                   | Value |
| ---------------------------------------- | ----- |
| Processing Latency Min                   |    4965   |
| Processing Latency Max                   |    21105   |
| Processing Latency Average               |     12000  |
| Processing Latency Standard Deviation    |     1594  |
| Send Time Min                            |  26     |
| Send Time Max                            |   341    |
| Send Time Average                        |    61   |
| Send Time Standard Deviation             |     30  |
| Processing Throughput Min                |   1    |
| Processing Throughput Max                |    21   |
| Processing Throughput Average            |     10  |
| Processing Throughput Standard Deviation |      5 |
| Send Throughput Min                      | 5011      |
| Send Throughput Max                      |  21105     |
| Send Throughput Average                  |   12190    |
| Send Throughput Standard Deviation       |    2511   |

## 1 Producer VM - 1 Consumer VM - Small Message Size


| Metric                                   | Value |
| ---------------------------------------- | ----- |
| Processing Latency Min                   |  90     |
| Processing Latency Max                   |  107147     |
| Processing Latency Average               |   43661    |
| Processing Latency Standard Deviation    |    27231   |
| Send Time Min                            |   24    |
| Send Time Max                            |    482   |
| Send Time Average                        |   64    |
| Send Time Standard Deviation             |     33  |
| Processing Throughput Min                |  1     |
| Processing Throughput Max                |  21     |
| Processing Throughput Average            |   20    |
| Processing Throughput Standard Deviation |     5  |
| Send Throughput Min                      |  620     |
| Send Throughput Max                      |   107147    |
| Send Throughput Average                  |   52409    |
| Send Throughput Standard Deviation       |    29814   |

## 1 Producer VM - 1 Consumer VM - Medium Message Size


| Metric                                   | Value |
| ---------------------------------------- | ----- |
| Processing Latency Min                   |  2423     |
| Processing Latency Max                   |   20973    |
| Processing Latency Average               |   11558    |
| Processing Latency Standard Deviation    |   1781    |
| Send Time Min                            |     25  |
| Send Time Max                            |     320  |
| Send Time Average                        |    65   |
| Send Time Standard Deviation             |    29   |
| Processing Throughput Min                |  1     |
| Processing Throughput Max                |   17    |
| Processing Throughput Average            |     9  |
| Processing Throughput Standard Deviation |      4 |
| Send Throughput Min                      | 2423      |
| Send Throughput Max                      | 20802      |
| Send Throughput Average                  |  11588     |
| Send Throughput Standard Deviation       |   2758    |

## 3 Producer VM's - 3 Consumers VM's - Large Message Size

| Metric                                   | Value |
| ---------------------------------------- | ----- |
| Processing Latency Min                   |   20899    |
| Processing Latency Max                   |    297548   |
| Processing Latency Average               |   155978    |
| Processing Latency Standard Deviation    |  89530     |
| Send Time Min                            |  122     |
| Send Time Max                            |   1826    |
| Send Time Average                        |    185   |
| Send Time Standard Deviation             |     52  |
| Processing Throughput Min                |   1    |
| Processing Throughput Max                |   57    |
| Processing Throughput Average            |    24   |
| Processing Throughput Standard Deviation |    12   |
| Send Throughput Min                      |  21241     |
| Send Throughput Max                      |  297173     |
| Send Throughput Average                  |  137888     |
| Send Throughput Standard Deviation       |  92675     |

## 4 Producer VM's: 25 Threads - 4 Consumer VM's: 25 Threads - X-Large Message Size

**This test could not be complete due to the message size limit in basic AWS SNS.
