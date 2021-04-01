# Redis
Redis (Remote Dictionary Server) is an in-memory data structure store, used as a distributed, in-memory key–value database, cache and message broker, with optional durability. Redis supports different kinds of abstract data structures, such as strings, lists, maps, sets, sorted sets, HyperLogLogs, bitmaps, streams, and spatial indexes. [Wikipedia](https://en.wikipedia.org/wiki/Redis)

It is written in ANSI C. The development of Redis is sponsored by Redis Labs today; before that, it was sponsored by Pivotal and VMware. According to the monthly ranking by DB-Engines.com, Redis is the most popular key-value store. [Docker](https://hub.docker.com/_/redis)


## Compatibility 

While Redis is most known for its NoSQL capabilities, it also provides an implementation of the Pub/Sub paradigm. Redis can also be used as a message bus.

- [Redis Pub/Sub - Docs](https://redis.io/topics/pubsub)    
- [Scaling Pub-Sub with Redis - Redisday Talk](https://www.youtube.com/watch?v=6G22a5Iooqk)
- [Redis Pub/Sub using Python - Tutorial](https://kb.objectrocket.com/redis/basic-redis-usage-example-part-1-exploring-pub-sub-with-redis-python-583)

### Basic Information
- How many individual actors can connect to this system at one time?
  - According to benchmarks, 100,000 users can connect to a single instance of Redis per second.
  - Redis also provides clustering, which might lower the amount of throughput due to message copying. 
- What license does it operate under?
  - It is open-source software released under a BSD 3-clause license.
- How much must be paid to use this technology?
    - One time fee?
    - [Monthly?](https://www.g2.com/products/redis-enterprise/pricing)
      - Multi-AZ - $93
      - Standard -$71
      - Cache - $22
    - Yearly?
- Does it have explicit enterprise support? 
  - [Redis Labs](https://redislabs.com/) provides enterprise support.

### Operating Systems
Can it be installed on the below?

|Operating System|Yes/No|Link to steps|Average Install Time| Number of Manual Steps to Install|
|--|--|--|--|--|
Ububtu 18.04|Yes|||
Ububtu 20.04|Yes|||
Windows 7|Yes|||
Windows 10|Yes|||
Mac|Yes|||
Docker (Windows)|Yes|||
Docker (Ububtu 20.04)|Yes|||
Docker (Mac)|Yes|||
Raspian||||
Android||||
iOS||||

### Hardware Architectures 
Can it run on these CPUs?

|CPU Family|Yes/No|Known Limitations|
|--|--|--|
ARM|Yes|
INTEL|Yes|
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

### Language Support 
Are there commercially available libraries for the following languages?

|Programming Language|Yes/No|Link(s)|
|--|--|--|
Python|Yes|
JavaScript|Yes|
C|Yes|
C++|Yes|
C#|Yes|
Objective-C|Yes|
Java|Yes|
Kotlin||
Swift|Yes|
Go|Yes|
Ruby|Yes|
Powershell||
Perl|Yes|
