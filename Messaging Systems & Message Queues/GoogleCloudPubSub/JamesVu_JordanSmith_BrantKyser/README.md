**Base Experiment**

The goal of this experiment is to understand when the technology is
viable to use.

**Experiment Hardware Configuration**

Each test should be ran using Ubuntu 20.04 chameleon cloud VM’s with 8
CPU and 32 GB of RAM. If these hardware specs aren’t attainable, use the
nearest available and document the configuration. Please also use
internal IP addresses for all communication to simulate a more
consistent network topology with less traffic.

**Compatibility**

Here we wish to understand where the tech is easily used

**Qualitative**

For MQ experiments, see [<u>Base MQ
experiment</u>](https://github.com/CS-6381/FinalProject/blob/main/DesignOfExperiments/Base-MQ.md)

For data stores, TBD.

**Basic Information**

-   How many individual actors can connect to this system at one time?
    One connection per subscription name. Multiple connections into a
    publication name is okay.

-   What license does it operate under? Creative Commons Attribution 4.0
    License, Apache 2.0 License
    (https://cloud.google.com/pubsub/pricing)

-   How much must be paid to use this technology? Need lots of requests
    to be expensive (https://cloud.google.com/pubsub/pricing)

    -   One time fee?

    -   Monthly?

    -   Yearly?

-   Does it have explicit enterprise support? A person may be able to
    contact Google Cloud (https://cloud.google.com/contact).

**Operating Systems**

Can it be installed on the below?

<table>
<thead>
<tr class="header">
<th><strong>Operating System</strong></th>
<th><strong>Yes/No</strong></th>
<th><strong>Link to steps</strong></th>
<th><strong>Average Install Time</strong></th>
<th><strong>Number of Manual Steps to Install</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Ubuntu 18.04</td>
<td>Yes</td>
<td>Please refer to Documentation folder.</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Ubuntu 20.04</td>
<td>Yes</td>
<td>https://pypi.org/project/google-cloud-pubsub/</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Windows 7</td>
<td>Yes</td>
<td>Refer to Windows 10</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Windows 10</td>
<td>Yes</td>
<td><p><a href="https://www.youtube.com/watch?v=f5DOsB7Nlw0&amp;t=254s">https://www.youtube.com/watch?v=f5DOsB7Nlw0&amp;t=254s</a></p>
<p><a href="https://cloud.google.com/pubsub/docs/building-pubsub-messaging-system">https://cloud.google.com/pubsub/docs/building-pubsub-messaging-system</a></p>
<p><a href="https://www.youtube.com/watch?v=UKAmZBrR300">https://www.youtube.com/watch?v=UKAmZBrR300</a></p></td>
<td>~ 20 min.</td>
<td></td>
</tr>
<tr class="odd">
<td>Mac</td>
<td>Yes</td>
<td>https://pypi.org/project/google-cloud-pubsub/</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Docker (Windows)</td>
<td>Yes</td>
<td>https://cloud.google.com/sdk/docs/install#windows</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Docker (Ubuntu 20.04)</td>
<td>Yes</td>
<td>‘”</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Docker (Mac)</td>
<td>Yes</td>
<td>“”</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Raspbian</td>
<td>Yes?</td>
<td>https://www.dckap.com/blog/how-to-make-a-proper-connect-between-raspberry-pi-and-gcloud-iot/</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Android</td>
<td>No</td>
<td>~Can utilize publishing and subscribing features through third party</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>iOS</td>
<td>No</td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

**Hardware Architectures**

Can it run on these CPUs?

| **CPU Family**                | **Yes/No** | **Known Limitations** |
|-------------------------------|------------|-----------------------|
| ARM                           |            |                       |
| INTEL                         | Yes        |                       |
| AMD                           | Yes        |                       |
| Embedded (Eiger, Aruix, etc.) |            |                       |

**Hardware Needs**

Create this table for all OS and CPU combinations tested

**EX: OS\_A on CPU\_B**

&lt;--MAP THIS TO THE EXPERIMENTS COMPLETED FOR YOUR TECHNOLOGY--&gt;

|                               | **CPU**             | **RAM**            | **Hard Disk Memory** |
|-------------------------------|---------------------|--------------------|----------------------|
| Idle                          | 0.13999999999999999 | 92.6               | 10382614528.0        |
| Max Observed Under Load A     | 77.2                | 98.7               | 10388865024          |
| Average Observed Under Load A | 17.043999999999997  | 90.60399999999998  | 10382843412.48       |
| Max Observed Under Load B     | 88.8                | 67.2               | 10389282816          |
| Average Observed Under Load B | 38.15               | 44.731249999999996 | 10388794624.0        |

**Language Support**

Are there commercially available libraries for the following languages?

<table>
<thead>
<tr class="header">
<th><strong>Programming Language</strong></th>
<th><strong>Yes/No</strong></th>
<th><strong>Link(s)</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Python</td>
<td>Yes</td>
<td><p><a href="https://www.youtube.com/watch?v=f5DOsB7Nlw0&amp;t=254s">https://www.youtube.com/watch?v=f5DOsB7Nlw0&amp;t=254s</a></p>
<p><a href="https://www.youtube.com/watch?v=UKAmZBrR300">https://www.youtube.com/watch?v=UKAmZBrR300</a></p></td>
</tr>
<tr class="even">
<td>JavaScript</td>
<td>Yes</td>
<td>https://cloud.google.com/pubsub/docs/reference/libraries</td>
</tr>
<tr class="odd">
<td>C</td>
<td>No</td>
<td></td>
</tr>
<tr class="even">
<td>C++</td>
<td>Yes</td>
<td>https://cloud.google.com/pubsub/docs/reference/libraries</td>
</tr>
<tr class="odd">
<td>C#</td>
<td>Yes</td>
<td>https://cloud.google.com/pubsub/docs/reference/libraries</td>
</tr>
<tr class="even">
<td>Objective-C</td>
<td>No</td>
<td></td>
</tr>
<tr class="odd">
<td>Java</td>
<td>Yes</td>
<td>https://cloud.google.com/pubsub/docs/reference/libraries</td>
</tr>
<tr class="even">
<td>Kotlin</td>
<td>Yes?</td>
<td>https://codelabs.developers.google.com/codelabs/cloud-spring-cloud-gcp-kotlin#1</td>
</tr>
<tr class="odd">
<td>Swift</td>
<td>No</td>
<td></td>
</tr>
<tr class="even">
<td>Go</td>
<td>Yes</td>
<td>https://cloud.google.com/pubsub/docs/reference/libraries</td>
</tr>
<tr class="odd">
<td>Ruby</td>
<td>Yes</td>
<td>https://cloud.google.com/pubsub/docs/reference/libraries</td>
</tr>
<tr class="even">
<td>PowerShell</td>
<td>Yes</td>
<td>https://cloud.google.com/pubsub/docs/building-pubsub-messaging-system</td>
</tr>
<tr class="odd">
<td>Perl</td>
<td>Yes?</td>
<td>Some references to perl here: https://github.com/sdondley/WebService-Google-Client</td>
</tr>
<tr class="even">
<td>Rust</td>
<td>Yes</td>
<td>Documentation here: https://docs.rs/google-pubsub1/2.0.0+20210322/google_pubsub1/</td>
</tr>
<tr class="odd">
<td>Elixir</td>
<td>Yes?</td>
<td>Documentation: https://paveltyk.medium.com/watch-google-bucket-with-elixir-google-cloud-storage-pubsub-elixir-broadway-500279375739</td>
</tr>
</tbody>
</table>
