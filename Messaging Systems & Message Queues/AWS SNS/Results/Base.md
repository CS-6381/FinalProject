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
- How many individual actors can connect to this system at one time? 1 publisher to up to 10 million subscribers times the 100,000 topics per account
- What license does it operate under? SNS operates under its own license users who want to use it commercial must pay for the license, but for personal use then its only 1$ hold on a card which they give back. 
- How much must be paid to use this technology? 
    - One time fee? One time fee that is given back of a 1$ -> monthly and yearly change at varying rates. 
    - Monthly?
    - Yearly?
- Does it have explicit enterprise support? Yes through amazon. 

### Operating Systems
Can it be installed on the below?
If the operating system can access the internet. Then you access the software from the link: https://docs.aws.amazon.com/sns/latest/dg/sns-getting-started.html

|Operating System|Yes/No|Link to steps|Average Install Time| Number of Manual Steps to Install|
|---|---|---|---|---|
Ububtu 18.04|Yes|||
Ububtu 20.04|Yes|||
Windows 7|Yes|||
Windows 10|Yes|||
Mac|Yes|||
Docker (Windows)|Yes|||
Docker (Ububtu 20.04)|Yes|||
Docker (Mac)|Yes|||
Raspian|Yes|||
Android|Yes|||
iOS|Yes|||

### Hardware Architectures 
Can it run on these CPUs?
Referencing the above link if the hardware is able to access the internet the can reach the Amazon SNS hub, and as long as it can run code in any form then it will be able to utilize the sns. 

|CPU Family|Yes/No|Known Limitations|
|---|---|---|
ARM||
INTEL||
AMD||
Embedded (Eiger, Aruix, etc.)||


### Language Support 
Are there commercially available libraries for the following languages?

|Programming Language|Yes/No|Link(s)|
|---|---|---|
Python|Yes |https://www.geeksforgeeks.org/popular-programming-languages-supported-by-aws/ 
JavaScript|Yes| https://www.geeksforgeeks.org/popular-programming-languages-supported-by-aws/ 
C|No|
C++|No|
C#|No|
Objective-C|No|
Java|Yes|https://www.geeksforgeeks.org/popular-programming-languages-supported-by-aws/ 
Kotlin|Yes| https://www.geeksforgeeks.org/popular-programming-languages-supported-by-aws/ 
Swift|No|
Go|Yes| https://www.geeksforgeeks.org/popular-programming-languages-supported-by-aws/ 
Ruby|No|
Powershell|No|
Perl|No|
Rust|No|
Elixr|No|
