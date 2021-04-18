# Use this to calculate statistics based on timeDifferences files.

# Imports
import os, csv, datetime, time, uuid, numpy
from pathlib import Path
from datetime import datetime, timedelta

# Lists to store write or read time differences
writeTimes = []
readTimes = []

# Lists to store rate of successful write or read iterations (e. g. '9/10' = 0.9)
writeSuccessRates = []
readSuccessRates = []

# Establish directories.
directory = Path('./timeDifferences/all')
                                                                                                         
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
def saveCalculations():

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

    # Save CSV. Create the folder first.
    saveFile = "./calculations/Calculations_" + datetime.now().strftime("%m-%d-%Y_%H%M%S") + "_" + str(uuid.uuid4()) + ".csv"
    with open(saveFile, "w") as csvFile:
        csvWriter = csv.writer(csvFile)
        csvWriter.writerow(['Metric', 'Value'])
        csvWriter.writerow(['writeLatencyMin', writeLatencyMin])
        csvWriter.writerow(['writeLatencyMax', writeLatencyMax])
        csvWriter.writerow(['writeLatencyAverage', writeLatencyAverage])
        csvWriter.writerow(['writeLatencyStandardDeviation', writeLatencyStandardDeviation])
        csvWriter.writerow(['readLatencyMin', readLatencyMin])
        csvWriter.writerow(['readLatencyMax', readLatencyMax])
        csvWriter.writerow(['readLatencyAverage', readLatencyAverage])
        csvWriter.writerow(['readLatencyStandardDeviation', readLatencyStandardDeviation])
        csvWriter.writerow(['writeThroughputMin', writeThroughputMin])
        csvWriter.writerow(['writeThroughputMax', writeThroughputMax])
        csvWriter.writerow(['writeThroughputAverage', writeThroughputAverage])
        csvWriter.writerow(['writeThroughputStandardDeviation', writeThroughputStandardDeviation])
        csvWriter.writerow(['readThroughputMin', readThroughputMin])
        csvWriter.writerow(['readThroughputMax', readThroughputMax])
        csvWriter.writerow(['readThroughputAverage', readThroughputAverage])
        csvWriter.writerow(['readThroughputStandardDeviation', readThroughputStandardDeviation])
    return saveFile

# Loop across all timeDifferences files before saving CSV.
for f in directory.glob('**/*'):
    if '.csv' in str(f):
        readCSV(f)
saveFile = saveCalculations()
print("Result at: " + saveFile)