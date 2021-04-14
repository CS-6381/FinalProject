
## CAP analysis:


The aim is to conduct an experiment which measures the Consistency/Availability for a given datastore in clusters.

First we need to set up a multi-node cluster
We can do this by specifically targetting a single key/id, and constantly updating its value (with a single Writer).
We then want to check the consistency/differences of multiple Readers across different nodes in the cluster.



If applicable, set up a multi-cluster server for the data-store. (eg: min N=2 nodes)

## Writer
The Writer should be insert/update in a while loop their current time-stamp with a space, then the sample1 payload from the samples provided in the /samples dir.
The writer should be writing to the same known key repeatedly (ex: id: "1", payload: "<timestamp> <sample_data>")

Set up an additional writer in the same format, always writing to the same key "2".
Set up an additional writer in the same format, always writing to the same key "3".

There will be 3 writers in total (writer's 2 and 3 are just creating work-loads for the replication/coordinators to be 'stressed')

## Reader
Set up multiple Readers aiming for them to target different Nodes on the cluster.
scale with the number of nodes in the cluster: N=1 thru N=10 would suffice.

Have the Reader take their current time-stamp, and then get/read request the data-store. the time-stamp from the stored message. Parse the time-stamp from the payload, and take the time delta (eg: reader time-stamp - writer time-stamp)

All readers should read from key "1".

Each reader should collect 1,000 datapoints each (10,000 if the collection is timely)

If its unreasonable to isolate which nodes to target for the reader/writer, then still set up 10*N Readers (so up to 100 readers, to 3 writers on a 10 node cluster), assuming there will be some load balancing across the nodes.

We will collect the different reader data in separate data-sets (just exports of 'write time-stamp', 'read time-stamp', and delta will be enough to collect, per each reader).

The aim is to find variance/'stutter' that is different across the different readers, depending on which nodes they are reading from, indicating the load is not synchronized across the cluster yet.
We can measure the relative delays/progressions for different data stores to evaluate their CAP spectrum.

The expectation is that the readers will have different graphs/shapes in the plot of write_time(look-up) vs. read_time(local), which we can use to draw conclusions regarding the focus on Consistency vs. Availability.



Some doc that may be useful for comparison, about how it may be feasible to specifically isolate which nodes you want to target for the read/write programs.
https://stackoverflow.com/questions/27077701/how-cassandra-select-the-node-to-send-request

Additional document on cluster configuration for example.
https://docs.datastax.com/en/cassandra-oss/2.1/cassandra/architecture/architectureClientRequestsAbout_c.html
