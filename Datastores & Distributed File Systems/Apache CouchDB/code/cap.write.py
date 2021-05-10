import couchdb
import random
import time
import datetime

couch = couchdb.Server('http://admin:stellawang@18.224.62.99/')
db = couch['test']

f = open('write.txt', "a")

for i in range(1,1001):
 first_time = datetime.datetime.now()
 couch = couchdb.Server('http://admin:stellawang@18.224.62.99/')
 db = couch['test']
 next_time = datetime.datetime.now()
 db.save({'content': 'abababababababababab'})
 f.write(str((next_time-first_time).total_seconds()) + ' ')
 f.close()
