# Run a number of readers 1 by 1.
import os, sys, time
sleepTime = 3
iterations = int(sys.argv[1])
for i in range(iterations):
    print("Iteration: " + str(i + 1) + " out of " + str(iterations))
    os.system("curl 'http://localhost:5000/r/1/1000'")
    time.sleep(sleepTime)