import os, sys, datetime, time, string, random, uuid, csv
import sys
sys.path.append('/opt/couchbase/lib')

# needed for any cluster connection
from couchbase.cluster import Cluster, ClusterOptions
from couchbase_core.cluster import PasswordAuthenticator

# needed to support SQL++ (N1QL) query
from couchbase.cluster import QueryOptions
import couchbase.subdocument as SD

# get a reference to our cluster
cluster = Cluster('couchbase://172.31.2.240', ClusterOptions(
  PasswordAuthenticator('Administrator', 'password')))

print("Connected to cluster")

# get a reference to our sample data bucket to write to 
cb = cluster.bucket('sample_data')

# get files with sample data
f = open('data/sample1.txt', 'r')
s1_content = f.read()
f.close()

# insert/update key 1
cb.mutate_in("document_1", [SD.upsert("1",s1_content)])
print("updated")

# read key 1
cb.lookup_in("document_1",
            [SD.get("1")])
print("read")

