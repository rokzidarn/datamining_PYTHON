__author__ = 'Rok'

from math import sqrt
from collections import Counter
from unidecode import unidecode
from itertools import combinations
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

def do_nothing(k):
    pass

def cosine_distance(v1,v2,d1,d2):
    #izracuna razdaljo, imenovalec vsebuje vse vrednosti, stevec le presek
    sumxx = sum(d1[i]**2 for i in range(len(d1)))
    sumyy = sum(d2[i]**2 for i in range(len(d2)))
    sumxy = sum(v1[i]*v2[i] for i in range(len(v1)))

    return 1-(sumxy/(sqrt(sumxx)*sqrt(sumyy)))

def symbol_freq(text, k=2): #k = 2,3,4
    groups = [text[i: i+k] for i in range(len(text)-k+1)]#tvori nize dolzine k
    freq_dict = Counter(groups) #belezi stevilo ponovitev zgornjih nizov

    return freq_dict

def create_intersection(d1, d2): #ohrani samo nize, ki se pojavijo v obeh
    k1=set(d1.keys()); k2=set(d2.keys())
    intersection = k1 & k2

    id1 = {k:d1[k] if k in d1 else do_nothing() for k in intersection}
    id2 = {k:d2[k] if k in d2 else do_nothing() for k in intersection}

    return id1, id2

def distance_matrix(text, languages):
    vect = []

    for c in combinations(languages, 2):
        i1 = languages.index(c[0]); i2 = languages.index(c[1]) #razlicna jezika
        f1 = symbol_freq(text[i1],2); f2 = symbol_freq(text[i2],2) #frekvence jezikov
        id1, id2 = create_intersection(f1,f2)
        dist = (cosine_distance(list(id1.values()), list(id2.values()), list(f1.values()), list(f2.values())))
        vect.append(dist) #1D

    return vect

def analyze(files):
    languages = [ i[8:11] for i in files]

    text = []
    for i in range(len(files)):
        lang_text = unidecode(open(files[i],"r",encoding="utf-8").read().replace('\n'," ").replace(',',"").replace('.',"").replace(';',"").lower())
        text.append(lang_text) #print(languages[i],": ",lang_text)

    vect = distance_matrix(text, languages)
    linkage_matrix = linkage(vect, 'average')

    plt.figure(101) #graficen prikaz
    plt.subplot(1,1,1)
    plt.title("LANGUAGE SIMILARITY")
    plt.xlabel('COUNTRIES')
    plt.ylabel('DISTANCE')
    dendrogram(linkage_matrix, color_threshold=1, truncate_mode='lastp', labels=languages, distance_sort='descending')
    plt.show()

def find_language(files):
    unknown = unidecode(open("unknown/hng.txt","r",encoding="utf-8").read().replace('\n'," ").replace(',',"").replace('.',"").replace(';',"").lower())
    text = []

    for i in range(len(files)):
        lang_text = unidecode(open(files[i],"r",encoding="utf-8").read().replace('\n'," ").replace(',',"").replace('.',"").replace(';',"").lower())
        text.append(lang_text)

    dist_min = 1
    for i in range(len(text)):
        f = symbol_freq(text[i],2); fu = symbol_freq(unknown,2) #frekvence jezikov
        id1, id2 = create_intersection(f,fu)
        dist = (cosine_distance(list(id1.values()), list(id2.values()), list(f.values()), list(fu.values())))
        #print(dist, (files[i])[6:9])
        if dist < dist_min:
            dist_min = dist; lang = (files[i])[6:9]

    print("Language:",lang, "(",1-dist_min,")")

#main
files = ["ready/slv.txt", "ready/eng.txt", "ready/ger.txt", "ready/rus.txt", "ready/slo.txt", "ready/ukr.txt", "ready/itn.txt",
         "ready/grk.txt", "ready/frn.txt", "ready/jpn.txt", "ready/dut.txt", "ready/hng.txt", "ready/den.txt", "ready/mkj.txt",
         "ready/por.txt", "ready/lux.txt", "ready/czc.txt", "ready/trk.txt", "ready/rum.txt", "ready/uzb.txt"]

ufiles = ["unknown/slv.txt", "unknown/uzb.txt", "unknown/ukr.txt", "unknown/trk.txt", "unknown/slo.txt", "unknown/rus.txt", "unknown/rum.txt",
          "unknown/por.txt", "unknown/lux.txt", "unknown/jap.txt", "unknown/itn.txt", "unknown/grk.txt", "unknown/ger.txt", "unknown/frn.txt",
          "unknown/eng.txt", "unknown/dut.txt","unknown/den.txt", "unknown/czc.txt","unknown/mkj.txt", "unknown/hng.txt"]

analyze(ufiles)
find_language(files)