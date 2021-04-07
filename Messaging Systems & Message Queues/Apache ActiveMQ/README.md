# Apache ActiveMQ
Apache ActiveMQ is an open source message broker written in Java together with a full Java Message Service (JMS) client. It provides "Enterprise Features" which in this case means fostering the communication from more than one client or server. Supported clients include Java via JMS 1.1 as well as several other "cross language" clients. The communication is managed with features such as computer clustering and ability to use any database as a JMS persistence provider besides virtual memory, cache, and journal persistency.[Wikipedia](https://en.wikipedia.org/wiki/Apache_ActiveMQ)

*Note: There is another project called Artemis which also goes by ActiveMQ Artemis. This is a different project, based off the code donated by HornetQ. Both Artemis and ActiveMQ use JMS, but they are diffferent code bases. Artemis is planned to be a successor for ActiveMQ, but that migration is still in progress.* [See details here.](https://www.redpill-linpro.com/techblog/2020/10/06/activemq-artemis-getting-started.html)

## Compatibility 
ActiveMQ utilizes the STOMP transport protocol, which makes it highly available to a variety of programming languages, including Python.

- [Python with ActiveMQ](https://ameyanekar.medium.com/create-an-activemq-client-using-python-c532b6f91074)
- [JMS - Publish Subscribe Examples using ActiveMQ and Maven](https://codenotfound.com/jms-publish-subscribe-messaging-example-activemq-maven.html)
- [ActiveMQ vs. Redis PubSub](https://freshcodeit.com/freshcode-post/introduction-to-message-brokers-activemq-vs-redis-pub-sub)

### Basic Information
- How many individual actors can connect to this system at one time? 
    - [Default is 1000](https://stackoverflow.com/questions/46035294/activemq-exceeded-the-maximum-number-of-allowed-client-connections#:~:text=1000%20connections%20should%20be%20the,the%20Apache%20distribution%20of%20ActiveMQ.)
- What license does it operate under?
    - Apache License 2.0
- How much must be paid to use this technology?
    - One time fee?
    - Monthly?
      - ~$430 Large/~$43 Micro - [Amazon Active MQ](https://aws.amazon.com/amazon-mq/pricing/)
    - Yearly?
- Does it have explicit enterprise support? 
    - [Commercial support](https://activemq.apache.org/support) from Amazon, Red Hat and others

### Operating Systems
Can it be installed on the below?

|Operating System|Yes/No|Link to steps|Average Install Time| Number of Manual Steps to Install|
|--|--|--|--|--|
Ububtu 18.04|Yes|[link](https://activemq.apache.org/version-5-getting-started.html)||
Ububtu 20.04|Yes|[link](https://activemq.apache.org/version-5-getting-started.html)||
Windows 7|Yes|[link](https://activemq.apache.org/version-5-getting-started.html)||
Windows 10|Yes|[link](https://activemq.apache.org/version-5-getting-started.html)||
Mac|Yes|[link](https://activemq.apache.org/version-5-getting-started.html)||
Docker (Windows)|Yes|[link](https://www.chriswirz.com/software/activemq-windows-nano-using-docker-build-stages)||
Docker (Ububtu 20.04)|Yes|Self-build||
Docker (Mac)||||
Raspian|Yes|[link](http://activemq.2283324.n4.nabble.com/ActiveMQ-on-raspberry-pi-tp4695624p4695635.html)||
Android||||
iOS||||

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

### Language Support 
Are there commercially available libraries for the following languages?

|Programming Language|Yes/No|Link(s)|
|--|--|--|
Python|Yes|
JavaScript||
C||
C++||
C#||
Objective-C||
Java|Yes|
Kotlin||
Swift||
Go||
Ruby||
Powershell||
Perl||
