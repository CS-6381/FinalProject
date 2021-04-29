# Base Experiment
The goal of this experiment is to understand when the technology is viable to use. 

## Compatibility 
Here we wish to understand where the tech is easily used

Ceph is a unified storage system supporting Object-storage, Block-storage, and File-System storage. It can also deploy all of these in the same cluster. This makes it highly dynamic compared to other datastores. RADOS is the underlying storage layer for the object, block, and file storage. RADOS is distributed, elastic, and reliable with replication and erasure coding. Below are descriptions and examples of the types of storage built on RADOS. 

|Type of storage|Description|Possible Use-Case|
|--|--|--|
Object|Used for storing raw data. Good for storing large blob-like data files. Swift and S3-compatible APIs.|Video data
Block|Good for data that needs to be quickly retrieved and manipulated.|RDB, Raid Volumes
File-system storage|Distributed file system interface with POSIX semantics. Can be used on top of Object or Block storage. Good for data that needs to be easily accessible across nodes on the network.|Web content files.

Here you can also find a desciption of the features Ceph provides compared to other datastores.

|Feature|Description|
|--|--|
Thin-Provisioning|Optimizes storage space, notably with block storage.
Partial or Complete reads and writes|Can service part of an object if desired, or require full object with atomic transactions.
Erasure coding|Allows for data recovery if nodes go down or data gets corrupted.
Snapshot history|Can rollback to previous points in time.
POSIX file system semantics support|Makes for easy and standardized data retrieval.


### Basic Information
- How many individual actors can connect to this system at one time? Unable to find a number since it's based on the number of nodes deployed, but it's likely in the thousands to tens of thousands of range based on other similar technologies.
- What license does it operate under? Taken from the Ceph README: Most of Ceph is dual licensed under the LGPL version 2.1 or 3.0. Some miscellaneous code is under BSD-style license or is public domain. The documentation is licensed under Creative Commons Attribution Share Alike 3.0 (CC-BY-SA-3.0). There are a handful of headers included here that are licensed under the GPL. Please see the file COPYING for a full inventory of licenses by file.
- How much must be paid to use this technology? 
    - Open-Source: There is an open-sourced version that you can manually manage, and won't cost anything.
    - Subscription: You can also purchase and subscription for a cluster managed by RedHat. One quote online for a premium subscription was $82,864.99 for one year of service and Read Hat Support, with 25 physical nodes and 512 TB of storage.
- Does it have explicit enterprise support? Not explicitly called enterprise, but essentially the Red Hat Ceph Storage subscriptions are the equivalent.
- What does it favor with regards to the CAP Theorem? Ceph favors consistency. 
- Does service need to be interrupted for scaling or upgrades? No, hardware can be removed or added while Ceph is online. 

### Operating Systems
Can it be installed on the below?

|Operating System/Technology|Yes/No|Link to steps|Average Install Time| Number of Manual Steps to Install|
|--|--|--|--|--|
Ububtu 18.04|Yes|https://computingforgeeks.com/how-to-deploy-ceph-storage-cluster-on-ubuntu-18-04-lts/#:~:text=In%20this%20guide%2C%20we%20will,%2C%20and%20file%2Dlevel%20storage.||
Ububtu 20.04|Yes|https://ubuntu.com/ceph/install||
Windows 7|Possibly - Not officially supported|https://github.com/ceph/ceph/blob/master/README.windows.rst||
Windows 10|Yes|https://github.com/ceph/ceph/blob/master/README.windows.rst||
Mac|Yes|https://github.com/mulbc/homebrew-ceph-client#:~:text=README.md-,Ceph%20client%20libraries%20for%20Homebrew,install%20and%20update%20Ceph%20libraries.||
Docker (Windows)|Yes|https://access.redhat.com/documentation/en-us/red_hat_ceph_storage/3/html/container_guide/deploying-red-hat-ceph-storage-in-containers||
Docker (Ububtu 20.04)|Yes|https://access.redhat.com/documentation/en-us/red_hat_ceph_storage/3/html/container_guide/deploying-red-hat-ceph-storage-in-containers||
Docker (Mac)|Yes|https://access.redhat.com/documentation/en-us/red_hat_ceph_storage/3/html/container_guide/deploying-red-hat-ceph-storage-in-containers||
CentOS 7|Yes|https://opensource.com/article/21/1/ceph-raspberry-pi#:~:text=Ceph%20is%20an%20open%20source,in%20a%20unified%20storage%20cluster.&text=This%20article%20will%20show%20you,in%20a%20Raspberry%20Pi%20cluster.|||=
Raspian||||
Android||||
iOS||||
Kubernetes|Yes|https://www.digitalocean.com/community/tutorials/how-to-set-up-a-ceph-cluster-within-kubernetes-using-rook||

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
- Commodity hardware is sufficient.
- Ceph is write intensive. 
- Ceph File System is CPU intensive. 

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
Python|Yes|https://pypi.org/project/python-cephclient/
JavaScript||
C|Yes|https://people.redhat.com/bhubbard/nature/default/rados/api/librados-intro/
C++|Yes|https://people.redhat.com/bhubbard/nature/default/rados/api/librados-intro/
C#||
Objective-C||
Java|Yes|https://people.redhat.com/bhubbard/nature/default/rados/api/librados-intro/
Kotlin||
Swift||
Go|Yes|https://github.com/ceph/go-ceph
Ruby||
Powershell||
Perl||

# Issues
We were unable to successfully deploy Ceph after trying several methods. Unfortunately, this means that we were unable to run any experiments against it, but the difficulty deploying it should be taken into account when comparing with other technologies.
