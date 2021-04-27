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
    supertime = dateutil.parser.parse(timestr)
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
    return [ele for ele in list if ele > 0]
    


def saveCalculations(df, f):
        # Calculate statistics.
    start_times = list(map(mktimestamp,df['start_time'].tolist()))
    writeOutList(start_times,'start_times')
    end_times =  list(map(mktimestamp,df['end_time'].tolist()))
    writeOutList(end_times,'end_times')
    newWriteTimes = removeNeg(listDiff(start_times))
    print('newWriteTimes',newWriteTimes[0],type(newWriteTimes[0]),len(newWriteTimes))
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

    
    with open(saveFile, "+a") as csvFile:
        csvWriter = csv.writer(csvFile)
        csvWriter.writerow(['file name','writeLatencyMin', 'writeLatencyMax',writeLatencyMin])
        csvWriter.writerow([f,writeLatencyMin, writeLatencyMax,writeLatencyMin])



# Loop across all timeDifferences files before saving CSV.
folder = 'Results'
print(os.listdir(folder))
for f in os.listdir(folder):        
    f = os.path.join(folder, f)
    if '25r.csv' in str(f):
        df = pd.read_csv(f)

        df['diff_time'] = pd.to_datetime(df['end_time']) - pd.to_datetime(df['start_time'])
        saveCalculations(df,f)
        print(f)
        print(df.head(10))

thistestlist = [0,.25,.5, 2 ]
print(listDiff(thistestlist))