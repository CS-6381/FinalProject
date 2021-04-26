import os, sys, datetime, time, string, random, uuid, csv
import sys
sys.path.append('/opt/couchbase/lib')

# needed for any cluster connection
from couchbase.cluster import Cluster, ClusterOptions
from couchbase_core.cluster import PasswordAuthenticator

# needed to support SQL++ (N1QL) query
from couchbase.cluster import QueryOptions
import couchbase.subdocument as SD

from timestamp import *

# get a reference to our cluster
cluster = Cluster('couchbase://172.31.2.240', ClusterOptions(
  PasswordAuthenticator('Administrator', 'password')))

print("Connected to cluster") 

# get a reference to our sample data bucket to write to 
cb = cluster.bucket('sample_data')

# get sample data file
f = open('data/sample1.txt', 'r')
s1_content = f.read()
f.close()

# create documents for sample data
ctime = getDateTime()
document1 = {"payload": s1_content, "timestamp": ctime}


def cap_writer_1():
  count = 0
  while count <= 50000:
    currTime = gethms()
    #cb.mutate_in("1", [SD.upsert("timestamp", currTime)])
    document1 = {"payload": s1_content, "timestamp": currTime}
    cb.upsert("2", document1)
    count+=1


cap_writer_1()
