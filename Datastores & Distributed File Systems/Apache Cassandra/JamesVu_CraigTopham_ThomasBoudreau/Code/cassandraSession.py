# Imports
import os, sys, datetime, time, string, random, uuid, csv, subprocess
from datetime import datetime as dt
# pip3 install cassandra-driver
from cassandra.cluster import Cluster
from pathlib import Path
from cassandra.cqlengine import connection
from cassandra.policies import DCAwareRoundRobinPolicy
from cassandra.auth import PlainTextAuthProvider
from flask import *
app = Flask(__name__)

# Connect to Cassandra.
clusterID = 'localhost'
print("Connecting to Cluster with clusterID: " + clusterID)
cluster = Cluster([clusterID])
session = cluster.connect('cs6381finalprojectks1')
connection.register_connection(clusterID, session = session)
print("Connection complete")

@app.route('/returnSession')
def returnSession():
    print("Returning session ...")
    return session

if __name__=="__main__":
	app.run(debug=True, port=5000)