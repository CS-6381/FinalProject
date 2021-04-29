# Use this to calculate statistics based on timeMeasurements files.

# Imports
import os, csv, datetime, time, uuid, numpy, ntpath, pathlib
from pathlib import Path
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import pandas as pd

# Lists to store times
publisherToBrokerTimes = []
brokerToSubscriberTimes = []

# Lists to store success rates
publisherToBrokerSuccessRates = []
brokerToSubscriberSuccessRates = []

# Establish directories.
directoryPath = './timeMeasurements/'
directory = Path(directoryPath)
folderList = []
saveFile = "./calculations/ac_" + datetime.now().strftime("%m-%d-%Y_%H%M%S") + "_" + str(uuid.uuid4()) + ".csv"
with open(saveFile, "w") as csvFile:
    csvWriter = csv.writer(csvFile)
    csvWriter.writerow(['Condition', 'publisherToBrokerTimesMin', 'publisherToBrokerTimesMax', 'publisherToBrokerTimesAverage', 'publisherToBrokerTimesStandardDeviation', 'brokerToSubscriberTimesMin', 'brokerToSubscriberTimesMax', 'brokerToSubscriberTimesAverage', 'brokerToSubscriberTimesStandardDeviation', 'publisherToBrokerSuccessRatesMin', 'publisherToBrokerSuccessRatesMax', 'publisherToBrokerSuccessRatesAverage', 'publisherToBrokerSuccessRatesStandardDeviation', 'brokerToSubscriberSuccessRatesMin', 'brokerToSubscriberSuccessRatesMax', 'brokerToSubscriberSuccessRatesAverage', 'brokerToSubscriberSuccessRatesStandardDeviation'])
                                                                                                         
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

    # Save CSV.
    with open(saveFile, "a", newline='') as csvFile:
        csvWriter = csv.writer(csvFile)
        csvWriter.writerow([folderName, publisherToBrokerTimesMin, publisherToBrokerTimesMax, publisherToBrokerTimesAverage, publisherToBrokerTimesStandardDeviation, brokerToSubscriberTimesMin, brokerToSubscriberTimesMax, brokerToSubscriberTimesAverage, brokerToSubscriberTimesStandardDeviation, publisherToBrokerSuccessRatesMin, publisherToBrokerSuccessRatesMax, publisherToBrokerSuccessRatesAverage, publisherToBrokerSuccessRatesStandardDeviation, brokerToSubscriberSuccessRatesMin, brokerToSubscriberSuccessRatesMax, brokerToSubscriberSuccessRatesAverage, brokerToSubscriberSuccessRatesStandardDeviation])
    return saveFile

# Function to generate graphs from Calculations CSV file
def generateGraphs(statsFile):
    
    # Initialize the lists for X and Y
    fig = plt.figure(figsize=(20, 15))
    statsDirectory = './calculations/' + statsFile
    data = pd.read_csv(statsDirectory)
    df = pd.DataFrame(data)
    statParams = ['publisherToBrokerTimesMin', 'publisherToBrokerTimesMax', 'publisherToBrokerTimesAverage', 'publisherToBrokerTimesStandardDeviation', 'brokerToSubscriberTimesMin', 'brokerToSubscriberTimesMax', 'brokerToSubscriberTimesAverage', 'brokerToSubscriberTimesStandardDeviation', 'publisherToBrokerSuccessRatesMin', 'publisherToBrokerSuccessRatesMax', 'publisherToBrokerSuccessRatesAverage', 'publisherToBrokerSuccessRatesStandardDeviation', 'brokerToSubscriberSuccessRatesMin', 'brokerToSubscriberSuccessRatesMax', 'brokerToSubscriberSuccessRatesAverage', 'brokerToSubscriberSuccessRatesStandardDeviation']
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
saveDirectory = saveFile.split('ac_')[0]
print("Save file: " + saveFile)
print(folderList)
print("Save count: " + str(saveCount))
generateGraphs(ntpath.basename(saveFile))
print("CSV results at: " + saveDirectory)
print("Graph results at: " + "./graphs/")