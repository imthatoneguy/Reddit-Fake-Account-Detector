import os
import csv
import datetime
import time

import pickle
import gib_detect_train

model_data = pickle.load(open('gib_model.pki', 'rb'))

csvFile = open("D:\\69M_reddit_accounts.csv")
vFile = open("D:\\AllSus.csv","w")
csvReader = csv.reader(csvFile)
interestingUsers = []
boringUsers = []
totalusers = {}
ratioUsers = {}
d = int(time.mktime(datetime.datetime(2015,1,1).timetuple()))
dE = int(time.mktime(datetime.datetime(2016,1,1).timetuple()))

i = 0

def gibgib ( username ):
    model_mat = model_data['mat']
    threshold = model_data['thresh']
    return (gib_detect_train.avg_transition_prob(username, model_mat) < threshold)

for row in csvReader:

    if i != 0:
        row[2] = datetime.datetime.utcfromtimestamp(int(row[2]))
        if gibgib(row[1]):
            vFile.write((row[1])+'\t'+(str(row[2]))+'\n')       
            interestingUsers.append(row)
            try:
                totalusers[str(row[2].year)+str(row[2].month)] += 1
            except:
                totalusers[str(row[2].year)+str(row[2].month)] = 1
        else:
            try:
                totalusers[str(row[2].year)+str(row[2].month)] += 1
            except:
                totalusers[str(row[2].year)+str(row[2].month)] = 1
    else:
        i+=1

vFile.close()
csvFile.close()

useryears = {}
for u in interestingUsers:
    try:
        useryears[str(u[2].year)+str(u[2].month)] += 1
    except:
        useryears[str(u[2].year)+str(u[2].month)] = 1
for y in useryears:
    ratioUsers[y] = useryears[y]/float(totalusers[y])
    print(y[0:4]+"-"+y[4:20].zfill(2)+"\t"+str(useryears[y])+"\t"+str(totalusers[y])+"\t"+str(ratioUsers[y]))

