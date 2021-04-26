# Testing Process Explained

For our experiments, due to resource constraints we only had access to 3 nodes, one of which could not perform read or write actions.

## CAP
Tests were ran on 2 nodes, writing and reading to 1 node:

Node 1 : Cluster
- head of cluster, therefore no write and read operations allowed directly from it

Node 2: 3 writers
- 1 writer writing to key 1
- 1 writer writing to key 2
- 1 writer writing to key 3

Node 3: 2 readers
- 1 reader reading from key 1: [reader1.csv](cap/reader1.csv)
- Another reader reading from key 1: [reader2.csv](cap/reader2.csv)

### CSV Snapsot (reader1.csv)
| Label Identifying Reader Id | Writer Message timestamp | Read Start Timestamp | Read Finish Timestamp | 
| --------------------------- | ------------------------ | -------------------- | --------------------- |
| reader1                     | 06:30:25.265709          | 06:30:25.265912      | 06:30:25.266356       | 
| reader1                     | 06:30:25.268393          | 06:30:25.268610      | 06:30:25.269029       | 
| reader1                     | 06:30:25.269158          | 06:30:25.269475      | 06:30:25.269872       | 


## Performance
Due to resource constraints, we are able to run the following configurations:

| Writer Machines | Writer Instances | Reader Machines | Reader Instances |
| --- | --- | --- | --- |
| 1 | 1 | 0 | 0 |
| 0 | 0 | 1 | 1 |


Using the following instructions (using all samples 1 - 5):

- run all writes over a range of keys 1-10000 (each payload being indexed by a unique/iterable): [1writer_range_keys.csv](performance/1writer/1writer_range_keys.csv)
- run all reads over the same given range (looking up each key once, for each record written): [1reader_range_keys.csv](performance/1reader/1reader_range_keys.csv)
- run with all writes targeting the same key (eg: 1)[1writer_same_key.csv](performance/1writer/1writer_same_key.csv)
- run all reads targeting the same key (eg:1)[1reader_same_key.csv](performance/1reader/1reader_same_key.csv)


### CSV Snapsot (1reader_range_keys.csv)
| reader_id | writer_id | key | start_time         | end_time           | delta_time             |
| ----------| --------- | --- | ------------------ | ------------------ | ---------------------- |
| reader1   | 0         | 0   | 1619406823.3976188 | 1619406823.3978367 | 0.00021791458129882812 |
| reader1   | 0         | 1   | 1619406823.3978484 | 1619406823.3982496 | 0.0004012584686279297  |
| reader1   | 0         | 2   | 1619406823.3982606 | 1619406823.3986838 | 0.00042319297790527344 |


## Calculations

[Link to Cap Results](cap/results.csv)
[Link to Performance Results](performance/results.csv)
