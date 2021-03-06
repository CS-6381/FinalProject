# Use this to calculate statistics based on timeMeasurements files.

# Imports
import os, csv, datetime, time, uuid, numpy
from pathlib import Path
from datetime import datetime, timedelta

# Lists to store times
publisherToBrokerTimes = []
brokerToSubscriberTimes = []

# Lists to store success rates
publisherToBrokerSuccessRates = []
brokerToSubscriberSuccessRates = []

# Establish directories.
directoryPath = './timeMeasurements/'
directory = Path(directoryPath)
                                                                                                         
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
            publisherToBrokerTimes.append(float(row[1]))
            brokerToSubscriberTimes.append(float(row[2]))
            successCount = successCount + 1
        splitFile = fileName.split('_')
        publisherToBrokerSuccessRates.append(float(splitFile[3]))
        brokerToSubscriberSuccessRates.append(successCount / float(splitFile[1]))
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
    publisherToBrokerTimesMin = min(publisherToBrokerTimes)
    publisherToBrokerTimesMax = max(publisherToBrokerTimes)
    publisherToBrokerTimesAverage = getAverage(publisherToBrokerTimes)
    publisherToBrokerTimesStandardDeviation = getStandardDeviation(publisherToBrokerTimes)
    brokerToSubscriberTimesMin = min(brokerToSubscriberTimes)
    brokerToSubscriberTimesMax = max(brokerToSubscriberTimes)
    brokerToSubscriberTimesAverage = getAverage(brokerToSubscriberTimes)
    brokerToSubscriberTimesStandardDeviation = getStandardDeviation(brokerToSubscriberTimes)
    publisherToBrokerSuccessRatesMin = min(publisherToBrokerSuccessRates)
    publisherToBrokerSuccessRatesMax = max(publisherToBrokerSuccessRates)
    publisherToBrokerSuccessRatesAverage = getAverage(publisherToBrokerSuccessRates)
    publisherToBrokerSuccessRatesStandardDeviation = getStandardDeviation(publisherToBrokerSuccessRates)
    brokerToSubscriberSuccessRatesMin = min(brokerToSubscriberSuccessRates)
    brokerToSubscriberSuccessRatesMax = max(brokerToSubscriberSuccessRates)
    brokerToSubscriberSuccessRatesAverage = getAverage(brokerToSubscriberSuccessRates)
    brokerToSubscriberSuccessRatesStandardDeviation = getStandardDeviation(brokerToSubscriberSuccessRates)

    # Save CSV. Create the folder first.
    saveFile = "./calculations/sc_" + folderName + "_" + datetime.now().strftime("%m-%d-%Y_%H%M%S") + "_" + str(uuid.uuid4()) + ".csv"
    with open(saveFile, "w") as csvFile:
        csvWriter = csv.writer(csvFile)
        csvWriter.writerow(['Metric', 'Value'])
        csvWriter.writerow(['publisherToBrokerTimesMin', publisherToBrokerTimesMin])
        csvWriter.writerow(['publisherToBrokerTimesMax', publisherToBrokerTimesMax])
        csvWriter.writerow(['publisherToBrokerTimesAverage', publisherToBrokerTimesAverage])
        csvWriter.writerow(['publisherToBrokerTimesStandardDeviation', publisherToBrokerTimesStandardDeviation])
        csvWriter.writerow(['brokerToSubscriberTimesMin', brokerToSubscriberTimesMin])
        csvWriter.writerow(['brokerToSubscriberTimesMax', brokerToSubscriberTimesMax])
        csvWriter.writerow(['brokerToSubscriberTimesAverage', brokerToSubscriberTimesAverage])
        csvWriter.writerow(['brokerToSubscriberTimesStandardDeviation', brokerToSubscriberTimesStandardDeviation])
        csvWriter.writerow(['publisherToBrokerSuccessRatesMin', publisherToBrokerSuccessRatesMin])
        csvWriter.writerow(['publisherToBrokerSuccessRatesMax', publisherToBrokerSuccessRatesMax])
        csvWriter.writerow(['publisherToBrokerSuccessRatesAverage', publisherToBrokerSuccessRatesAverage])
        csvWriter.writerow(['publisherToBrokerSuccessRatesStandardDeviation', publisherToBrokerSuccessRatesStandardDeviation])
        csvWriter.writerow(['brokerToSubscriberSuccessRatesMin', brokerToSubscriberSuccessRatesMin])
        csvWriter.writerow(['brokerToSubscriberSuccessRatesMax', brokerToSubscriberSuccessRatesMax])
        csvWriter.writerow(['brokerToSubscriberSuccessRatesAverage', brokerToSubscriberSuccessRatesAverage])
        csvWriter.writerow(['brokerToSubscriberSuccessRatesStandardDeviation', brokerToSubscriberSuccessRatesStandardDeviation])
    return saveFile

# Loop across all time measurements files before saving CSV.
saveCount = 0
folderList = []
for f in directory.glob('**/*'):
    strF = str(f)
    print("Looping across: " + strF)
    if 'producer' in strF or 'consumer' in strF or 'all' in strF:
        innerFolder = strF.split('timeMeasurements/')[1]
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
saveDirectory = saveFile.split('sc_')[0]
print(folderList)
print("Save count: " + str(saveCount))
print("Results at: " + saveDirectory)