__author__ = 'Rok'

import gzip
import numpy
import csv
import datetime
import linear
import average

FORMAT = "%Y-%m-%d %H:%M:%S.%f"

def parsedate(x):
    if not isinstance(x, datetime.datetime):
        x = datetime.datetime.strptime(x, FORMAT)
    return x

def tsdiff(x, y):
    return (parsedate(x) - parsedate(y)).total_seconds()

def tsadd(x, seconds):
    d = datetime.timedelta(seconds=seconds)
    nd = parsedate(x) + d
    return nd.strftime(FORMAT)

def getHourDec(d):
    hour = parsedate(d)
    return (hour - hour.replace(hour=0,minute=0,second=0)).seconds / 3600.

def find(primer ,d):
    for ins in d:
        if (primer == ins[0]):
            return ins[1]

#main

f = gzip.open("train.txt.csv.gz", "rt")
reader = csv.reader(f, delimiter="\t")
next(reader)
data = [ d for d in reader ]
count = len(data)

l = average.SeparateBySetLearner(average.AverageTripLearner())
c = l(data)

linije = set(tuple(d[2:5]) for d in data)

napovedniki = []
lr = linear.LinearLearner(lambda_=1.)

for l in linije:
    xl = [] #odhodi posameznega modela; tuple(linija,koef)
    yl = [] #prihodi posameznega modela

    for d in data:
        ucni_primer = tuple(d[2:5]) #posamezen primer, ID linije
        if (ucni_primer == l):
            xl.append([getHourDec(d[-3]), (getHourDec(d[-3]))**2, getHourDec(d[-3])**3, (getHourDec(d[-3]))**4, getHourDec(d[-3])**5])
            yl.append(tsdiff(d[-1],d[-3]))

    napovednik = lr(numpy.array(xl),numpy.array(yl)) #izracun napovedi
    napovedniki.append([ucni_primer, napovednik])

f = gzip.open("test.txt.csv.gz", "rt") #napovedovanje
reader = csv.reader(f, delimiter="\t")
next(reader)

fo = open("reg.txt", "wt")
for r in reader:
    testni_primer = tuple(r[2:5])
    napovednik = find(testni_primer, napovedniki)

    if(napovednik != None):
        n = napovednik(numpy.array(([getHourDec(r[-3]), (getHourDec(r[-3]))**2, getHourDec(r[-3])**3, (getHourDec(r[-3]))**4, getHourDec(r[-3])**5])))
        fo.write(tsadd(r[-3], n) + "\n")
    else:
        fo.write(tsadd(r[-3], c(r)) + "\n")

fo.close()