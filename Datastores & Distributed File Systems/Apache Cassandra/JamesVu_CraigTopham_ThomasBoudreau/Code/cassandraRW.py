# Have Cassandra running and run this as a writer or reader.
# "python3 cassandraRW.py 5 w 5" = 5 iterations of writing a random 5-character message into the database
# "python3 cassandraRW.py 5 r" = 5 iterations of reading 1 message from the database

# Imports
import os, sys, datetime, time, string, random, uuid, csv, subprocess
from datetime import datetime as dt
# pip3 install cassandra-driver
from cassandra.cluster import Cluster

# Connect to Cassandra.
cluster = Cluster()
session = cluster.connect('cs6381finalprojectks1')

# Other variables
thisFile = str(os.path.basename(__file__))
sleepTime = 1
timeList = []
loopCount = int(sys.argv[1])
rwOption = sys.argv[2]

# Function to write to Cassandra
def writeQuery(charLength):
    print("Writing ...")
    message = ''.join(random.choices(string.ascii_uppercase + string.digits, k = int(charLength)))
    query = "INSERT INTO table1 (id, message) VALUES(" + str(uuid.uuid4()) + ", '" + message + "')"
    session.execute(query)
    return message

# Function to read from Cassandra
def readQuery():
    print("Reading ...")
    rows = session.execute("SELECT * FROM table1 LIMIT 1")
    message = ''
    for row in rows:
        rowMessage = row.message
    return rowMessage

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
def saveTimes():
    print("Saving times ...")
    saveName = ''
    if rwOption == 'w':
        saveName = "./timeDifferences/timeDifferences_" + rwOption + "_" + str(loopCount) + "_" + sys.argv[3] + "_" + getHostName() + "_" + getProcessID(thisFile) + "_" + dt.now().strftime("%m-%d-%Y_%H%M%S") + "_" + str(uuid.uuid4()) + ".csv"
    if rwOption == 'r':
        saveName = "./timeDifferences/timeDifferences_" + rwOption + "_" + str(loopCount) + "_" + getHostName() + "_" + getProcessID(thisFile) + "_" + dt.now().strftime("%m-%d-%Y_%H%M%S") + "_" + str(uuid.uuid4()) + ".csv"
    with open(saveName, "w") as csvFile:
        csvWriter = csv.writer(csvFile)
        csvWriter.writerow(['readerID', 'writerID', 'key', 'startTime', 'endTime', 'timeDifference'])
        csvWriter.writerows(timeList) 
    return 'Done'

# Iterate writing or reading a specified number of times before appending time differences to a CSV file.
for i in range(loopCount):
    print("Running " + thisFile + " as " + rwOption + ". Iteration: " + str(i + 1) + " out of " + str(loopCount))
    startTime = ''
    returnVal = ''
    writerID = '0'
    readerID = '0'
    if rwOption == 'w':
        startTime = datetime.datetime.now()
        returnVal = writeQuery(sys.argv[3])
        writerID = getProcessID(thisFile)
    if rwOption == 'r':
        startTime = datetime.datetime.now()
        returnVal = readQuery()
        readerID = getProcessID(thisFile)
    endTime = datetime.datetime.now()
    timeDifference = endTime - startTime
    timeList.append([readerID, writerID, returnVal, str(startTime), str(endTime), str(timeDifference)])
    print("Time difference: " + str(timeDifference))
    # time.sleep(sleepTime)
saveTimes()
print("Done: " + rwOption)
time.sleep(sleepTime)