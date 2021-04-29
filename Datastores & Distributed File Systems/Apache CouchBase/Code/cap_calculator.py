import os, sys, datetime, time, string, random, uuid, csv, pandas
import sys
import statistics
import numpy as np
sys.path.append('/opt/couchbase/lib')
from timestamp import *

reader1 = 'results/cap/reader1.csv'
reader2 = 'results/cap/reader2.csv'

reader1_deltas = []
reader2_deltas = []
final_list = []
reader_list = [[reader1, reader1_deltas], [reader2, reader2_deltas]]


# read csv files, capture and calculate deltas
def get_latency_all():
    for reader in reader_list: 
        df = pandas.read_csv(reader[0])
        for index, rows in df.iterrows():
            start =(df['Read Start Timestamp'][index])
            end  = (df['Read Finish Timestamp'][index])
            delta = convert_seconds(str(end)) -  convert_seconds(str(start))
            #latency = round(delta * 10000)
            #final_list.append(latency)
            final_list.append(delta)

def get_avg(some_list):
    return sum(some_list) / len(some_list)

def get_min(some_list):
    return min(np.array(some_list))

def get_max(some_list):
    return max(some_list)

def get_sd(some_list):
    return statistics.stdev(some_list)


def create_csv(some_list):
    columns = ['Metric', 'value']
    with open ('results/cap/results.csv', 'w') as f:
        write = csv.writer(f)
        write.writerow(columns)
        write.writerow(['Read Latency Min', get_min(final_list)])
        write.writerow(['Read Latency Max', get_max(final_list)])
        write.writerow(['Read Latency Average', get_avg(final_list)])
        write.writerow(['Read Latency Standard Deviation', get_sd(final_list)])


get_latency_all()
create_csv(final_list)
   



