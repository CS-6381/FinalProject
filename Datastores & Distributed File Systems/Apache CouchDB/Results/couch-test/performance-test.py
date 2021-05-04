import os, sys, datetime, time, string, random, uuid, csv
import couchdb
from timestamp import *

couch_server = couchdb.Server('http://admin:admin@127.0.0.1:5984/')


# doc_id, doc_rev = db.save({'type': 'Person', 'name': 'John Doe'})
# print("saved and read: ", db[doc_id])

documents = []
for i in range(1,6):
    f = open('data/sample{}.txt'.format(i), 'r')
    content = f.read()
    f.close()
    print('collected sample ', i)
    documents.append(content)

print('document list length: ', len(documents))

columns = ['reader_id', 'writer_id', 'key', 'start_time', 'end_time', 'delta_time']

def write_diff_keys():
    print("start 1 writer write with different keys")
    for j in range(1,len(documents)):
        content = documents[j]
        try:
            db = couch_server.create('performance-test-sample{}'.format(j))
            print("successfully created database, ", db)
        except:
            db = couch_server['performance-test-sample{}'.format(j)]
            print('connected existed database')
        
        with open ('results/performance/1writer/1writer_range_keys_{}.csv'.format(j), 'w') as f:
            write = csv.writer(f)
            write.writerow(columns)

            for i in range(1,10001):
                if (i%1000 == 0):
                    print('done {}/{}'.format(i,10000))
                document = {'_id':str(i), 'payload': content}
                #print(document)
                start = time.time()
                db.save(document)
                end = time.time()
                delta = end - start
                lst = [0,1,i,start,end,delta]
                write.writerow(lst)
            print("done with sample ", j)

def read_diff_keys():
    print("start 1 reader read with different keys")
    for j in range(len(documents)):
        db = couch_server['performance-test-sample{}'.format(j)]
        print('connected existed database')
        with open ('results/performance/1reader/1reader_range_keys_{}.csv'.format(j), 'w') as f:
                write = csv.writer(f)
                write.writerow(columns)
                for i in range(1,10001):
                    if (i%1000 == 0):
                        print('done {}/{}'.format(i,10000))
                    #print(document)
                    start = time.time()
                    doc = db[str(i)]
                    end = time.time()
                    delta = end - start
                    lst = [0,1,i,start,end,delta]
                    write.writerow(lst)
                print("done with sample ", j)
#write_diff_keys()
read_diff_keys()