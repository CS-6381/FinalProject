| Category | Kafka |
| --- | --- |
| Overview Basics | <ul><li>Service bus to connect heterogeneous applications</li></ul><ul><li>Isolates producers from consumers</li></ul><ul><li>Producer Centric – does not block producers</li></ul> |
| Implementation Basics | <ul><li>3 Main Components – Publisher, Cluster/Manager, Subscriber</li></ul><ul><li>Partitioning and stream of event packets containing data and transforming them into durable message brokers with cursors, supporting batch consumers that may be offline, or online consumers that want messages at low latency</li></ul><ul><li>Provides longer retention of messages (even after consumption) allowing re-consumption</li></ul><ul><li>Metadata stored at consumer level (not server level like other MQS) </li></ul><ul><li>No “master”, brokers treated as peers</li></ul><ul><li>Metadata of brokers maintained in Zookeeper(??later versions too??) </li></ul> |
| Use Cases | <ul><li>Distributed Pub/Sub Messaging system</li></ul><ul><li>Monitoring Data from Distributed Applications</li></ul><ul><li>Log aggregation services</li></ul><ul><li>Highly scalable</li></ul>|
| Features | <ul><li>Guarantees 0% data loss</li></ul><ul><li>2 million writes / second</li></ul><ul><li>Optimized for data ingestion in real time</li></ul>|
| Scalability | <ul><li>Highly scalable</li></ul><ul><li>Adding consumers – doesn’t affect performance or require downtime</li></ul> |
| Failure Response | <ul><li>Resilient – creates replicas for failover</li></ul> |
| Message Consumption Model | <ul><li>PULL</li></ul> |
| Flexibility | <ul><li>General purpose Pub/Sub capability</li></ul> |
| Broker | <ul><li>Runs a cluster handling incoming high volume data streams</li></ul> |
| Message Delivery | <ul><li>Never Delivered</li></ul><ul><li>May be redelivered</li></ul><ul><li>Delivered Once</li></ul> |
| Message Ordering | <ul><li>Not known for message ordering</li></ul><ul><li>Need to utilize consistent hash exchange or sharding plugin</li></ul> |
| Storage Architecture | <ul><li>Records stored in log entry</li></ul><ul><li>Records stored as topics</li></ul> |
| Consumption Tracking | <ul><li>Does not track consumption</li></ul><ul><li>Consumers required to keep track of cursor</li></ul> |
| Record Retention Policy | <ul><li>Default – 7 days</li></ul><ul><li>Indefinite dependent on disk available</li></ul> |
| Record Replay | <ul><li>Yes</li></ul> |
| Data Transmission Protocols | <ul><li>Binary over TCP</li></ul><ul><li>Client initiates socket with queues, writes messages, waits for ack</li></ul> |
| Delivery Guarantees | <ul><li>at-most-once</li></ul><ul><li>at-least-once, and </li></ul><ul><li>also high-throughput exactly once semantics specifically aimed at end-to-end stream processing use cases</li></ul> |
| Replication | <ul><li>Synchronous – producer identifies lead from ZK and publishes – Written to log of lead replica and all followers of lead start pulling the message – order is ensured</li></ul><ul><li>Asynchronous – lead replica sends ACK to client w/o waiting for acknowledgement of receipt by other brokers</li></ul><ul><li>Resilient, durable messages with automatic recovery</li></ul> |
| Known For | <ul><li>Publisher Centric<ul><li>High-Volume Publishers<ul><li>On or Offline Consumers<ul><li>Extremely high throughput with consistent latencies<ul><li>Allows consumers to re-read messages |
| Other Features | <ul><li>Kafka Streams – helps to filter and transform data</li></ul><ul><li>Message Compression – GZIP/Snappy used to compress by producer</li></ul><ul><li>Message Batching</li></ul><ul><li>Must write separate publisher and subscribers – not embedded in application</li></ul> |
| Implementation Details | <ul><li>Backbone is message caching and storing on filesystem</li></ul><ul><li>Data is immediately written to OS kernal page</li></ul><ul><li>Caching/flushing of data to disk is configurable</li></ul> |
