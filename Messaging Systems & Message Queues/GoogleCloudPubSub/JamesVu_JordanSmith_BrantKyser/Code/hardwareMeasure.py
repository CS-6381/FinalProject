# pip install py-cpuinfo
import psutil, time
loopCount = 1
waitTime = 5
cpuArr = []
ramArr = []
storageArr = []

def getCPU():
    cpuArr.append(psutil.cpu_percent())
    maxCPU = max(cpuArr)
    total = sum(tuple(cpuArr))
    averageCPU = total / len(cpuArr)
    return {'maxCPU: ': maxCPU, 'averageCPU': averageCPU}

def getRAM():
    ramArr.append(psutil.virtual_memory().percent)
    maxRAM = max(ramArr)
    total = sum(tuple(ramArr))
    averageRAM = total / len(ramArr)
    return {'maxRAM: ': maxRAM, 'averageRAM': averageRAM}

def getStorage():
    storageArr.append(psutil.disk_usage('/').used)
    maxStorage = max(storageArr)
    total = sum(tuple(storageArr))
    averageStorage = total / len(storageArr)
    return {'maxStorage: ': maxStorage, 'averageStorage': averageStorage}

while True:
    print("Measuring hardware - iteration: " + str(loopCount))
    print(getCPU())
    print(getRAM())
    print(getStorage())
    print("Waiting ...")
    loopCount = loopCount + 1
    time.sleep(waitTime)