# Have Cassandra running and run this to create or drop table.
# "python3 table.py c {{uuid or int depending on use}}" = create table with id of use type
# "python3 table.py d" = drop table

# Imports
import os, sys, datetime, time, string, random, uuid, csv, subprocess
from datetime import datetime as dt
# pip3 install cassandra-driver
from cassandra.cluster import Cluster
from pathlib import Path

# Connect to Cassandra.
cluster = Cluster()
session = cluster.connect('cs6381finalprojectks1')
cdOption = sys.argv[1]

# Create table query
if cdOption == 'c':
    print("Creating table ...")
    query = "Create Table table1(id " + sys.argv[2] + " Primary Key, message text);"
    print(query)
    try:
        session.execute(query)
    except Exception as e:
        print("Create Exception: " + str(e))

# Drop table query
if cdOption == 'd':
    print("Dropping table ...")
    query = "drop table table1;"
    print(query)
    try:
        session.execute(query)
    except Exception as e:
        print("Drop Exception: " + str(e))