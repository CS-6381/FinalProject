# (modified by Google Cloud Pub Sub Team)

# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Imports
import argparse, ast, os, sys, time, datetime, zmq, broker, csv, uuid
from datetime import datetime as dt
import socket as sock
from google.cloud import pubsub_v1

# Establish variables.
sleepTime = 3
outTime = 300
timeFormat = '%Y-%m-%d %H:%M:%S.%f'
messageArr = []
messageLimit = 10

def sub(project_id, subscription_id, timeout=None):
    """Receives messages from a Pub/Sub subscription."""
    # Initialize a Subscriber client
    subscriber_client = pubsub_v1.SubscriberClient()
    # Create a fully qualified identifier in the form of
    subscription_path = subscriber_client.subscription_path(project_id, subscription_id)

    def bindSocket(message):
        context = zmq.Context()
        ipAddress = str(sock.gethostbyname(sock.gethostname()))
        portNumer = 5000
        socket = context.socket(zmq.PUB)
        bind_str = "tcp://" + ipAddress + ":" + portNumber
        print("Bind str: " + bind_str)
        socket.bind(bind_str)
        print("Binding done")
        print(message)
        socket.send_string("message")
        print('Message sent')

    def extractMessage(message, receiptTime):
        print("Extracting message - # of messages saved: " + str(len(messageArr)))
        try:
            messageData = message.data.decode("utf-8") 
            splitMessage = messageData.split('_')
            print(splitMessage)
            messageSize = splitMessage[1]
            sendTimeStr = splitMessage[2]
            sendTime = datetime.datetime.strptime(sendTimeStr, timeFormat)
            brokerToSubscriberTime = datetime.timedelta.total_seconds(receiptTime - sendTime)
            publisherToBrokerTime = splitMessage[3]
            publisherToBrokerSuccessRate = str(splitMessage[4])
            messageID = message.message_id
            messageArr.append([messageID, publisherToBrokerTime, brokerToSubscriberTime])
            return {'messageSize': messageSize, 'publisherToBrokerSuccessRate': publisherToBrokerSuccessRate}

        except Exception as e:
            print("Exception: " + str(e))
    
    def saveMessageTimes(result):
        print("********************** Saving messages ...")
        print("Message size + publisher to broker success rate: " + str(result))
        with open("./timeMeasurements/tm_" + str(messageLimit) + "_" + result['messageSize'] + "_" + result['publisherToBrokerSuccessRate'] + "_" + str(uuid.uuid4()) + ".csv", "w") as csvFile:
            csvWriter = csv.writer(csvFile)
            csvWriter.writerow(['messageID', 'publisherToBrokerTime', 'brokerToSubscriberTime'])
            csvWriter.writerows(messageArr)
        print("!!!!!!!!!!!!!!!!!!!!!! Done saving messages")
        return "Done"

    def callback(message):
        receiptTime = datetime.datetime.now()
        print("Received message: " + str(len(messageArr)) + " out of " + str(messageLimit))
        # Acknowledge the message. Unack'ed messages will be redelivered.
        message.ack()
        print("Acknowledged: " + str(message.message_id))
        result = extractMessage(message, receiptTime)
        if len(messageArr) == messageLimit:
            saveMessageTimes(result)
            abort(404)

    streaming_pull_future = subscriber_client.subscribe(
        subscription_path, callback=callback
    )
    print("Listening for messages on: " + str(subscription_path))
    try:
        # Calling result() on StreamingPullFuture keeps the main thread from
        # exiting while messages get processed in the callbacks.
        streaming_pull_future.result(timeout=timeout)

    except:  # noqa
        streaming_pull_future.cancel()
    subscriber_client.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("project_id", help="Google Cloud project ID")
    parser.add_argument("subscription_id", help="Pub/Sub subscription ID")
    parser.add_argument(
        "timeout", default=None, nargs="?", const=1, help="Pub/Sub subscription ID"
    )
    args = parser.parse_args()
    while True:
        sub(args.project_id, args.subscription_id, args.timeout)