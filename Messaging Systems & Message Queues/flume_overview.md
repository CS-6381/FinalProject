| Category | Flue |
| --- | --- |
| Overview Basics | <ul><li>Get streaming data from multiple sources for storage and analysis in HDFS</li></ul><ul><li>collects, aggregates, moves log data from many different sources to a centralized data store. </li></ul><ul><li>data sources are customizable - network traffic, social-media-generated, email messages, etc. </li></ul> |
| Implementation Basics | <ul><li>Sources/Inputs of Data </li></ul><ul><li>Sinks/Outputs of Data</li></ul><ul><li>Agent – daemon for 1+ channels</li></ul><ul><li>Channel – holding area as events are passed between source and sink</li></ul><ul><li>Interceptors – sit between source and channel – process events with UUID, host info, timestamp, regex filtering, etc. </li></ul> |
| Use Cases | <ul><li>Simple collection/aggregation of log data</li></ul><ul><li>Process Transaction logs in application/web servers</li></ul> |
| Features | <ul><li>Flexible and simple based on streaming data flows</li></ul><ul><li>Query processing engine to transform data before reaching sink</li></ul><ul><li>Efficiently collect, aggregate, and move large </li></ul>amounts of data from many sources to centralized store</li></ul> |
| Scalability | <ul><li>Not scalable itself</li></ul><ul><li>Adding Consumers – requires pipeline topology design changes (downtime) </li></ul> |
| Failure Response | <ul><li>Not resilient – lose data if node fails</li></ul><ul><li>Transient Messaging – will lose messages if channel Fails</li></ul>
| Message Consumption Model | <ul><li>PUSH</li></ul> |
| Flexibility | <ul><li>Tightly integrated with Hadoop</li></ul> |
| Broker | <ul><li>Runs </li></ul> |
| Message Delivery | <ul><li>Best Effort – undelivered messages discarded – good for metrics where loss can be tolerated</li></ul><ul><li>Disk Failover – store undeliverable data to local disk<ul><li>End to End (E2E) </li></ul> |
| Message Ordering | <ul><li>Zero ordering guarantees</li></ul> |
| Storage Architecture | <ul><li>Event acts as store until consumed</li></ul> |
| Consumption Tracking | <ul><li>Keeps message in storage until consumed</li></ul> |
| Record Retention Policy | <ul><li>Default is emphemeral</li></ul><ul><li>Durable message subscriptions can be set up with DB with unlimited capacity</li></ul> |
| Record Replay | <ul><li>Yes, but must use File Channel instead of Memory Channel</li></ul> |
| Data Transmission Protocols | <ul><li>Misc. </li></ul> |
| Delivery Guarantees | <ul><li>Guaranteed – both receiver and sender evoke to ensure guaranteed transaction</li></ul><ul><li>Guarantees that the events will reach their destination at least once</li></ul><ul><li>Attemps to only write once</li></ul> |
| Replication | <ul><li>Default – MemoryChannel - uses emphemeral memory based channels – higher throughput but loss</li></ul><ul><li>FileChannel - Durable channel can be set up but no replication and data not available until recovery – Uses write ahead log</li></ul> |
| Known For | <ul><li>Not scalable in comparison to Kafka</li></ul><ul><li>Specifically designed for Hadoop</li></ul><ul><li>Filtering and transforming streams before arriving at sink</li></ul><ul><li>Aggregate data to centralized HDFS or HBase storage</li></ul> |
| Other Features | <ul><li>Source and sink are built-in</li></ul> |
| Implementation Details | 
