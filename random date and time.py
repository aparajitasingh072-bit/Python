import random
import time

def getRandomdate(startdate, enddate ):
    print("printing random date between", startdate, " and ", enddate)
    randomGenerator = random.random()
    dateFormat = '%m/%d/%Y'

    starttime = time.mktime(time.strptime(startdate, dateFormat))
    endtime = time.mktime(time.strptime(enddate, dateFormat))

    randomtime = starttime + randomGenerator * (endtime - starttime)
    randomdate = time.strftime(dateFormat, time.localtime(randomtime))
    return randomdate
print ("Random date = ", getRandomdate("1/1/2016", "12/12/2018"))