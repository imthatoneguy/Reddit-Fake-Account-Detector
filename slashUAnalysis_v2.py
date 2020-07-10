import os
import csv
import datetime
import time

import pickle
import gib_detect_train

model_data = pickle.load(open('gib_model.pki', 'rb'))

csvFile = open("D:\\69M_reddit_accounts.csv")
vFile = open("D:\\Twelvsies.csv","w")
csvReader = csv.reader(csvFile)
interestingUsers = []
boringUsers = []

d = int(time.mktime(datetime.datetime(2015,1,1).timetuple()))
dE = int(time.mktime(datetime.datetime(2016,1,1).timetuple()))

i = 0

def gibgib ( username ):
    model_mat = model_data['mat']
    threshold = model_data['thresh']
    return (gib_detect_train.avg_transition_prob(username, model_mat) < threshold)

for row in csvReader:
    t = 0
    try:
        t = int(row[2])
    except:
        t = 0
    if t < dE and t > d and len(row[1]) == 12 and row[4] == '0' and row[5] == '0':

        try:
            if gibgib(row[1]):
                interestingUsers.append(row)
                vFile.write((row[1])+'\t'+(str(datetime.datetime.utcfromtimestamp(int(row[2]))))+'\n')
            else:
                pass
        except:
            pass
vFile.close()
csvFile.close()
