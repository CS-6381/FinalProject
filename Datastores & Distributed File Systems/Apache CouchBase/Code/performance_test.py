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
doc_list = [document1, document2, document3, document4, document5]

def write_to_txt_file(result):
    with open ('results/test.txt', 'w') as fo:
        fo.write(','.join([str(n) for n in result]))
        fo.write('\n')

def run_performance_write_same_key():
    columns = ['reader_id', 'writer_id', 'key', 'start_time', 'end_time', 'delta_time']
    with open ('results/performance/1writer/1writer_same_key.csv', 'w') as f:
        write = csv.writer(f)
        write.writerow(columns)
         
        key = 0
        for doc in doc_list:
            count = 0
            
            while count <= 10000:
                start_time = getDateTime()
                cb.upsert(str(key), doc)
                end_time = getDateTime()
                delta = end_time - start_time
                list = [0, 121, key, start_time, end_time, delta]
                write.writerow(list)
                count+=1
            key+=1


def run_performance_read_same_key():
    columns = ['reader_id', 'writer_id', 'key', 'start_time', 'end_time', 'delta_time']
    with open ('results/performance/1reader/1reader_same_key.csv', 'w') as f:
        write = csv.writer(f)
        write.writerow(columns)
         
        key = 1
        for doc in doc_list:
            count = 0
            while count <= 10000:
                start_time = getDateTime()
                cb.get(str(key), quiet=True)
                end_time = getDateTime()
                delta = end_time - start_time
                list = [123, 0, key, start_time, end_time, delta]
                write.writerow(list)
                count+=1
            key+=1



def run_performance_write_range_keys():
    columns = ['reader_id', 'writer_id', 'key', 'start_time', 'end_time', 'delta_time']
    with open ('results/performance/1writer/1writer_range_keys.csv', 'w') as f:
        write = csv.writer(f)
        write.writerow(columns)
         
        key = 0
        for doc in doc_list:
            count = 0
            
            while count <= 10000:
                start_time = getDateTime()
                cb.upsert(str(key),doc)
                end_time = getDateTime()
                delta = end_time - start_time
                list = [0, 121, key, start_time, end_time, delta]
                write.writerow(list)
                count+=1
                key+=1

def run_performance_read_range_keys():
    columns = ['reader_id', 'writer_id', 'key', 'start_time', 'end_time', 'delta_time']
    with open ('results/performance/1reader/1reader_range_keys.csv', 'w') as f:
        write = csv.writer(f)
        write.writerow(columns)
         
        key = 0
        for doc in doc_list:
            count = 0
            
            while count <= 10000:
                start_time = getDateTime()
                cb.get(str(key), quiet=True)
                end_time = getDateTime()
                delta = end_time - start_time
                list = [123, 0, key, start_time, end_time, delta]
                write.writerow(list)
                count+=1
                key+=1

run_performance_write_range_keys()
run_performance_read_range_keys()
run_performance_write_same_key()
run_performance_read_same_key()




