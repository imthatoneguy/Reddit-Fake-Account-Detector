import os
import csv
import datetime
import time

import pickle
import gib_detect_train

model_data = pickle.load(open('gib_model.pki', 'rb'))

csvFile = open("D:\\69M_reddit_accounts.csv")
vFile = open("D:\\RealUsers.csv","w")
csvReader = csv.reader(csvFile)
interestingUsers = []
boringUsers = []

d = int(time.mktime(datetime.datetime(2015,1,1).timetuple()))
dE = int(time.mktime(datetime.datetime(2016,1,1).timetuple()))

i = 0
for row in csvReader:
    try:
        if int(row[4])>100:
            vFile.write((row[1])+' ')
            i+=1
            if i > 10:
                vFile.write('\n')
                i = 0
        else:
            pass
    except:
        pass

vFile.close()
csvFile.close()



    
