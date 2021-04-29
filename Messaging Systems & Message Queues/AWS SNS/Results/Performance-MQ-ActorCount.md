# Performance Experiment - MQ - Actor Count

Notes: Because the subscribers are singular containerized AWS Lambda functions, I did not have the flexibility to have multiple instances on a single VM. The testing was therefore restricted to the VM test cases rather than the instance test cases. The producers still have  the flexibility to match the requirements; however, I decided it would be more consistent to match the producer requirements to what we could make available on the subscriber system.  

Data: Output stored under 'test_results/actor_tests/'. The data captured is automatically output by AWS Cloudwatch and provides all necessary Pub/Sub metrics for these experiments. By analyzing the output csv in excel, as well, as custom scripts, the resulting data is calculated using:
* AWS SNS Timestamps
* AWS SNS Dwell Time = the time between the publish timestamp and Amazon SNS endpoint timestamp
* Timestamps on our 'START' events on the Lambda containers

Infrastructure used:

Producer script (Ubuntu 20.04) -> AWS SNS topic -> AWX Lambda as Consumer (deployed to AWS Linux 2 container)


## 1 Producer - 1 Consumer


| Metric | Value |
| --- | --- |
| Processing Latency Min | 2247|
| Processing Latency Max |20753 |
| Processing Latency Average | 11887|
| Processing Latency Standard Deviation | 1545|
| Send Time Min | 26|
| Send Time Max | 411|
| Send Time Average |71 |
| Send Time Standard Deviation |35 |
| Processing Throughput Min | 1|
| Processing Throughput Max | 22|
| Processing Throughput Average | 10|
| Processing Throughput Standard Deviation | 5|
| Send Throughput Min | 2247|
| Send Throughput Max | 20753|
| Send Throughput Average | 11764|
| Send Throughput Standard Deviation |2767 |


## 3 Producer VM's - 3 Consumers VM's

| Metric | Value |
| --- | --- |
| Processing Latency Min | 50243|
| Processing Latency Max | 131460|
| Processing Latency Average | 77232|
| Processing Latency Standard Deviation | 13708|
| Send Time Min | 22|
| Send Time Max |529 |
| Send Time Average | 57|
| Send Time Standard Deviation | 32|
| Processing Throughput Min |1 |
| Processing Throughput Max | 171|
| Processing Throughput Average | 51|
| Processing Throughput Standard Deviation | 42|
| Send Throughput Min | 50348|
| Send Throughput Max | 130789|
| Send Throughput Average | 77507|
| Send Throughput Standard Deviation | 16560|

## 4 Producer VM's - 4 Consumer VM's

| Metric | Value |
| --- | --- |
| Processing Latency Min | 18997|
| Processing Latency Max |79875 |
| Processing Latency Average |44850 |
| Processing Latency Standard Deviation | 17638|
| Send Time Min |20 |
| Send Time Max | 396|
| Send Time Average | 53|
| Send Time Standard Deviation | 31|
| Processing Throughput Min | 4|
| Processing Throughput Max | 257|
| Processing Throughput Average |145 |
| Processing Throughput Standard Deviation |67 |
| Send Throughput Min | 19606|
| Send Throughput Max | 76522|
| Send Throughput Average | 36625|
| Send Throughput Standard Deviation |17960 |