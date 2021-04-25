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

f = open('data/sample2.txt', 'r')
s2_content = f.read()
f.close()

f = open('data/sample3.txt', 'r')
s3_content = f.read()
f.close()

f = open('data/sample4.txt', 'r')
s4_content = f.read()
f.close()

f = open('data/sample5.txt', 'r')
s5_content = f.read()
f.close()

# create documents for sample data
document1 = {"payload": s1_content}
document2 = {"payload": s2_content}
document3 = {"payload": s3_content}
document4 = {"payload": s4_content}
document5 = {"payload": s5_content}


def run_performance_write(sample):
    count = 0
    while(count <= 10000):       
        doc = "document" + str(sample)
        start_time = getDateTime()
        cb.upsert(str(sample), doc)
        end_time = getDateTime()
        delta = end_time - start_time
        count = count+1
        print(start_time, end_time, delta)
        list = [0, 1, 1, start_time, end_time, delta]
        return list
        


def run_performance_read(sample):
    count = 0
    while(count <= 10000):       
        start_time = getDateTime()
        cb.get(str(sample), quiet=True)
        end_time = getDateTime()
        delta = end_time - start_time
        count= count+1
        print(start_time, end_time, delta)


f = open("results/test.txt", "w")
result = run_performance_write(1)
with open ('test.txt', 'w') as fo:
    fo.write(','.join([str(n) for n in result]))

# def csv(key, reader_id, writer_id, start_time, end_time, delta_time):
#     with open('persons.csv', 'wb') as csvfile:
#     filewriter = csv.writer(csvfile, delimiter=',',
#                             quotechar='|', quoting=csv.QUOTE_MINIMAL)
#     filewriter.writerow(['Name', 'Profession'])
#     filewriter.writerow(['Derek', 'Software Developer'])
#     filewriter.writerow(['Steve', 'Software Developer'])
#     filewriter.writerow(['Paul', 'Manager'])



