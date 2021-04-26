import os, sys, datetime, time, string, random, uuid, csv, pandas
import sys
import statistics
import numpy as np
from math import floor
sys.path.append('/opt/couchbase/lib')
from timestamp import *

reader1 = 'results/performance/1reader/1reader_range_keys.csv'
reader2 = 'results/performance/1reader/1reader_same_key.csv'

writer1 = 'results/performance/1writer/1writer_range_keys.csv'
writer2 = 'results/performance/1writer/1writer_same_key.csv'

reader1_deltas = []
reader2_deltas = []
final_list_r_l = []
final_list_r_tp = []
reader_list = [[reader1, reader1_deltas], [reader2, reader2_deltas]]

writer1_deltas = []
writer2_deltas = []
final_list_w_l = []
final_list_w_tp = []
writer_list = [[writer1, writer1_deltas], [writer2, writer2_deltas]]



# read csv files, capture and calculate deltas
def get_latency_reader():
    for reader in reader_list: 
        df = pandas.read_csv(reader[0])
        for index, rows in df.iterrows():
            start = convert_from_t_dt(df['start_time'][index])
            end  = convert_from_t_dt(df['end_time'][index])
            start1 = convert_seconds(start)
            end1 = convert_seconds(end)
            delta = convert_seconds(str(end)) -  convert_seconds(str(start))
            #latency = round(delta * 1000)
            #final_list_r_l.append(latency)
            final_list_r_l.append(delta)

# read csv files, capture and calculate deltas
def get_latency_writer():
    for writer in writer_list: 
        df = pandas.read_csv(writer[0])
        for index, rows in df.iterrows():
            start = convert_from_t_dt(df['start_time'][index])
            end  = convert_from_t_dt(df['end_time'][index])
            start1 = convert_seconds(start)
            end1 = convert_seconds(end)
            delta = convert_seconds(str(end)) -  convert_seconds(str(start))
            #print(delta)
            #latency = round(delta * 1000)
            #final_list_w_l.append(latency)
            final_list_w_l.append(delta)

def get_throughput_reader():
    for reader in reader_list: 
        df = pandas.read_csv(reader[0])
        for index, rows in df.iterrows():
            start = convert_from_t_dt(df['start_time'][index])
            end  = convert_from_t_dt(df['end_time'][index])
            start1 = convert_seconds(start)
            end1 = convert_seconds(end)
            delta = floor(convert_seconds(str(end)) -  convert_seconds(str(start)))
            final_list_r_tp.append(delta)

def get_throughput_writer():
    for writer in writer_list: 
        df = pandas.read_csv(writer[0])
        for index, rows in df.iterrows():
            start = convert_from_t_dt(df['start_time'][index])
            end  = convert_from_t_dt(df['end_time'][index])
            start1 = convert_seconds(start)
            end1 = convert_seconds(end)
            delta = floor((convert_seconds(str(end)) -  convert_seconds(str(start))) * 1000)
            final_list_w_tp.append(delta)


def get_avg(some_list):
    return sum(some_list) / len(some_list)

def get_min(some_list):
    return min(some_list)

def get_max(some_list):
    return max(some_list)

def get_sd(some_list):
    return statistics.stdev(some_list)


def create_csv():
    columns = ['Metric', 'value']
    with open ('results/performance/results.csv', 'w') as f:
        write = csv.writer(f)
        write.writerow(columns)
        write.writerow(['Write Latency Min', get_min(final_list_w_l)])
        write.writerow(['Write Latency Max', get_max(final_list_w_l)])
        write.writerow(['Write Latency Average', get_avg(final_list_w_l)])
        write.writerow(['Write Latency Standard Deviation', get_sd(final_list_w_l)])
        write.writerow(['Read Latency Min', get_min(final_list_r_l)])
        write.writerow(['Read Latency Max', get_max(final_list_r_l)])
        write.writerow(['Read Latency Average', get_avg(final_list_r_l)])
        write.writerow(['Read Latency Standard Deviation', get_sd(final_list_r_l)])
        write.writerow(['Write Throughput Min', get_min(final_list_w_tp)])
        write.writerow(['Write Throughput Max', get_max(final_list_w_tp)])
        write.writerow(['Write Throughput Average', get_avg(final_list_w_tp)])
        write.writerow(['Write Throughput Standard Deviation', get_sd(final_list_w_tp)])
        write.writerow(['Read Throughput Min', get_min(final_list_r_tp)])
        write.writerow(['Read Throughput Max', get_max(final_list_r_tp)])
        write.writerow(['Read Throughput Average', get_avg(final_list_r_tp)])
        write.writerow(['Read Throughput Standard Deviation', get_sd(final_list_r_tp)])


get_latency_reader()
get_latency_writer()
get_throughput_reader()
get_throughput_writer()
create_csv()
   