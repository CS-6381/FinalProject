import pandas as pd

import os, csv, datetime, time, uuid, numpy
from pathlib import Path
import dateutil.parser
# from datetime import datetime, timedelta


saveFile = "./calculations/Calculations_" + datetime.datetime.now().strftime("%m-%d-%Y_%H%M%S") + "_" + str(uuid.uuid4()) + ".csv"

def mktimestamp(timestr):
    try:
        supertime = dateutil.parser.parse(timestr)
    except Exception as e:
        print(timestr, e)
    theTS = supertime.timestamp()
    # time.mktime(datetime.datetime.strptime(timestr,"%YYYY-%mm-%dd %H:%M:%S").timetuple())
    return theTS

# Loop across all timeDifferences files before saving CSV.
folder = 'Results'
print(os.listdir(folder))
for f in os.listdir(folder):        
    f = os.path.join(folder, f)
    if ('.csv' in str(f)) & (not '_min_sec' in str(f)):
        with open(f + '_min_sec.csv','w') as fout:
            fout.write('start_times,end_time,time_diff\n')
            with open(f,'r') as fin:
                for line in fin:
                    line = line.replace(',2021-04-24 ',',2021-04-22 ')
                    lineList = line.split(',2021-04-22 ')
                    if len(lineList)>2:
                        start_time = mktimestamp(lineList[1])
                        end_time = mktimestamp(lineList[2])
                        fout.write(str(start_time) + ',' +  str(end_time) + ',' +  str(end_time - start_time) + '\n')
                    

