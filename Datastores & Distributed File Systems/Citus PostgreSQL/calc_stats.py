import pandas as pd
import os, csv, datetime, time, uuid, numpy
from pathlib import Path
import dateutil.parser
# from datetime import datetime, timedelta

saveFile = "./calculations/Calculations_" + datetime.datetime.now().strftime("%m-%d-%Y_%H%M%S") + "_" + str(uuid.uuid4()) + ".csv"

# Function to calculate average
def getAverage(data):
    total = sum(tuple(data))
    average = total / len(data)
    return average 

# Function to calculate standard deviation
def getStandardDeviation(data):
    mean = sum(data) / len(data)
    variance = sum([((x - mean) ** 2) for x in data]) / len(data)
    res = variance ** 0.5
    return res

def mktimestamp(timestr):
    try:
        supertime = dateutil.parser.parse(timestr)
    except Exception as e:
        print(timestr, e)
    theTS = supertime.timestamp()
    # time.mktime(datetime.datetime.strptime(timestr,"%YYYY-%mm-%dd %H:%M:%S").timetuple())
    return theTS

def listDiff(listy):            # [1, 2, 3]
    list1 = []
    list2 = []
    for i in listy:
        list1.append(i)
        list2.append(i)
    list1.append(0)     # [1, 2, 3, 0]
    list2.insert(0,0 )  # [0, 1, 2, 3]
    diffList = []
    zip_object = zip(list1, list2)
    for list1_i, list2_i in zip_object:
        diffList.append(list1_i-list2_i)
    diffList.pop()
    diffList.pop(0)      #    [1, 1]
    return diffList

def writeOutList(listyMcList,fname):
    with open(fname + '.txt','w') as fout:
        for i in listyMcList:
            fout.write(str(i) + '\n')

def removeNeg(list):
    # Remove Negative Elements in List
    # Using list comprehension
    list_for_short_time = [ele for ele in list if ele > 0]
    if len(list_for_short_time) == 0:
        list_for_short_time = list
    print('len(list_for_short_time)',len(list_for_short_time))
    return list_for_short_time
    
def calculize(df, f):
        # Calculate statistics.
    start_times = df['start_times'].tolist()
    end_times =  df['end_time'].tolist()
    time_diff =  df['time_diff'].tolist()
    print('start_times',len(start_times))
    newWriteTimes = removeNeg(listDiff(start_times))
    print('newWriteTimes',type(newWriteTimes),len(newWriteTimes))
    newWriteTimes.sort()
    writeOutList(newWriteTimes,'sortedNewWriteTimes')
    newReadTimes =  removeNeg(listDiff(end_times))
    writeLatencyMin = min(newWriteTimes)
    writeLatencyMax = max(newWriteTimes)
    writeLatencyAverage = getAverage(newWriteTimes)
    writeLatencyStandardDeviation = getStandardDeviation(newWriteTimes)
    readLatencyMin = min(newReadTimes)
    readLatencyMax = max(newReadTimes)
    readLatencyAverage = getAverage(newReadTimes)
    readLatencyStandardDeviation = getStandardDeviation(newReadTimes)
    writeThroughput = (max(start_times)-min(start_times))/len(start_times)
    # writeThroughputMax = max(writeSuccessRates)
    # writeThroughputAverage = getAverage(writeSuccessRates)
    # writeThroughputStandardDeviation = getStandardDeviation(writeSuccessRates)
    # readThroughputMin = min(readSuccessRates)
    # readThroughputMax = max(readSuccessRates)
    # readThroughputAverage = getAverage(readSuccessRates)
    # readThroughputStandardDeviation = getStandardDeviation(readSuccessRates)
    print('writeLatencyMin = min(newWriteTimes)', writeLatencyMin)
    print('writeLatencyMax = max(newWriteTimes)', writeLatencyMax)
    print('writeLatencyAverage = getAverage(newWriteTimes)',writeLatencyAverage)
    print('writeLatencyStandardDeviation = getStandardDeviation(newWriteTimes)',writeLatencyStandardDeviation)
    print('readLatencyMin = min(newReadTimes)',readLatencyMin)
    print('readLatencyMax = max(newReadTimes)',readLatencyMax)
    print('readLatencyAverage = getAverage(newReadTimes)',readLatencyAverage)
    print('readLatencyStandardDeviation = getStandardDeviation(newReadTimes)',readLatencyStandardDeviation)
    print('writeThroughput',writeThroughput)
    return [writeLatencyMin, writeLatencyMax,writeLatencyAverage,writeThroughput,readLatencyMin,readLatencyMax,readLatencyAverage,readLatencyStandardDeviation]

# Loop across all timeDifferences files before saving CSV.
folder = 'Results'
print(os.listdir(folder))

with open(saveFile, "+a",newline='') as csvFile:
    csvWriter = csv.writer(csvFile)
    csvWriter.writerow(['file name','writeLatencyMin', 'writeLatencyMax','writeLatencyAverage','writeThroughput','readLatencyMin','readLatencyMax','readLatencyAverage','readLatencyStandardDeviation'])
    for f in os.listdir(folder):        
        f = os.path.join(folder, f)
        if '_min_sec.csv' in str(f):
            df = pd.read_csv(f)
            print(f)            
            print(df['start_times'].head(10).to_list())
            csvWriter.writerow([f] + calculize(df,f))