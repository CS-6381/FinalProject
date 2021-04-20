# MQ Data Processor

This directory contains a python program for performing calculations on the output of your producer programs.

The program generates two files: latencies.csv and throughput.csv.

The latencies.csv file contains the durations of each request in milliseconds.

Ex output:

```
2002
3003
4004
```

The throughput.csv file contains the throughput at each second of the experiment (messages per second).

Ex output:

```
3
1
2
```

## Usage

`python3 main.py -d csv_dir`

where `csv_dir` is a directory containing producer CSV files.

## Help

Contact [@jmbeach](https://github.com/jmbeach) with questions / concerns.
