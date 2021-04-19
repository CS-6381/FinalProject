# Base Experiment
The goal of this experiment is to understand when the technology is viable to use. 

## Compatibility 
Here we wish to understand where the tech is easily used

### Apache Pulsar
Apache Pulsar is a cloud-native, distributed messaging and streaming platform originally created at Yahoo. It is now a top-level Apache Software Foundation Project.

Here you can also find a desciption of the features Pulsar to compared with other Messaging Systems and Message Queues.

|Feature|Description|
|--|--|
Messaging|Pulsar is built on the publish-subscribe pattern|
Geo Replication| Support for multiple clusters in a Pulsar instance. This enables messages to be produced and consumed in different geolocations|
Multi Tenancy|Tenants (use groups) can be spread across clusters, and supports isolation, authentication, authorization, and quotas|
Persistent Storage|Guaranteed message delivery for applications. This results in non-acknowledged messages being sotred in a durable manner until they can be delivered to and acknowledged by consumers. The storage is Based on Apache BookKeeper and supports IO-level isolation between write and read operations. Pulsar also supports non-persistent storage|
Horizontally Scalable|Clusters in an instance can replicate data amongst themselves|
Low latency with durability| Low publish latency (<5ms) at scale with strong durability guarantees|

[Apache Pulsar](https://pulsar.apache.org/en/)


### Basic Information
- How many individual actors can connect to this system at one time? 
- What license does it operate under?
    -  Apache License, version 2.0
- How much must be paid to use this technology?
    - One time fee?
    - Monthly?
    - Yearly?
        - Open Source Version: Free
        - [StreamNative] (https://streamnative.io/) is a recently launched company that provides a cloud based version of Apache Pulsar. They have free and paid tiers.
- Does it have explicit enterprise support? 
    -No

# Operating Systems
|Operating System|Yes/No|Link to steps|Average Install Time| Number of Manual Steps to Install|
|--|--|--|--|--|
Ububtu 18.04|Yes|https://pulsar.apache.org/docs/v1.21.0-incubating/deployment/instance|
Ububtu 20.04|Yes|https://pulsar.apache.org/docs/v1.21.0-incubating/deployment/instance||
Windows 7|No||
Windows 10|No|||
Mac|Yes|https://pulsar.apache.org/docs/v1.21.0-incubating/deployment/instance|
Docker (Windows)|Yes|https://pulsar.apache.org/docs/en/standalone-docker||
Docker (Ububtu 18.04)|Yes|https://pulsar.apache.org/docs/en/standalone-docker/||
Docker (Mac)|Yes|https://pulsar.apache.org/docs/en/standalone-docker/||
Raspian||||
Android||||
iOS||||
Kubernetes|Yes|https://pulsar.apache.org/docs/v1.21.0-incubating/deployment/Kubernetes/||


### Hardware Architectures 
Can it run on these CPUs?

|CPU Family|Yes/No|Known Limitations|
|--|--|--|
ARM||
INTEL||
AMD||
Embedded (Eiger, Aruix, etc.)||

### Hardware Needs 
Create this table for all OS and CPU combinations tested 

#### EX: OS_A on CPU_B
||CPU|RAM|Hard Disk Memory|
|--|--|--|--|
|Idle||||
|Max Observed Under Load A||||
|Average Observed Under Load A||||
|Max Observed Under Load B||||
|Average Observed Under Load B||||


## Language Support
Are there commercially available libraries for the following languages?

|Programming Language|Yes/No|Link(s)|
|--|--|--|
Python|Yes|https://pulsar.apache.org/docs/en/client-libraries-python|
JavaScript|Yes|https://pulsar.apache.org/docs/en/client-libraries-node|
C|||
C++|Yes|https://pulsar.apache.org/docs/en/client-libraries-cpp|
C#|Yes|https://pulsar.apache.org/docs/en/client-libraries-dotnet|
Objective-C|||
Java|Yes|https://pulsar.apache.org/docs/en/client-libraries-java|
Kotlin||
Swift|||
Go|Yes|https://pulsar.apache.org/docs/en/client-libraries-go|
Ruby|||
Powershell||
Perl||