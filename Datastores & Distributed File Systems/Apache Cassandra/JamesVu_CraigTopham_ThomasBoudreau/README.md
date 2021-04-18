# Base Experiment
The goal of this experiment is to understand when the technology is viable to use. 

# Experiment Hardware Configuration
Each test should be ran using Ubuntu 20.04 chameleon cloud VM’s with 8 CPU and 32 GB of RAM. If these hardware specs aren’t attainable, use the nearest available and document the configuration. Please also use internal IP addresses for all communication to simulate a more consistent network topology with less traffic.

## Compatibility 

### Qualitative 

**TODO**

For data stores, TBD.

### Basic Information
- How many individual actors can connect to this system at one time?
    - [Unlimited, but configurable.](https://cassandra.apache.org/doc/latest/configuration/cassandra_config_file.html#native-transport-max-concurrent-connections)
    - In our experiment trials, ~ 5 instances.
- What license does it operate under?
    - Apache License 2.0 (https://en.wikipedia.org/wiki/Apache_Cassandra)
- How much must be paid to use this technology?
    - Nothing, it is open-source. (https://en.wikipedia.org/wiki/Apache_Cassandra)
- Does it have explicit enterprise support? 
    - Yes, but only from [third-parties.](https://cassandra.apache.org/third-party/)
    - DataStax uses Apache Cassandra and offers support (https://www.datastax.com/services/support).

### Operating Systems
Can it be installed on the below?

**Cassandra runs on Java, this means that it can theoretically run on any device with JVM support. However, the following table has been completed based on available documentation. (Including third-party documentation)**

|Operating System|Yes/No|Link to steps|Average Install Time| Number of Manual Steps to Install|
|--|--|--|--|--|
Ubuntu 18.04|Yes|[Install](https://cassandra.apache.org/doc/latest/getting_started/installing.html), https://www.youtube.com/watch?v=pGhkX5z_vW8|~10 min.|~5
Ubuntu 20.04|Yes|[Install](https://cassandra.apache.org/doc/latest/getting_started/installing.html)||
Windows 7|Yes|[Install](https://www.datastax.com/blog/getting-started-apache-cassandra-windows-easy-way), https://www.datastax.com/blog/getting-started-apache-cassandra-windows-easy-way||
Windows 10|Yes|[Install](https://www.datastax.com/blog/getting-started-apache-cassandra-windows-easy-way), https://www.youtube.com/watch?v=EEXtVn3zAqc|~ 10 min.|
Mac|Yes|[Install](https://codefoundries.com/developer/cassandra/cassan…), https://www.youtube.com/watch?v=JtpsOFXJUBw|~ 10 min.|
Docker (Windows)|Yes|[Install](https://cassandra.apache.org/doc/latest/getting_started/installing.html), https://www.datastax.com/learn/apache-cassandra-operations-in-kubernetes/running-a-cassandra-application-in-docker|~ 15 min.|
Docker (Ububtu 20.04)|Yes|[Install](https://hub.docker.com/_/cassandra)||
Docker (Mac)|Yes|[Install](https://hub.docker.com/_/cassandra)||
Raspbian|Yes (since Raspbian is Debian-based)|[Install](https://stackoverflow.com/questions/43690299/cassandra-on-raspberry-pi-3), https://docs.datastax.com/en/cassandra-oss/3.x/cassandra/install/installDeb.html||
Android|No|||
iOS|No|||

### Hardware Architectures 
Can it run on these CPUs?

|CPU Family|Yes/No|Known Limitations|
|--|--|--|
ARM|Yes (https://www.linux.com/training-tutorials/setting-arm-based-cassandra-cluster-beagle-bone-black/)|2 or more CPU cores needed for production server (https://cassandra.apache.org/doc/latest/operating/hardware.html#:~:text=While%20Cassandra%20can%20be%20made,at%20least%2032GB%20of%20RAM.)
INTEL|Yes|2 or more CPU cores needed for production server (https://cassandra.apache.org/doc/latest/operating/hardware.html#:~:text=While%20Cassandra%20can%20be%20made,at%20least%2032GB%20of%20RAM.)
AMD|Yes|2 or more CPU cores needed for production server (https://cassandra.apache.org/doc/latest/operating/hardware.html#:~:text=While%20Cassandra%20can%20be%20made,at%20least%2032GB%20of%20RAM.)
Embedded (Eiger, Aruix, etc.)|Yes (https://github.com/wlloyd/eiger)|2 or more CPU cores needed for production server (https://cassandra.apache.org/doc/latest/operating/hardware.html#:~:text=While%20Cassandra%20can%20be%20made,at%20least%2032GB%20of%20RAM.)

### Hardware Needs 
Create this table for all OS and CPU combinations tested 

#### EX: OS_A on CPU_B
<--MAP THIS TO THE EXPERIMENTS COMPLETED FOR YOUR TECHNOLOGY-->
||CPU|RAM|Hard Disk Memory|
|--|--|--|--|
|Idle|0.17142857142857143|93.39999999999999|10374848512.0|
|Max Observed Under Load A|21.3|96.3|10375655424|
|Average Observed Under Load A|7.466666666666666|94.08749999999999|10368999594.666666|
|Max Observed Under Load B|19.0|95.7|10379653120|
|Average Observed Under Load B|11.285714285714286|95.10000000000001|10376818688.0|

### Language Support 
Are there commercially available libraries for the following languages?

|Programming Language|Yes/No|Link(s)|
|--|--|--|
Python|Yes|[List](https://cassandra.apache.org/doc/latest/getting_started/drivers.html?highlight=drivers#python), https://towardsdatascience.com/getting-started-with-apache-cassandra-and-python-81e00ccf17c9, https://www.youtube.com/watch?v=NKsRYoLhSJU
JavaScript|Yes|[Datastax](https://docs.datastax.com/en/developer/nodejs-driver/4.1/getting-started/), https://www.npmjs.com/package/cassandra-driver
C|Yes|[Datastax](https://docs.datastax.com/en/developer/cpp-driver/2.0/), https://github.com/datastax/cpp-driver
C++|Yes|[List](https://cassandra.apache.org/doc/latest/getting_started/drivers.html?highlight=drivers#c).
C#|Yes|[List](https://cassandra.apache.org/doc/latest/getting_started/drivers.html?highlight=drivers#c-net)
Objective-C|No|
Java|Yes|[List](https://cassandra.apache.org/doc/latest/getting_started/drivers.html?highlight=drivers#java), https://www.baeldung.com/cassandra-with-java
Kotlin|Yes|[List](https://cassandra.apache.org/doc/latest/getting_started/drivers.html?highlight=drivers#java), https://docs.datastax.com/en/developer/java-driver/4.9/manual/mapper/config/kotlin/
Swift|Yes|https://github.com/YouClap/Kassandra
Go|Yes|[List](https://cassandra.apache.org/doc/latest/getting_started/drivers.html?highlight=drivers#go)
Ruby|Yes|[List](https://cassandra.apache.org/doc/latest/getting_started/drivers.html?highlight=drivers#ruby), https://docs.datastax.com/en/developer/ruby-driver/2.0/
PowerShell|Maybe|https://stackoverflow.com/questions/36664397/how-to-start-cassandra-server
Perl|Yes|[List](https://cassandra.apache.org/doc/latest/getting_started/drivers.html?highlight=drivers#perl)
Rust|Yes|[List](https://cassandra.apache.org/doc/latest/getting_started/drivers.html?highlight=drivers#rust)
Elixir|Yes|[List](https://cassandra.apache.org/doc/latest/getting_started/drivers.html?highlight=drivers#elixir)

# Base Experiment (MQ)

This experiment is an extension of the [Base experiment](./Base.md) that is specific to Datastore technologies.

## Qualitative Data

Fill in with information you discover about the given Data Store.
Please include any other key characteristics of the data store which amy not be outlined.

| Metric | Value |
| --- | --- |
| Use Case |Write-heavy workloads | 
| CAP Theorem Evaluation | [Official explanation](https://cassandra.apache.org/doc/latest/architecture/guarantees.html#what-is-cap) |  
| Database/Structure Hierarchy | [Keyspace, Partition, Table, Row, Column](https://cassandra.apache.org/doc/latest/architecture/overview.html#features) | 
| Replication / Clustering Availability |[Multi-master Replication](https://cassandra.apache.org/doc/latest/architecture/dynamo.html#multi-master-replication-versioned-data-and-tunable-consistency) | 
| Syntax/Query Language Support | [Cassandra Query Language](https://cassandra.apache.org/doc/latest/cql/index.html)| 


![](https://github.com/CTopham/Test_Repo/blob/master/Cassandradata.png)
