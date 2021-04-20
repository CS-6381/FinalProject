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


## 3 Producer VM's - 3 Consumers VM's

Run eight instances of your producer on three different machines (24 instances total).

Ensure you run your programs in such a way that the output is not lost. For example: `python main.py > results.csv`.

Run eight instances of your consumer program on three different machines as well.

Fill this table with the appropriate links:

| File Name | Link |
| --- | --- |
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

## 4 Producer VM's - 4 Consumer VM's

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