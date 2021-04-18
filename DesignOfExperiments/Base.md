# Base Experiment
The goal of this experiment is to understand when the technology is viable to use. 

## Expiriment Hardware Configuration
Each test should be ran using Ubuntu 20.04 chameleon cloud VM’s with 8 CPU and 32 GB of RAM. If these hardware specs aren’t attainable, use the nearest available and document the configuration. Please also use internal IP addresses for all communication to simulate a more consistent network topology with less traffic. 

## Compatibility 
Here we wish to understand where the tech is easily used

### Qualitative 

For MQ experiments, see [Base MQ experiment](./Base-MQ.md)

For data stores, TBD.

### Basic Information
- How many individual actors can connect to this system at one time? 
- What license does it operate under?
- How much must be paid to use this technology?
    - One time fee?
    - Monthly?
    - Yearly?
- Does it have explicit enterprise support? 

### Operating Systems
Can it be installed on the below?

|Operating System|Yes/No|Link to steps|Average Install Time| Number of Manual Steps to Install|
|--|--|--|--|--|
Ububtu 18.04||||
Ububtu 20.04||||
Windows 7||||
Windows 10||||
Mac||||
Docker (Windows)||||
Docker (Ububtu 20.04)||||
Docker (Mac)||||
Raspian||||
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

|Programming Language|Yes/No|Link(s)|
|--|--|--|
Python||
JavaScript||
C||
C++||
C#||
Objective-C||
Java||
Kotlin||
Swift||
Go||
Ruby||
Powershell||
Perl||
Rust||
Elixr||
