# Use this to calculate statistics based on timeDifferences files.

# Imports
import os, csv, datetime, time, uuid, numpy, ntpath, pathlib
from pathlib import Path
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import pandas as pd

# Lists to store write or read time differences
writeTimes = []
readTimes = []

# Lists to store rate of successful write or read iterations (e. g. '9/10' = 0.9)
writeSuccessRates = []
readSuccessRates = []

# Establish directories.
directoryPath = './timeDifferences/'
directory = Path(directoryPath)
folderList = []
saveFile = "./calculations/ac_" + datetime.now().strftime("%m-%d-%Y_%H%M%S") + "_" + str(uuid.uuid4()) + ".csv"
with open(saveFile, "w") as csvFile:
    csvWriter = csv.writer(csvFile)
    csvWriter.writerow(['Condition', 'writeLatencyMin', 'writeLatencyMax', 'writeLatencyAverage', 'writeLatencyStandardDeviation', 'readLatencyMin', 'readLatencyMax', 'readLatencyAverage', 'readLatencyStandardDeviation', 'writeThroughputMin', 'writeThroughputMax', 'writeThroughputAverage', 'writeThroughputStandardDeviation', 'readThroughputMin', 'readThroughputMax', 'readThroughputAverage', 'readThroughputStandardDeviation'])
                                                                                                         
# Function to list all files in a directory                                                                                                                      
def listFiles(directory):                                                                                                  
    r = []                                                                                                            
    subdirs = [x[0] for x in os.walk(directory)]                                                                            
    for subdir in subdirs:                                                                                            
        files = os.walk(subdir).__next__()[2]                                                                             
        if (len(files) > 0):                                                                                          
            for file in files:                                                                                        
                r.append(os.path.join(subdir, file))                                                                         
    return r

# Function to convert list of times to proper format
def convertTimes(data):
    arr = []
    for datum in data:
        timeVal = float((datetime.strptime(datum, '%H:%M:%S.%f') - datetime.strptime('00', '%H')).total_seconds()*1000)
        arr.append(timeVal)
    return arr

# Function to read a CSV file
def readCSV(csvFile):
    
    # initializing the titles and rows list
    fields = []
    
    # reading csv file
    with open(csvFile, 'r') as cf:
        # creating a csv reader object
        csvReader = csv.reader(cf)
        
        # extracting field names through first row
        fields = next(csvReader)
    
         # extracting each data row one by one
        successCount = 0
        fileName = str(csvFile)
        for row in csvReader:
            if '_w_' in fileName:
                writeTimes.append(row[5])
            if '_r_' in fileName:
                readTimes.append(row[5])
            successCount = successCount + 1
        successMax = ''
        if '_w_' in fileName:
            writeSuccessRates.append(successCount/int(fileName.split('_w_')[1].split('_')[0]))
        if '_r_' in fileName:
            readSuccessRates.append(successCount/int(fileName.split('_r_')[1].split('_')[0]))
    return 'done'

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

# Function to save calculations to a CSV file
def saveCalculations(folderName):

    # Calculate statistics.
    newWriteTimes = convertTimes(writeTimes)
    newReadTimes = convertTimes(readTimes)
    writeLatencyMin = min(newWriteTimes)
    writeLatencyMax = max(newWriteTimes)
    writeLatencyAverage = getAverage(newWriteTimes)
    writeLatencyStandardDeviation = getStandardDeviation(newWriteTimes)
    readLatencyMin = min(newReadTimes)
    readLatencyMax = max(newReadTimes)
    readLatencyAverage = getAverage(newReadTimes)
    readLatencyStandardDeviation = getStandardDeviation(newReadTimes)
    writeThroughputMin = min(writeSuccessRates)
    writeThroughputMax = max(writeSuccessRates)
    writeThroughputAverage = getAverage(writeSuccessRates)
    writeThroughputStandardDeviation = getStandardDeviation(writeSuccessRates)
    readThroughputMin = min(readSuccessRates)
    readThroughputMax = max(readSuccessRates)
    readThroughputAverage = getAverage(readSuccessRates)
    readThroughputStandardDeviation = getStandardDeviation(readSuccessRates)

    # Save CSV.
    with open(saveFile, "a", newline='') as csvFile:
        csvWriter = csv.writer(csvFile)
        csvWriter.writerow([folderName, writeLatencyMin, writeLatencyMax, writeLatencyAverage, writeLatencyStandardDeviation, readLatencyMin, readLatencyMax, readLatencyAverage, readLatencyStandardDeviation, writeThroughputMin, writeThroughputMax, writeThroughputAverage, writeThroughputStandardDeviation, readThroughputMin, readThroughputMax, readThroughputAverage, readThroughputStandardDeviation])
    return saveFile

# Function to generate graphs from Calculations CSV file
def generateGraphs(statsFile):
    
    # Initialize the lists for X and Y
    fig = plt.figure(figsize=(20, 15))
    statsDirectory = './calculations/' + statsFile
    data = pd.read_csv(statsDirectory)
    df = pd.DataFrame(data)
    statParams = ['writeLatencyMin', 'writeLatencyMax', 'writeLatencyAverage', 'writeLatencyStandardDeviation', 'readLatencyMin', 'readLatencyMax', 'readLatencyAverage', 'readLatencyStandardDeviation', 'writeThroughputMin', 'writeThroughputMax', 'writeThroughputAverage', 'writeThroughputStandardDeviation', 'readThroughputMin', 'readThroughputMax', 'readThroughputAverage', 'readThroughputStandardDeviation']
    for col in range(16):
        X = list(df.iloc[:, 0])
        Y = list(df.iloc[:, col + 1])
        
        # Plot the data using bar() method
        plt.xticks(
            rotation=45, 
            horizontalalignment='right',
            fontsize='small'  
        )
        plt.bar(X, Y, color='g')
        xAxis = 'Condition'
        yAxis = statParams[col]
        plt.title(xAxis + ' vs. ' + yAxis)
        plt.xlabel(xAxis)
        plt.ylabel(yAxis)
        
        # Show the plot
        # plt.show()
        plt.savefig('./graphs/' + statsFile.replace('ac', yAxis).replace('.csv', '.png'))
    
    return 'Done'

# Loop across all timeDifferences files before saving CSV.
saveCount = 0
for f in directory.glob('**/*'):
    strF = str(f)
    print("Looping across: " + strF)
    if 'writer' in strF or 'reader' in strF or 'all' in strF:
        innerFolder = strF.split('timeDifferences/')[1]
        if '/' not in innerFolder:
            folderList.append(innerFolder)
for fold in folderList:
    innerDirectory = Path(directoryPath + fold)
    print("Inner directory: " + str(innerDirectory))
    for cf in innerDirectory.glob('**/*'):
        print("Inner directory item: " + str(cf))
        if '.csv' in str(cf):
            readCSV(cf)
    saveFile = saveCalculations(fold)
    saveCount = saveCount + 1
saveDirectory = saveFile.split('ac_')[0]
print("Save file: " + saveFile)
print(folderList)
print("Save count: " + str(saveCount))
generateGraphs(ntpath.basename(saveFile))
print("CSV results at: " + saveDirectory)
print("Graph results at: " + "./graphs/")