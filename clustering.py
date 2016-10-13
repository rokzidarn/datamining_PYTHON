__author__ = 'Rok'
import csv
from math import sqrt
from itertools import product, combinations
import sys

avg = lambda lst: sum(lst)/len(lst)

def column(matrix, i): #glasovi posamezne drzave, stolpec
    return [row[i] for row in matrix]

class Clustering:
    linkages = {"min": min, "max": max, "average": avg}

    def __init__(self, file_name, linkage="average"):
        #read data from file
        i=0
        self.voters = [] #atributi, drzave
        self.points = []
        data2d = [] #tocke vseh drzav

        for row in csv.reader(open("eurovision.csv", 'rb')): #branje, tvorba objektov
            if i==0:
                for i in range(16,63): #atributi, drzave
                    voter = [row[i]]
                    self.voters.append(voter) #seznam, seznamov, vsaka drzava svoj seznam
                    i=i+1
            else:
                data = [] #tocke posamezne drzave
                for i in range(16,63): #osnovne tocke
                    if row[i]=="":
                        data.append(-1) #da vem katere treba preskocit
                    else:
                        data.append(float(row[i]))
                data2d.append(data)

        k = 0 #transponiram, da dobim stolpce za posamezno drzavo -> funkcija column
        for v in self.voters: #dodajanje tock posamezni glasovalki
            self.points.append(column(data2d,k))
            k=k+1

        #popravim MONT, SER, SER&MONT (29,37,38)
        for i in range(74,146):
            self.points[29][i]=self.points[38][i]
            self.points[37][i]=self.points[38][i]

        self.linkage = self.linkages[linkage]
        self.clusters = [[i] for i in range(len(self.points))]

    def row_distance(self, r1, r2):
        # problem je normalizacija, v primeru ko so ravno izmenicne -1
        sum = 0
        k = 0
        for x, y in zip(self.points[r1], self.points[r2]):
            if(x != -1 and y != -1):
                sum = sum + ((x-y)**2)
                k = k + 1

        if(sum == 0):
            return sys.maxint
        else:
            return sqrt(sum/k)

    def cluster_distance(self, c1, c2):
        return avg([self.row_distance(x,y) for x,y in product(c1,c2)])

    def closest_clusters(self):
        dist, close = min((self.cluster_distance(*c), c) for c in combinations(self.clusters, 2))
        return dist, close

    def run(self): #clustering
        joining = []
        while len(self.clusters) > 1:
            dist, close = hc.closest_clusters()
            pair = [close[0],close[1]]

            for i in range(len(pair)):
                for j in range(len(pair[i])):
                    print self.voters[pair[i][j]],
                if i != len(pair)-1:
                    print " + ",
            print ""

            #i = c1
            #j = c2
            #for x in range(len(self.clusters)):
                #if x != i or x != j:
                    #joining.append(self.clusters[x])
            #joining.append([self.clusters[i],self.clusters[j]])

            self.clusters = [x for x in self.clusters if x not in pair] + [pair[0] + pair[1]]

#main

hc = Clustering("eurovision.csv")
hc.run()

print "-----------------------------------------------------------------------------------------------------------------------"
#izpis

def offset(i):
    for k in range(3*i):
        print " ",

def line(i):
    for k in (range(3*i+1)):
        print " ",
    print "----|"

def output(ime,sez, i):
    if(isinstance(sez,list)):
        for l in range(len(sez)):
                output(ime,sez[l],i+1)
    else:
        offset(i)
        print "-----",ime[sez-1]
        line(i-1)

ime = ["SLO","CRO","ITA","HUN","GER","UK","RUS"]
sez = [[[3],[4]],[7],[[[1],[2]],[[5],[6]]]]
output(ime,sez,0)
