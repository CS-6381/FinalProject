# Base Experiment

The goal of this experiment is to understand when the technology is viable to use.

## Compatibility

Here we wish to understand where the tech is easily used

### Basic Information

- How many individual actors can connect to this system at one time?
  - Configurable (per user, per ip address, or per user ip address)
- What license does it operate under?
  - Apache License, Version 2.0
- How much must be paid to use this technology?
  - Open Source
- Does it have explicit enterprise support?
  - No

|                           | HDPS (Hadoop Distributed File System)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Website(s)**            | (1) location for all documentation [http://hadoop.apache.org/docs/current/](http://hadoop.apache.org/docs/current/) <br/> (2) GitHub repository for IPSF Desktop [https://hadoop.apache.org/releases.html](https://hadoop.apache.org/releases.html)                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **Overview Basics**       | Distributed File System                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **Implementation Basics** | Quick Start [https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-common/SingleCluster.html](https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-common/SingleCluster.html) <br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **Use Cases**             | (1) Finance Sector: risk modelling. <br/> (2) Healthcare Sector: traking of large scale health index and metrics for curing diseases, reducing medical cost, predicting and managing epidemics and maintaining the quality of human life. <br/> (3) Telecom Industry: saving very large number of records frequently, for example, 30 Terabytes per month. <br/> (4) Retail Sector: Any large scale retailer doing transactional data analysis needs to put together massive quantities of Point of Sale transaction data coming from various data sources, with an objective of predicting demand, increasing profit and creating targeted marketing and promotional campaigns. <br/> (5) Building Recommendation System. <br/> |
| **Features**              | (1) Scalability. <br/> (2) Fault Tolerance. <br/> (3) High Availability. <br/> (4) Distributed Storage. <br/> (5) Data Reliability. <br/> (6) Replication. <br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **Scalability**           | Highly Scalable                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **Goals**                 | (1) Fast recovery from hardware failures. Because one HDFS instance may consist of thousands of servers, failure of at least one server is inevitable. <br/> (2) Access to streaming data. <br/> (3) Accommodation of large data sets. <br/> (4) Portability. <br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

### Operating Systems

| Operating System      | Yes/No | Link to steps                                                                                         | Average Install Time | Number of Manual Steps to Install |
| --------------------- | ------ | ----------------------------------------------------------------------------------------------------- | -------------------- | --------------------------------- |
| Ububtu 18.04          | Yes    | https://phoenixnap.com/kb/install-hadoop-ubuntu                                                       |                      |
| Ububtu 20.04          | Yes    | https://phoenixnap.com/kb/install-hadoop-ubuntu                                                       |                      |
| Windows 7             | Yes    | https://www.youtube.com/watch?v=MKjHncfqMTk                                                           |                      |
| Windows 10            | Yes    | https://towardsdatascience.com/installing-hadoop-3-2-1-single-node-cluster-on-windows-10-ac258dd48aef |                      |
| Mac                   | Yes    | https://towardsdatascience.com/installing-hadoop-on-a-mac-ec01c67b003c                                |                      |
| Docker (Windows)      | Yes    | https://clubhouse.io/developer-how-to/how-to-set-up-a-hadoop-cluster-in-docker/                       |                      |
| Docker (Ububtu 20.04) | Yes    | https://clubhouse.io/developer-how-to/how-to-set-up-a-hadoop-cluster-in-docker/                       |                      |
| Docker (Mac)          | Yes    | https://clubhouse.io/developer-how-to/how-to-set-up-a-hadoop-cluster-in-docker/                       |                      |
| Raspian               | Yes    | https://dev.to/awwsmm/building-a-raspberry-pi-hadoop-spark-cluster-8b2                                |                      |
| Android               | No     |                                                                                                       |                      |
| iOS                   | No     |                                                                                                       |                      |

### Hardware Architectures

| CPU Family                    | Yes/No | Known Limitations |
| ----------------------------- | ------ | ----------------- |
| ARM                           | Yes    |
| INTEL                         | Yes    |
| AMD                           | Yes    |
| Embedded (Eiger, Aruix, etc.) |        |

### Hardware Needs

Create this table for all OS and CPU combinations tested

#### EX: OS_A on CPU_B

<--MAP THIS TO THE EXPERIMENTS COMPLETED FOR YOUR TECHNOLOGY-->
||CPU|RAM|Hard Disk Memory|
|--|--|--|--|
|Idle||||
|Max Observed Under Load A||||
|Average Observed Under Load A||||
|Max Observed Under Load B||||
|Average Observed Under Load B||||

### Language Support

Are there commercially available libraries for the following languages?

If you are looking for packages from different programming languages to connect to HDFS, here are the list. If you want to extend Hadoop's internal components, you have to use Java because that's what Hadoop is written in. If you want to leverage Hadoop's machine learning algorithms, it would be best to run Spark on top of Hadoop and write programs in Scala or Python.

| Programming Language | Yes/No | Pacakge(s)                                                                          |
| -------------------- | ------ | ----------------------------------------------------------------------------------- |
| Python               | Yes    | hdfs3, HdfsCLI, H2O, hadoop, pydoop.hdfs, hdfs                                      |
| JavaScript           | Yes    | webhdfs                                                                             |
| C                    | Yes    | https://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-hdfs/LibHdfs.html |
| C++                  |        |
| C#                   | Yes    | https://www.nuget.org/packages/Microsoft.Phoenix.Client/                            |
| Objective-C          |        |
| Java                 | Yes    | https://hadoop.apache.org/docs/stable/api/index.html                                |
| Kotlin               | Yes    |
| Swift                |        |
| Go                   |        |
| Ruby                 | Yes    | ruby-hdfs                                                                           |
| Powershell           |        |
| Perl                 |        |
| Rust                 | Yes    | https://hyunsik.github.io/hdfs-rs/hdfs/index.html                                   |
| Elixr                |        |
