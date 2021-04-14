# Base Experiment
The goal of this experiment is to understand when the technology is viable to use. 

## Compatibility 
Here we wish to understand where the tech is easily used

### Qualitative 

For MQ experiments, see [Base MQ experiment](./Base-MQ.md)

For data stores, TBD.

### Basic Information
- How many individual actors can connect to this system at one time? Connections can be pooled into scalable solutions.
- What license does it operate under?
- How much must be paid to use this technology?
    - None
- Does it have explicit enterprise support? Yes

### Operating Systems
Can it be installed on the below?

|Operating System|Yes/No|Link to steps|Average Install Time| Number of Manual Steps to Install|
|--|--|--|--|--|
Ububtu 18.04|Yes|https://www.postgresql.org/download/linux/ubuntu/|5 min|
Ububtu 20.04|Yes|https://www.postgresql.org/download/linux/ubuntu/|5 min|
Windows 7|Yes|https://www.postgresql.org/download/windows/|5 min|
Windows 10|Yes|https://www.postgresql.org/download/windows/|5 min|
Mac|Yes|https://www.postgresql.org/download/macosx/|5 min|
Docker (Windows)|Yes|https://hub.docker.com/_/postgres|1 min|
Docker (Ububtu 20.04)|Yes|https://hub.docker.com/_/postgres|1 min|
Docker (Mac)|Yes|https://hub.docker.com/_/postgres|1 min|
Raspian|Yes|https://www.postgresql.org/download/linux/debian/|5 min|
Android|No||5 min|
iOS|No|||

### Hardware Architectures 
Can it run on these CPUs?

|CPU Family|Yes/No|Known Limitations|
|--|--|--|
ARM|No|N/A
INTEL|Yes|None
AMD|Yes|None
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
Python|Yes|https://www.postgresqltutorial.com/postgresql-python/
JavaScript|Yes|https://node-postgres.com/
C|Yes|https://www.postgresql.org/docs/9.1/libpq.html
C++|Yes|https://www.postgresql.org/docs/7.2/libpqplusplus.html
C#|Yes|https://www.npgsql.org/
Objective-C|Yes|http://objective-cloud.com/docs/using-a-database/
Java|Yes|https://jdbc.postgresql.org/
Kotlin|Yes|https://github.com/JetBrains/Exposed
Swift|Yes|https://developer.apple.com/forums/thread/91392
Go|Yes|https://medium.com/avitotech/how-to-work-with-postgres-in-go-bad2dabd13e4
Ruby|Yes|https://zetcode.com/db/postgresqlruby/
Powershell|Yes|https://www.cdata.com/kb/tech/postgresql-ado-powershell.rst
Perl|Yes|https://www.compose.com/articles/connecting-and-loading-data-to-postgresql-with-perl/
Rust|Yes|https://crates.io/crates/postgres
Elixir|Yes|https://elixirschool.com/en/lessons/ecto/basics/
