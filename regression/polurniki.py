import gzip
import csv
import lpputils

f = gzip.open("test.txt.csv.gz", "rt")
reader = csv.reader(f, delimiter="\t")
next(reader) #skip legend

fo = open("polurniki.txt", "wt") #samo prebere podatki in jim doda 30min = 1800s
for l in reader:
    fo.write(lpputils.tsadd(l[-3], 30*60) + "\n")
fo.close()
#pride v postev ko bom imel zgrajen model da dodam pot in vidim za koliko sem se zmotil