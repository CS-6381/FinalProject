# Imports
import sys, time, datetime, zmq, broker, uuid
import socket as sock
from pathlib import Path

# Establish variables.
context = zmq.Context()
directory = Path('./messages')
sleepTime = 0.1
attemptCount = 1
ipAddress = str(sock.gethostbyname(sock.gethostname()))
portNumber = '5000'
fileName = sys.argv[1]
socket = context.socket(zmq.PUB)
bind_str = "tcp://" + ipAddress + ":" + portNumber
socket.bind(bind_str)

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

# Keep publishing.
while True:
    print("Publisher bound to: " + bind_str)
    topic = ''
    for f in directory.glob('**/*'):
        strFile = str(f)
        if fileName in strFile:
            with open(strFile, 'r') as fileMessage:
                openedMessage = fileMessage.read()
                nowTime = str(datetime.datetime.now())
                topic = 'messageSize_' + str(len(openedMessage)) + '_' + nowTime + '_' + openedMessage + '_' + str(attemptCount)
    print("Sending from publisher to broker - iteration: " + str(attemptCount))
    socket.send_string(topic)
    time.sleep(sleepTime)  # Take a short break.
    attemptCount = attemptCount + 1