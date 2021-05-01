# Base Experiment
The goal of this experiment is to understand when the technology is viable to use.

## Experiment Hardware Configuration
Each test should be run using Ubuntu 20.04 chameleon cloud VM’s with 8 CPU and 32 GB of RAM. If these hardware specs aren’t attainable, use the nearest available and document the configuration. Please also use internal IP addresses for all communication to simulate a more consistent network topology with less traffic.

## Compatibility
 - Generally compatible with Linux, Mac, and Windows operating systems with libraries for Java and Python implementations. Java is much more strongly supported 

## Qualitative Data

| Metric | Value |
| --- | --- |
| Centricity (data-centric or message-centric) | data-centric |
| Connection (machine-to-machine or point-to-point) | point-to-point |
| Underlying Architecture (decentralized or hub-and-spoke) | decentralized |
| Protocol | REST |
| Transport(s) | external => HTTP, internal => gRPC |
| Data Serialization | built-in base types and ability to add custom types |
| Supports Queuing | no |
| Data Type Representation | types related to databases and batches |
| QoS Parameters | exactly-once execution, windowing, checkpointing |
| Supports Dynamic Discovery | no |
| Communication Patterns | streaming or batch |
| Abstraction Layer | REST |
| Up-front Complexity | very high |
| Large Implementations | yes - can be distributed over 1000s of machines/containers |

### Basic Information
- How many individual actors can connect to this system at one time?
  - reads directly from a queue or a file system, inherently is not connected to actors
- What license does it operate under?
  - Apache License 2.0
- How much must be paid to use this technology?
    - One time fee? NO
    - Monthly? NO
    - Yearly? NO
- Does it have explicit enterprise support? NO

### Operating Systems
Can it be installed on the below?

| Operating System | Yes/No | Link to steps | Average Install Time | Number of Manual Steps to Install |
| --- | --- | --- | --- | --- |
| Ubuntu 18.04 | yes | [installation instructions](https://ci.apache.org/projects/flink/flink-docs-release-1.12/try-flink/local_installation.html) | 5 minutes | 3 steps |
| Ubuntu 20.04 | yes | [installation instructions](https://ci.apache.org/projects/flink/flink-docs-release-1.12/try-flink/local_installation.html) | 5 minutes | 3 steps |
| Windows 7 | yes | [installation instructions](https://ci.apache.org/projects/flink/flink-docs-release-1.12/try-flink/local_installation.html) | 5 minutes | 3 steps |
| Windows 10 | yes | [installation instructions](https://ci.apache.org/projects/flink/flink-docs-release-1.12/try-flink/local_installation.html) | 5 minutes | 3 steps |
| Mac | yes | [installation instructions](https://ci.apache.org/projects/flink/flink-docs-release-1.12/try-flink/local_installation.html) | 5 minutes | 3 steps |
| Docker (Windows) | yes | [installation instructions](https://ci.apache.org/projects/flink/flink-docs-release-1.12/try-flink/local_installation.html) | 5 minutes | 3 steps |
| Docker (Ububtu 20.04) | yes | [installation instructions](https://ci.apache.org/projects/flink/flink-docs-release-1.12/try-flink/local_installation.html) | 5 minutes | 3 steps |
| Docker (Mac) | yes | [installation instructions](https://ci.apache.org/projects/flink/flink-docs-release-1.12/try-flink/local_installation.html) | 5 minutes | 3 steps |
| Raspian| no |  |  |
| Android| no |  |  |
| iOS| no |  |  |

### Hardware Architectures
Can it run on these CPUs?

| CPU Family | Yes/No | Known Limitations |
| --- | --- | --- |
| ARM | yes |  | 
| INTEL | yes |  |
| AMD | yes |  |
| Embedded (Eiger, Aruix, etc.) | no |  |

### Hardware Needs
Create this table for all OS and CPU combinations tested

#### EX: OS_A on CPU_B
<--MAP THIS TO THE EXPERIMENTS COMPLETED FOR YOUR TECHNOLOGY-->

|  | CPU | RAM | Hard Disk Memory |
| --- | --- | --- | --- |
| Idle |  |  |  |
| Max Observed Under Load A |  |  |  |
| Average Observed Under Load A |  |  |  |
| Max Observed Under Load B |  |  |  |
| Average Observed Under Load B |  |  |  |

### Language Support
Are there commercially available libraries for the following languages?

| Programming Language | Yes/No | Link(s) |
| --- | --- | --- |
| Python | yes | [docs](https://ci.apache.org/projects/flink/flink-docs-release-1.12/api/python/) |
| JavaScript | no |  |
| C | no |  |
| C++ | no |  |  |
| C# | no |  |  |
| Objective-C | no |  |
| Java | yes | [docs](https://ci.apache.org/projects/flink/flink-docs-release-1.12/api/java/) |
| Kotlin | no |  |
| Swift | no |  |
| Go | no |  |
| Ruby | no |  |
| Powershell | no |  |
| Perl | no |  |
| Rust | no |  |
| Elixr | no |  |
