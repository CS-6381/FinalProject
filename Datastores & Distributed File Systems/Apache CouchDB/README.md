# Base Experiment
The goal of this experiment is to understand when the technology is viable to use. 

## Compatibility 
Here we wish to understand where the tech is easily used

### Basic Information
Apache CouchDB is an open source, distributed, document-oriented NoSQL database implemented in Erlang. It stores data with JSON documents and uses Javascript as query language and supports MapReduce. It uses HTTP for an API.

||**Apache CouchDB**|
|--|--|
|**Website(s)**|<ul><li>Official documentation: https://docs.couchdb.org/en/stable/index.html<li> Official Github repo: https://github.com/apache/couchdb|
|**Overview Basics**|Couch Replication Protocol|
|**Implementation Basics**|https://docs.couchdb.org/en/stable/install/index.html|
|**Use Cases**|<ul><li>Progressive web development <li>Dynamic content platform <li>Ideal for mobile devices where network connection is not guaranteed|
|**Features**|<ul><li>ACID semantics<li>Built for offline: can replicate to decives that can go offline and handle data sync when device is back online<li>Distributed architecture with replication<li>Document storage <li>Eventual consistency <li>MapReduce views and indexes <li>HTTP API|
|**Scalability**|Highly scalable|


### Operating Systems
|Operating System|Yes/No|Link to steps|Average Install Time| Number of Manual Steps to Install|
|--|--|--|--|--|
Ububtu 18.04|Yes|https://docs.couchdb.org/en/stable/install/unix.html|
Ububtu 20.04|Yes|https://docs.couchdb.org/en/stable/install/unix.html|
Debian 9|Yes|https://docs.couchdb.org/en/stable/install/unix.html|
Debian 10|Yes|https://docs.couchdb.org/en/stable/install/unix.html|
CentOS|Yes|https://docs.couchdb.org/en/stable/install/unix.html|
Windows|Yes (8, 8.1, 10 require the .NET Framework v3.5)|https://docs.couchdb.org/en/stable/install/windows.html|
MacOS|Yes|https://docs.couchdb.org/en/stable/install/mac.html|
Docker|Yes|https://docs.couchdb.org/en/stable/install/docker.html||
Kubernetes|Yes|https://docs.couchdb.org/en/stable/install/kubernetes.html||


### Hardware Architectures 
Can it run on these CPUs?

|CPU Family|Yes/No|Known Limitations|
|--|--|--|
ARM|Yes|
INTEL|Yes|
AMD|Yes|

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


### Language Support
Are there commercially available libraries for the following languages?

|Programming Language|Yes/No|Link(s)|
|--|--|--|
Python|Yes|https://cwiki.apache.org/confluence/display/COUCHDB/Python|
JavaScript|Yes (Officially maintained)|https://cwiki.apache.org/confluence/pages/viewpage.action?pageId=97555281|
C/C++|Yes|https://cwiki.apache.org/confluence/pages/viewpage.action?pageId=44993997|
C#|Yes|https://cwiki.apache.org/confluence/pages/viewpage.action?pageId=97555303|
Objective-C|Yes|https://cwiki.apache.org/confluence/display/COUCHDB/Objective-C|
Java|Yes|https://cwiki.apache.org/confluence/display/COUCHDB/Java|
Kotlin||
Swift||
Go|Yes|https://cwiki.apache.org/confluence/display/COUCHDB/Go|
Ruby Client|Yes|https://cwiki.apache.org/confluence/display/COUCHDB/Ruby+Client|
Powershell||
Perl|Yes|https://cwiki.apache.org/confluence/display/COUCHDB/Perl|
Lisp|Yes|https://cwiki.apache.org/confluence/display/COUCHDB/Lisp|
