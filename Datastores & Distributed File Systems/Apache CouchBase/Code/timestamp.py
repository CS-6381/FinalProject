from datetime import datetime
import time

def getDateTime():
    #dateTimeObj = datetime.now()
    #return dateTimeObj
    now = time.time()
    return now
    #return round(time.time() * 1000)

def gethms():
    time_seconds = getDateTime()
    ty_res = time.gmtime(time_seconds)
    res = time.strftime("%H:%M:%S",ty_res)
    return str(res)


def convert_gethms(time_string):
    #ty_res = time.gmtime(time_string)
    res =  time.strptime(time_string,'%H:%M:%S')
    return res

