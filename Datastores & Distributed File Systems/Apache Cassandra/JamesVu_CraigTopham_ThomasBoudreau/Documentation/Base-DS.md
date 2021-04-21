**Base Experiment (MQ)**

This experiment is an extension of the [Base
experiment](https://github.com/CS-6381/FinalProject/blob/main/DesignOfExperiments/Base.md) that
is specific to DS technologies.

**Qualitative Data**

TODO: Change this These metrics are inspired by [Yahoo! Cloud Serving
Benchmark (YCSB)](https://github.com/brianfrankcooper/YCSB/wiki). Fill
in with information you discover about your chosen DS.

<table>
<thead>
<tr class="header">
<th><strong>Metric</strong></th>
<th><strong>Value</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Centricity (data-centric or message-centric)</td>
<td><a href="https://cassandra.apache.org/">https://cassandra.apache.org/</a>: Data-centric (stores data)</td>
</tr>
<tr class="even">
<td>Connection (machine-to-machine or point-to-point)</td>
<td><p><a href="https://cassandra.apache.org/">https://cassandra.apache.org/</a>: Point-to-point. Data replicated to nodes.</p>
<p><a href="https://www.geeksforgeeks.org/application-connectivity-with-cassandra/">https://www.geeksforgeeks.org/application-connectivity-with-cassandra/</a>: Database can be used on the same computer.</p></td>
</tr>
<tr class="odd">
<td>Underlying Architecture (decentralized or hub-and-spoke)</td>
<td><a href="https://cassandra.apache.org/">https://cassandra.apache.org/</a>: Decentralized, no single place of failure</td>
</tr>
<tr class="even">
<td>Protocol</td>
<td><p><a href="https://stackoverflow.com/questions/28127182/data-transmission-between-nodes-and-client-cassandra">https://stackoverflow.com/questions/28127182/data-transmission-between-nodes-and-client-cassandra</a>: Gossip</p>
<p><a href="https://en.wikipedia.org/wiki/Gossip_protocol">https://en.wikipedia.org/wiki/Gossip_protocol</a>: Gossip allows data to spread to all group members.</p></td>
</tr>
<tr class="odd">
<td>Transport(s)</td>
<td><a href="https://cassandra.apache.org/doc/latest/faq/">https://cassandra.apache.org/doc/latest/faq/</a>: Ports are TCP.</td>
</tr>
<tr class="even">
<td>Data Serialization</td>
<td><a href="http://www.diva-portal.org/smash/get/diva2:839521/FULLTEXT02">http://www.diva-portal.org/smash/get/diva2:839521/FULLTEXT02</a>: SQL is limited by table format and the need to change table rules when changing data structure. Data serialization alleviates this issue by treating the database as a file storage system that stores data in binary form in columns with unique ID’s. This allows queries to read fewer columns, thus dropping overhead. Apache Avro, a serialization library, allows the user to define JSON-based data structures in serialization.</td>
</tr>
<tr class="odd">
<td>Supports Queuing</td>
<td><a href="https://medium.com/@anirudhkanabar/clustering-order-in-cassandra-how-to-achieve-ordering-of-data-in-cassandra-f52e8a73d5d5">https://medium.com/@anirudhkanabar/clustering-order-in-cassandra-how-to-achieve-ordering-of-data-in-cassandra-f52e8a73d5d5</a>: Clustering order feature allows queries to be sorted according to their given parameter</td>
</tr>
<tr class="even">
<td>Data Type Representation</td>
<td><a href="https://cassandra.apache.org/doc/latest/cql/types.html">https://cassandra.apache.org/doc/latest/cql/types.html</a>: CQL (Cassandra Query Language) supports many native types (e. g. BLOB, BOOLEAN, DATE, FLOAT, INT, TEXT, TIMESTAMP, UUID, VARCHAR, etc.).</td>
</tr>
<tr class="odd">
<td>QoS Parameters</td>
<td><a href="https://docs.datastax.com/en/dse/5.1/cql/cql/cql_using/useQueryColumnsSort.html">https://docs.datastax.com/en/dse/5.1/cql/cql/cql_using/useQueryColumnsSort.html</a>: You can set the LIMIT or PARTITION LIMIT parameter to control how much data you get back with a SELECT query.</td>
</tr>
<tr class="even">
<td>Supports Dynamic Discovery</td>
<td><a href="https://stackoverflow.com/questions/46643437/cassandra-read-performance">https://stackoverflow.com/questions/46643437/cassandra-read-performance</a>: Cassandra’s writing performance is greater than its reading performance.</td>
</tr>
<tr class="odd">
<td>Communication Patterns</td>
<td><a href="https://cassandra.apache.org/doc/latest/faq/">https://cassandra.apache.org/doc/latest/faq/</a>: Cassandra uses 7000 for cluster communication, 9042 for native protocol clients, and 7199 for JMX. Configure native procol and internode communication ports in Cassandra Configure File (<a href="https://cassandra.apache.org/doc/latest/configuration/cassandra_config_file.html#cassandra-yaml">https://cassandra.apache.org/doc/latest/configuration/cassandra_config_file.html#cassandra-yaml</a>) and JMX port in cassandra-env.sh. Ports are TCP.</td>
</tr>
<tr class="even">
<td>Abstraction Layer</td>
<td><p><a href="https://www.geeksforgeeks.org/features-of-cassandra/">https://www.geeksforgeeks.org/features-of-cassandra/</a>: Cassandra uses CQL, which provides an abstraction layer to hide structure implementation.</p>
<p><a href="https://www.datastax.com/resources/video/datastax-accelerate-2019-casquatch-open-source-java-abstraction-layer-cassandra">https://www.datastax.com/resources/video/datastax-accelerate-2019-casquatch-open-source-java-abstraction-layer-cassandra</a>: Casquatch is a database abstraction layer with code for streamlining Cassandra works that includes load balancing, connection pooling, and geo-redundancy and uses the concept of POJO instead of CQL.</p></td>
</tr>
<tr class="odd">
<td>Up-front Complexity</td>
<td><p><a href="https://cassandra.apache.org/">https://cassandra.apache.org/</a>: Decentralized. Data replicated to nodes.</p>
<p><a href="https://www.quora.com/Is-Cassandra-hard-to-learn">https://www.quora.com/Is-Cassandra-hard-to-learn</a>: Setup not too difficult. The focus is on your project database design.</p>
<p><a href="https://en.wikipedia.org/wiki/Apache_Cassandra">https://en.wikipedia.org/wiki/Apache_Cassandra</a>: Free, open source</p>
<p><a href="https://www.youtube.com/watch?v=z0fPRyR12KA">https://www.youtube.com/watch?v=z0fPRyR12KA</a>: Setup can be not too difficult (e. g. on Ubuntu).</p></td>
</tr>
<tr class="even">
<td>Large Implementations</td>
<td><p><a href="https://www.quora.com/How-much-data-can-a-single-node-in-a-Cassandra-cluster-handle-Are-there-configuration-settings-to-set-the-data-size-limit-the-data-size-on-the-node/https://stackoverflow.com/questions/4775388/how-much-data-per-node-in-cassandra-cluster">https://www.quora.com/How-much-data-can-a-single-node-in-a-Cassandra-cluster-handle-Are-there-configuration-settings-to-set-the-data-size-limit-the-data-size-on-the-node/https://stackoverflow.com/questions/4775388/how-much-data-per-node-in-cassandra-cluster</a>: Under 1 TB per node</p>
<p><a href="https://stackoverflow.com/questions/7190573/cassandra-node-limitations">https://stackoverflow.com/questions/7190573/cassandra-node-limitations</a>: A row must fit 1 node.</p>
<p><a href="https://docs.datastax.com/en/cql-oss/3.x/cql/cql_reference/refLimits.html#:~:text=Table%20%2F%20CF%20name%20length%3A%2048,65535%20(2%2016%2D1)">https://docs.datastax.com/en/cql-oss/3.x/cql/cql_reference/refLimits.html#:~:text=Table%20%2F%20CF%20name%20length%3A%2048,65535%20(2%2016%2D1)</a>: CQL has some limits: 2 GB max per column or blob, 48 characters max per table name, 65535 parameters max per query, etc.</p></td>
</tr>
</tbody>
</table>
