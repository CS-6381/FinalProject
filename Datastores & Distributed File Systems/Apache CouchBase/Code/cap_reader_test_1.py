import os, sys, datetime, time, string, random, uuid, csv
import sys
sys.path.append('/opt/couchbase/lib')

# needed for any cluster connection
from couchbase.cluster import Cluster, ClusterOptions
from couchbase_core.cluster import PasswordAuthenticator

# needed to support SQL++ (N1QL) query
from couchbase.cluster import QueryOptions
import couchbase.subdocument as SD

from couchbase.collection import MutateInOptions

from timestamp import *

# get a reference to our cluster
cluster = Cluster('couchbase://172.31.2.240', ClusterOptions(
  PasswordAuthenticator('Administrator', 'password')))

print("Connected to cluster") 

# get a reference to our sample data bucket to write to 
bucket = cluster.bucket('sample_data')
cb = bucket.default_collection()

# get sample data file
f = open('data/sample1.txt', 'r')
s1_content = f.read()
f.close()

# create documents for sample data
document1 = {"payload": s1_content}



def run_cap_reader1():
    columns = ['Label Identifying Reader Id','Writer Message timestamp', 'Read Start Timestamp', 'Read Finish Timestamp']
    with open ('results/cap/reader1.csv', 'w') as f:
      write = csv.writer(f)
      write.writerow(columns)
      count = 0
      while count <= 1: 
        cb.get("1", quiet=True)
        before_time = getDateTime()
        writer_timestamp = cb.mutate_in(
                "1", [SD.get("timestamp")])
        after_time = getDateTime()
        ts = writer_timestamp.content_as[str](0)
        convert_gethms(ts)
        list = ["reader1",ts, before_time, after_time]
        write.writerow(list)
        count+=1


run_cap_reader1()