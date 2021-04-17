import sys
import os
import stomp
import time

user = os.getenv("ACTIVEMQ_USER") or "admin"
password = os.getenv("ACTIVEMQ_PASSWORD") or "password"
host = os.getenv("ACTIVEMQ_HOST") or "localhost"
port = os.getenv("ACTIVEMQ_PORT") or 61613
destination = sys.argv[1:2] or ["/topic/event"]
destination = destination[0]
messages = 100000
data = "Hello World from Python"

conn = stomp.Connection(host_and_ports = [(host, port)])
conn.start()
conn.connect(login=user,passcode=password)

for i in range(0, messages):
  conn.send(body=data, destination=destination, persistent='false')
  time.sleep(0.1)
  
conn.send(body="SHUTDOWN", destination=destination, persistent='false')

conn.disconnect()
