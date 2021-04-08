# Base Experiment
The goal of this experiment is to understand when the technology is viable to use. 

## Compatibility 
Here we wish to understand where the tech is easily used

MinIO was designed to be a high performance cloud object store.
https://min.io/resources/docs/MinIO-high-performance-object-storage.pdf

|Type of storage|Description|Possible Use-Case|
|--|--|--|
Object|Used for storing raw data. Good for storing large blob-like data files.|Video data

Here you can also find a desciption of the features MinIO to comare with other datastores.

|Feature|Description|
|--|--|
Performance|Designed for high performance.
Scalability|Designed with high scalability in mind.
Simplicity|Designed to be a simple as possible.
Erasure Coding|Allows for data recovery if nodes go down or data gets corrupted.
BitRot Protection|Will capture and heal corrupted data on the fly.
Identity and Access Management|Centralized access, temporary passwords, rotated tokens.
Encryption|Multiple server-side encryption schemes can be used: AES-256-GCM, ChaCha20-Poly1305 and AES-CBC.
Continous Replication|Tracks changes across Petabytes of data for replication to support disaster recovery.
Monitoring|Container build-in prometheus monitoring for an easy-to-monitor solution.
Metadata Architecture|Does not have a separate metadata store, to support strong consistency and reduce points of failure.
Kubernetes Native|Designed to deploy natively into a kubernetes environment.


MinIO has also provided their own performance benchmarks:
**8 node MinIO cluster**
|Setup|Avg Read Throughput (GET)|Avg Write Throughput (PUT)
|--|--|--|
Distributed|46.54 GB/s|34.4 GB/s
Distributed with Encryption|46.4 GB/s|34.6 GB/s

**32 node MinIO cluster**
|Setup|Avg Read Throughput (GET)|Avg Write Throughput (PUT)
|--|--|--|
Distributed|183.2 GB/s|171.3 GB/s
Distributed with Encryption|162 GB/s|114.7 GB/s


### Basic Information
- How many individual actors can connect to this system at one time? Unable to find data. It will scale up with the number of nodes deployed though, of course.
- What license does it operate under? Both 100% Open Source GNU AGPL v3 and Commercial licenses, depending on the tier.
- How much must be paid to use this technology?
https://min.io/pricing
|Feature|Community|Standard|Enterprise|
|--|--|--|--|
Price|Free|$10/TB/Month|$20/TB/Month
License|100% Open Source: GNU AGPL v3|Commercial|Commercial
Software Releases|Update to Latest|1 Year Long Term Support|5 Years Long Term Support
SLA|None|< 24hr SLA|< 1hr SLA
Support|Public Slack Channel + Github Issues|24x7 L4 Direct Engineering Support via SUBNET|24x7 L4 Direct Engineering Support via SUBNET
Security Updates & Critical Bugs|Self Update|Guided Update|Guided Update
Panic Button|None|1 per year|Unlimited
Annual Architecture Review|No|Yes|Yes
Annual Performance Review|No|Yes|Yes
Indemnification|No|No|Yes
Security + Policy Review|No|No|Yes
- Does it have explicit enterprise support? Yes

### Operating Systems
Can it be installed on the below?

|Operating System|Yes/No|Link to steps|Average Install Time| Number of Manual Steps to Install|
|--|--|--|--|--|
Ububtu 18.04||||
Ububtu 20.04||||
Windows 7|Possibly - Windows version not specified|https://docs.min.io/docs/minio-quickstart-guide.html||
Windows 10|Yes|https://docs.min.io/docs/minio-quickstart-guide.html||
Mac|Yes|https://docs.min.io/docs/minio-quickstart-guide.html||
Docker (Windows)|Yes|https://docs.min.io/docs/minio-docker-quickstart-guide.html||
Docker (Ububtu 20.04)|Yes|https://docs.min.io/docs/minio-docker-quickstart-guide.html||
Docker (Mac)|Yes|https://docs.min.io/docs/minio-docker-quickstart-guide.html||
Raspian||||
Android||||
iOS||||
Kubernetes|Yes|https://github.com/minio/operator/blob/master/README.md||


### Hardware Architectures 
Can it run on these CPUs?

|CPU Family|Yes/No|Known Limitations|
|--|--|--|
ARM|Yes|
INTEL||
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

### Language Support 
Are there commercially available libraries for the following languages?

|Programming Language|Yes/No|Link(s)|
|--|--|--|
Python|Yes|https://docs.min.io/docs/python-client-api-reference.html
JavaScript|Yes|https://docs.min.io/docs/javascript-client-api-reference.html
C||
C++||
C#||
.Net|Yes|https://docs.min.io/docs/dotnet-client-api-reference.html
Objective-C||
Java|Yes|https://docs.min.io/docs/java-client-api-reference.html
Kotlin||
Swift||
Go|Yes|https://docs.min.io/docs/golang-client-api-reference.html
Ruby||
Powershell||
Perl||
