# Base Experiment (MQ)

This experiment is an extension of the [Base experiment](./Base.md) that is specific to Datastore technologies.

## Qualitative Data

Fill in with information you discover about the given Data Store.
Please include any other key characteristics of the data store which amy not be outlined.

| Metric | Value |
| --- | --- |
| Use Case | Caching, Mobile data management, Session management, Mainframe offload, User profile store, Source-of-truth data stores, etc [More Uses cases](https://www.couchbase.com/solutions)| 
| CAP Theorem Evaluation | Availability: If one Index-Service node is lost, the other continues to provide access to replicated indexes. High Performance: If original and replica copies are available, incoming queries are load-balanced across them. The trade off is Eventual Consistency  [More detailed Couchbase CAP information](https://docs.couchbase.com/server/current/learn/services-and-indexes/indexes/index-replication.html)|  
| Database/Structure Hierarchy | The data model is based on JSON. Documents represent a single instance of an object in application code - considered to be the equivalent of a row in a relational table. Attributes of a document are equivalent to a column. The scheme is dynamic, meaning that document structures can vary. This allows for flexibility and efficiency. [More information on the document data model](https://docs.couchbase.com/server/current/learn/data/document-data-model.html) | 
| Replication / Clustering Availability | Availability: Couchbase provides high availability for reading an writing data through a variety of features. For writing, the ability to get data off a single node as quickly as possible is aparount to avoid any data loss due to falure of that individual node. Replication: Using the cross datacenter replication (XDCR) capability you can set up replication of data between clusters. XDCR helps protect against data center failures and also helps maintain data locality in globally distributed mission critical applications. [Couchbase Replication and Clustering Basics](https://docs.couchbase.com/server/current/learn/clusters-and-availability/clusters-and-availability.html) - [More information on Couchbase replication and clustering](https://docs.couchbase.com/server/5.1/architecture/high-availability-replication-architecture.html)  | 
| Syntax/Query Language Support | Couchbase uses the N1QL "nickel" query language. N1QL is an expressive, powerful and complete SQL dialiect for querying, transforming, and maniuplating json data. It is also based on SQL. [More information on N1QL](https://docs.couchbase.com/server/current/n1ql/query.html)| 

