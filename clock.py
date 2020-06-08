import datetime
import time


def getTime():
    time = str(datetime.datetime.now())

    time = time.split()
    time = time[1]
    time = " ".join(time)
    time = time.split()
    time = "".join(time[0:8])
    return time


"""
while True:
    getTime()
    time.sleep(0.5)
"""
