from datetime import datetime
import time

def getDateTime():
    #dateTimeObj = datetime.now()
    #return dateTimeObj
    now = time.time()
    return now
    #return round(time.time() * 1000)

def gethms():
    #time_seconds = getDateTime()
    #ty_res = time.gmtime(time_seconds)
    #res = time.strftime('%H:%M:%S.%f',ty_res)
    res = datetime.utcnow().strftime('%H:%M:%S.%f')
    return str(res)

def get_reg_hms():
    time_seconds = getDateTime()
    ty_res = time.gmtime(time_seconds)
    #res = time.strftime('%H:%M:%S.%f',ty_res)
    res = datetime.utcnow().strftime('%H:%M:%S.%f')
    return res


def convert_gethms(time_string):
    #ty_res = time.gmtime(time_string)
    #res =  time.strptime(time_string,'%H:%M:%S.%f')
    res = datetime.strptime(time_string, '%H:%M:%S.%f')
    return res.time()

def convert_seconds(time_string):
    time = time_string.split(':')
    totalSeconds = float(time[0]) * 3600 + float(time[1]) * 60 + float(time[2])
    return totalSeconds

def convert_from_t_dt(time):  
    return datetime.fromtimestamp(time).strftime('%H:%M:%S.%f')

