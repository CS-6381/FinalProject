# AWS SNS
Author: Rick Tesmond\
CS 6381

Link: https://aws.amazon.com/sns/

## Technology Overview
Amazon Web Service's answer to a pub/sub messaging system.

"Amazon Simple Notification Service (Amazon SNS) is a fully managed messaging service for both application-to-application (A2A)."

Features:
* push-based pub/sub
* many-to-many
* plugs in to many AWS services (can be incorporated with SQS, Lambda, Kinesis for parallel processing)
   * this flexibility will allow me to run our tests across different solutions if the need be... like adding in queuing for testing consistency or DataWatch to help analyze results.
    
* Two different Topic type options:
   * Standard Topic: nearly unlimited message thoroughput, best effort ordering, and stable support for 100,000 Standard topics and each topic supports up to 12.5M subscriptions.
    * FIFO Topics (First In First Out): support up to 300 messages per second or 10 MB per second per FIFO topic, and can support 1000 FIFO topics and each topic supports up to 100 subscriptions.
    

Other notes - the first 1M messages are free, but the subsequent messages do come with a cost... though it's a small cost per million.
