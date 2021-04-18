# Use this to empty out old messages from Google Cloud Pub Sub.

# Imports
import os, time

# Variables
subscriptionPath = 'projects/<<insert string here>>/subscriptions/<<insert string here>>'
sleepTime = 5

# Clear old messages and close all xterm windows.
print('Clearing ...')
terminalCMD = 'gcloud pubsub subscriptions seek ' + subscriptionPath + ' --time=$(date +%Y-%m-%dT%H:%M:%S)'
os.system(terminalCMD)
time.sleep(sleepTime)
# os.system('killall xterm')
print('Done clearing old Google Cloud Pub Sub messages')