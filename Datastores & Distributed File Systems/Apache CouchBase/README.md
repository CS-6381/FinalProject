# Base Experiment
The goal of this experiment is to understand when the technology is viable to use. 

## Compatibility 
Here we wish to understand where the tech is easily used

### Couchbase
Couchbase is an open source, distributed, NoSQL document-oriented engagement database, optimized for interactive applications. Couchbase is meant to help developers build quickly, scale big, and save more.

|Type of storage|Description|Possible Use-Case|
|--|--|--|
JSON Object|Used for storing JSON Formatted Raw data| Json Data
Key Value/Binary Object|Used for storing raw data not in JSON Format. Good for storing large blob-like data files|Images|


Here you can also find a desciption of the features of Couchbase to compare with other datastores.

|Feature|Description|
|--|--|
NoSQL|Data is stored in key-value object/item format, or JSON Object format. Unlike relational databases, there is no requirement to create a schema|
N1QL ("nickel")|Declarative query language that extends SQL for JSON data. Combines familiarity of SQL with flexibility of JSON data model
Distribution|Automatically distributes data across all servers or virtual machines|
Mem Cached Protocol Capability|Achieve Data Replication, Durability and Zero Application downtime when adding and removing servers
Durability|Ensures likelihood of data-writes surviving unexpected events such as node outages
Memory-First|Operations occur in memory, thus avoiding traditional database disk I/O bottlenecks
Elastic Scalability|Ability to separate different data processing workloads in distinct scalable services. This provides flexibility to applications with changing workloads and requirements
Persistence|Protection against data loss, buckets can be configured for replication to create redundancy, and data is also written to disk so that in the event of a crash, data can be retrieved from the disk for recovery.
Replication|Provides high availability for reading and writing data through [Intra-Cluster replication, Index Replication, and Cross Datacenter Replication](https://docs.couchbase.com/server/5.1/architecture/high-availability-replication-architecture.html)



### Basic Information
- How many individual actors can connect to this system at one time? 
- What license does it operate under?
    -  Couchbase has an Open Sourced Edition which operates under the Apache License 2.0. They also have Community edition which operates under the Community Edition License Agreement,  and the Enterprise edition which operates under the Enterprise Subscription License Agreeement 
- How much must be paid to use this technology?
    - One time fee?
    - Monthly?
    - Yearly?
        - Open Source Version: Free
- Does it have explicit enterprise support? 
    - [Couchbase](https://www.couchbase.com/support-policy/enterprise-software) provides enterprise support.  
- Uses in industry:
    - Caching
    - Mobile data management 
    - Session management
    - Mainframe offload
    - User profile store
    - Source-of-truth data stores
    - Operational dashboards
    - Device management
    - Mobile wallet
    - Pricing
    - Product catalog
    - Omnichannel
    - Personalization
    - Shopping cart
    - Recommendations
    https://www.couchbase.com/customers
- Key Features:
    - N1QL
    - In-memory database
    - Cross datacenter replication
    - Multi-dimensional scaling  
    - Analytics  
    https://www.couchbase.com/customers
    
# Operating Systems
|Operating System|Yes/No|Link to steps|Average Install Time| Number of Manual Steps to Install|
|--|--|--|--|--|
Ububtu 18.04|Yes|https://docs.couchbase.com/server/current/install/ubuntu-debian-install.html|
Ububtu 20.04|No|||
Windows 7|No||
Windows 10|Yes (dev and testing only)|https://docs.couchbase.com/server/current/install/install-package-windows.html||
Windows Server 2019|Yes|https://docs.couchbase.com/server/current/install/install-package-windows.html||
Windows Server 2016|Yes|https://docs.couchbase.com/server/current/install/install-package-windows.html||
Mac 10.14 "Mojave"|Yes|https://docs.couchbase.com/server/current/install/macos-install.html||
Mac 10.13 "High Sierra"|Yes|https://docs.couchbase.com/server/current/install/macos-install.html||
Docker (Windows)|Yes|https://docs.couchbase.com/server/current/install/getting-started-docker.html||
Docker (Ububtu 18.04)|Yes|https://docs.couchbase.com/server/current/install/getting-started-docker.html||
Docker (Mac)|Yes|https://docs.couchbase.com/server/current/install/getting-started-docker.html||
Raspian||||
Android||||
iOS||||
Kubernetes|Yes|https://docs.couchbase.com/operator/current/install-kubernetes.htm||


### Hardware Architectures 
Can it run on these CPUs?

|CPU Family|Yes/No|Known Limitations|
|--|--|--|
ARM|No|
INTEL|Yes|
AMD|Yes|
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
Python|Yes|https://docs.couchbase.com/python-sdk/current/hello-world/overview.html|
JavaScript|Yes|https://docs.couchbase.com/couchbase-lite/current/javascript.html|
C|Yes|https://docs.couchbase.com/c-sdk/current/hello-world/overview.html|
C++|Yes|https://docs.couchbase.com/cxx-txns/current/distributed-acid-transactions-from-the-sdk.html|
C#|Yes|https://docs.couchbase.com/dotnet-sdk/current/howtos/distributed-acid-transactions-from-the-sdk.html|
Objective-C|Yes|https://docs.couchbase.com/couchbase-lite/current/objc/quickstart.html\
Java|Yes|https://docs.couchbase.com/java-sdk/current/hello-world/overview.html|
Kotlin||
Swift|Yes|https://docs.couchbase.com/couchbase-lite/current/swift/quickstart.html|
Go|Yes|https://docs.couchbase.com/go-sdk/current/hello-world/overview.html|
Ruby|Yes|https://docs.couchbase.com/ruby-sdk/current/hello-world/overview.html|
Powershell||
Perl||
