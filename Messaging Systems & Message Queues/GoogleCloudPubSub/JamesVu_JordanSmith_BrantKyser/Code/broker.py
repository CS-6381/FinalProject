# Sample code for CS6381 (modified by Google Cloud Pub Sub Team)
# Vanderbilt University
# Instructor: Aniruddha Gokhale
#
# Code taken from ZeroMQ examples and modified to demonstrate
# a subscriber with multiple sockets and using poll to decide if
# there is incoming data.
#
# We can execute the code on localhost or in mininet
#
#

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
import sys, time, datetime, zmq, broker, os, uuid, argparse
from datetime import datetime as dt
from google.cloud import pubsub_v1

class CS6381_Subscriber ():
    """ Subscriber class """

    #################################################################
    # constructor
    #################################################################
    def __init__ (self, args):
        # arguments
        self.publicationIP = '127.0.1.1'
        self.port = '5000'
        self.topic = 'message'
        self.projectID = args[0]
        self.topicID = args[1]
        self.successCount = 0
        
        #  The zmq context
        self.context = None

        # we will use the poller to poll for incoming data
        self.poller = None
        
        # socket for each subscription
        self.topic_socket = None

    #################################################################
    # configure the subscriber
    #################################################################
    def configure (self):

        # first get the context
        print ("Subscriber::configure - get the context object")
        self.context = zmq.Context()

        # obtain the poller
        print ("Subscriber::configure - get the poller object")
        self.poller = zmq.Poller ()

        # now let us obtain our sockets all of which are of SUB type
        print ("Subscriber::configure - obtain the SUB socket")
        self.topic_socket = self.context.socket (zmq.SUB)

        # connect all our sockets to the publisher
        print ("Subscriber::configure - connect the SUB sockets to publisher")

        # Send parameters to the broker.
        publicationIP = self.publicationIP
        topic = self.topic
        portNumber = self.port
        import socket as sock
        connect_str = "tcp://" + publicationIP + ":" + portNumber
        print("connect_str: " + connect_str)
        self.topic_socket.connect(connect_str)
        
        # set filters on the sockets
        filter = topic
        print("Filter: " + str(filter))
        print ("Subscriber:configure - subscribing to {}".format (filter))
        self.topic_socket.setsockopt_string(zmq.SUBSCRIBE, filter)
        
        # register these sockets for incoming data
        print ("Subscriber::configure - register our sockets with a poller")
        self.poller.register (self.topic_socket, zmq.POLLIN)

    # ***** Helper function to measure time between publication and receipt by subscriber
    def measureTime(self, payload, receiptTime):
        splitPayload = payload.split("_")
        messageSize = splitPayload[0] + '_' + splitPayload[1]
        sendTimeStr = splitPayload[2]
        messageContent = splitPayload[3]
        print("sendTimeStr: " + str(sendTimeStr))
        timeFormat = '%Y-%m-%d %H:%M:%S.%f'
        sendTime = datetime.datetime.strptime(sendTimeStr, timeFormat)
        publisherToBrokerTime = str(datetime.timedelta.total_seconds(receiptTime - sendTime))
        nowTime = str(datetime.datetime.now())
        self.successCount = self.successCount + 1
        attemptCount = int(splitPayload[4])
        successRate = str(self.successCount / attemptCount)
        newMessage = messageSize + '_' + nowTime + '_' + publisherToBrokerTime + '_' + successRate + '_' + messageContent 
        print("Message to send from broker to subscriber: " + newMessage)

        # Initialize a Publisher client.
        client = pubsub_v1.PublisherClient()
        # Create a fully qualified identifier of form `projects/{project_id}/topics/{topic_id}`
        topic_path = client.topic_path(self.projectID, self.topicID)

        # When you publish a message, the client returns a future.
        print("Topic path set")
        byteMessage = bytes(newMessage, 'utf-8')
        api_future = client.publish(topic_path, byteMessage)
        message_id = api_future.result()

    #################################################################
    # run the event loop
    #################################################################
    def event_loop (self):
        print ("Subscriber:event_loop - run the event loop")
        count = 1
        while True:
            print("Count: " + str(count))
            count = count + 1

            # poll for events. We give it an infinite timeout.
            # The return value is a socket to event mask mapping
            print("Polling...")
            events = dict (self.poller.poll ())

            # find which socket was enabled and accordingly make a callback
            # Note that we must check for all the sockets since multiple of them
            # could have been enabled.
            print("Is topic socket in events?")
            if self.topic_socket in events:
                print("Yes")
                self.recv_topic()

    def recv_topic(self):
        string = self.topic_socket.recv_string()
        receiptTime = datetime.datetime.now()
        result = str(self.measureTime(string, receiptTime))
        return result
    
#################################################################
# main function
#################################################################
def main (projectID, topicID):
    """ Main program """

    print("Current libzmq version is %s" % zmq.zmq_version())
    print("Current  pyzmq version is %s" % zmq.__version__)
    print ("Subscriber program")

    # first parse the arguments
    print ("Parse command line arguments")
    # parsed_args = [sys.argv[1], sys.argv[2], projectID, topicID]
    parsed_args = [sys.argv[1], sys.argv[2]]

    # instantiate the subscriber
    print ("Instantiate a subscriber object")
    subscriber =  CS6381_Subscriber (parsed_args)

    # configure the subscriber
    print ("Configure the subscriber")
    subscriber.configure ()

    # now let the subscriber wait in an event loop. Save the subscribed information into a specific file.
    print ("Start the event loop")
    subscriber.event_loop()
    print ("Subscriber event loop terminated")
    return "Done"
    
#----------------------------------------------
# if __name__ == '__main__':
#     main ()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("project_id", help="Google Cloud project ID")
    parser.add_argument("topic_id", help="Pub/Sub topic ID")

    args = parser.parse_args()

    main(args.project_id, args.topic_id)