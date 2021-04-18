# Have Cassandra running, run this a server (python3 capAnalysis.py), and use HTTP requests to run a writer or reader off of it ("http://localhost:5000/{{path}}").

# Imports
import os, sys, datetime, time, string, random, uuid, csv, subprocess, requests
from datetime import datetime as dt
# pip3 install cassandra-driver
from cassandra.cluster import Cluster
from pathlib import Path
from flask import *
app = Flask(__name__)

# Other variables
thisFile = str(os.path.basename(__file__))
sleepTime = 1
timeList = []
directory = Path('./samples')

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

# Function to get current time
def getTime():
    return str(datetime.datetime.now())

# Function to insert record to Cassandra
def insertQuery(payload, recordIndex):
    print("Inserting ...")
    message = payload + ' ' + getTime()
    query = "INSERT INTO table1 (id, message) VALUES(" + recordIndex + ", '" + message + "')"
    session.execute(query)
    return message

# Function to write to Cassandra
def updateQuery(payload, recordIndex):
    print("Updating ...")
    message = payload + ' ' + getTime()
    query = "UPDATE table1 SET message = '" + message + "' where id = " + recordIndex + ";"
    print(query)
    session.execute(query)
    return message

# Function to read from Cassandra
def readQuery(recordIndex):
    print("Reading ...")
    readStartTime = getTime()
    rows = session.execute("SELECT * FROM table1 where id = " + recordIndex)
    rowMessage = ''
    for row in rows:
        print(row)
        # rowMessage = row['message']
        rowMessage = row.message
    readEndTime = getTime()
    rowMessageSplit = rowMessage.split(' ')
    writeTime = rowMessageSplit[1] + ' ' + rowMessageSplit[2]
    result = ['reader' + recordIndex, writeTime, readStartTime, readEndTime]
    print(result)
    return result

# Function to get hostname to distinguish machines
def getHostName():
    print("Getting host name ...")
    rawOutput = str(subprocess.check_output('hostname -I', shell = True))
    cleanOutput = rawOutput.split("b'")[1]
    if ' ' in rawOutput:
        cleanOutput = cleanOutput.split(' ')[0]
    cleanOutput = cleanOutput.replace('.','+')
    return cleanOutput

# Function to get process ID to distinguish instances
def getProcessID(processName):
    print("Getting process ID for: " + processName)
    try:
        rawOutput = str(subprocess.check_output('ps -ef | grep ' + processName, shell = True))
        whoAmI = str(subprocess.check_output("whoami", shell = True)).split("'")[1].split("\\")[0]
        processID = str(rawOutput.split(whoAmI)[1].lstrip()).split(' ')[0]
        return processID
    except Exception as e:
        print("getProcessID Exception: " + str(e))
        return None

# Function to save time differences to CSV files. Create the folder first.
def saveTimes(iterations):
    print("Saving times ...")
    saveName = "./capTimes/ct_" + iterations + "_" + getHostName() + "_" + getProcessID(thisFile) + "_" + dt.now().strftime("%m-%d-%Y_%H%M%S") + "_" + str(uuid.uuid4()) + ".csv"
    with open(saveName, "w") as csvFile:
        csvWriter = csv.writer(csvFile)
        csvWriter.writerow(['Label Identifying Reader Id', 'Write Message timestamp', 'Read Start Timestamp', 'Read Finish Timestamp'])
        csvWriter.writerows(timeList) 
    return 'Done'

@app.route('/i/<recordIndex>')
def insertCall(recordIndex):
    for f in directory.glob('**/*'):
        strFile = str(f)
        if recordIndex in strFile:
            with open(strFile, 'r') as fileMessage:
                insertQuery(fileMessage.read(), recordIndex)
    # exit
    return "Done insert"

@app.route('/u/<recordIndex>')
def updateCall(recordIndex):
    while True:
        for f in directory.glob('**/*'):
            strFile = str(f)
            if recordIndex in strFile:
                with open(strFile, 'r') as fileMessage:
                    updateQuery(fileMessage.read(), recordIndex)
    return "Done update"

@app.route('/r/<recordIndex>/<iterations>')
def readCall(recordIndex, iterations):
    for i in range(int(iterations)):
        timeList.append(readQuery(recordIndex))
    saveTimes(iterations)
    print("Done read")
    return "Done read"

if __name__=="__main__":
    # Connect to Cassandra.
    cluster = Cluster()
    session = cluster.connect('cs6381finalprojectks1')
    print("Ready for requests")
    app.run(debug=False, port=5000)