# Use this to generate a file of random characters equal to the count specified as an argument.

# Imports
import sys, string, random, uuid, time, datetime
from datetime import datetime

# Generate a string of random characters equal to the specified count.
charLength = sys.argv[1]
randomStr = ''.join(random.choices(string.ascii_uppercase + string.digits, k = int(charLength)))

# Save the file.
saveName = "./messages/Message_" + charLength + "_" + datetime.now().strftime("%m-%d-%Y_%H%M%S") + "_" + str(uuid.uuid4()) + ".txt"
with open(saveName, "w") as f:
    f.write(randomStr)
    f.close()