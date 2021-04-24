import os, sys, datetime, time, string, random, uuid, csv, subprocess, requests
from pathlib import Path

# needed for any cluster connection
from couchbase.cluster import Cluster, ClusterOptions
from couchbase_core.cluster import PasswordAuthenticator

# needed to support SQL++ (N1QL) query
from couchbase.cluster import QueryOptions

# get a reference to our cluster
cluster = Cluster('couchbase://172.31.2.240', ClusterOptions(
  PasswordAuthenticator('Administrator', 'password')))

print("Connected to cluster")

# get a reference to our sample data bucket to write to 
cb = cluster.bucket('sample_data')

# get files
f = open('data/sample1.txt', 'r')
s1_content = f.read()
f.close()

#

# insert/update key 1
collection.mutate_in("1", [SD.upsert(s1_content)])
print("updated")
