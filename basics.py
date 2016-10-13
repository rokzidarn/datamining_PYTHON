__author__ = 'Rok'

# FUNKCIJA ord()
# FUNKCIJA readlines()

import math
import urllib
import cmath  # kompleksna stevila
import test  # lahko importam kar svoje projekte

global spremenljivka
spremenljivka = 123123


# funkcija lahko vraca vec vrednosti, terko
def fibonacci(n, a=1, b=1):  # ze definirani argumenti vnaprej
    for i in range(n):  # gre od 0 dalje
        a, b = b, a + b  # najprej izracuna, torej a+b, nato priredi a=b, nato v b shrani kar je izracunal b=a+b
    return a


def fibonacci(n):  # generatorska funkcija, v bistvu ze takoj vrne iterator
    a = b = 1
    for i in range(n):  # pri zanki se najprej ustvari iterator, nato se klice next()
        yield a
        # yield je kot return vendar se ne konca temvec vrne vrednost in v primeru ponovnega klica se spet izvaja
        a, b = b, a + b


def binomRec(n, k):
    if k == 0 or k == n:
        return 1
    return binomRec(n - 1, k - 1) + binomRec(n - 1, k)


def vejitev():  # argument je lahko tudi funkcija
    a = 10
    b = 12
    if a > 12 or b == 42:
        a = 12
        print a
    elif a < 0 or b == 2:
        a = 0
        print b
    else:
        a = b = 0
        print "a+b=", a + b


def deljivost():
    a = b = 1
    for i in range(100):
        if a % 1131 == 0:
            print a, "je deljiv s 1131"
            break  # ce se ne izvede break, gremo na else stavek
        a, b = b, a + b
    else:  # posebnost pythona lahko v povezavi z zanko in neizvedenim break
        print "Nobeno od prvih 100 Fibonaccijevih stevil ni deljivo s 1131"


def f(a, b, c=3, *arg):  # * pomeni terko argumentov, torej ne vemo koliko, **pomeni slovar
    print "a=%s, b=%s, c=%s, arg=%s" % (a, b, c, arg)


def povprecje(l):  # sprozitev izjeme
    if not l:
        raise ZeroDivisionError("seznam je prazen")
    return sum(l) / len(l)


def izpisiPoprecje(l):  # lovljenje izjem
    try:
        p = povprecje(l)
        print p
    except ZeroDivisionError:
        print "Ne bo slo, seznam je prazen"
    except:
        print "Neznana napaka."


def mnozenje_s(k):
    def f(x):
        return x * k

    return f


# -----------------------------------------------------------------------------------------------------------------------
# main

print 'Hello, world!'

print math.log(2.7)
a = max(1, 23, 2, 7);
print a  # vec ukazov v isti vrsti

print fibonacci(6)
print fibonacci(6, 4, 10)  # prepise definirane argumente funkcije z novimi
print fibonacci(4, "a", "t")  # deluje tudi na crkah

s = 138416847845213516846415187879854321315987717184529598465165
from math import log

print log(s, 10)
print len(str(s))

print (1 + 2j) * (4 + 3j)  # kompleksna stevila
# konstante pisane z veliko zacetnico, void funkcije vracajo None
bool = True
c1, c2 = "xy"  # razpakira string na dve spremenljivke, terko

print 2 ** 10  # potenciranje
print True or False
print 5 and 12
print 1 < 2 < 3 < 4 != 5 < 4

string = "moje ime je rok"
print string.split(" ")

print range(5, 12)
print range(5, 122, 4)

l = ["Miran", "Miha", "Mitja", ]  # vejica pomeni, da lahko dodajam na konec
for e in l:  # izpis enakovreden kot pri tabelah a[i]
    print e  # if "Miran" in l; ce se nahaja notri

print binomRec(5, 2)

f = file("slika.jpg", "rb")
s = (f.read())
print s[:30], len(s)  # prvih 30 znakov
file("kopija.gif", "wb").write(s)  # pisanje

for l in file("dat.txt", "r"):  # bere po vrsticah + zmeraj doda \n
    print l

import sys
# sys.stdout = file("c:/log.txt", "wt") #preusmeritev stdout
sys.stdout.write("Rok\n")

# indeksiranje: s[0], s[-1] je zadnji, s[2:5] so 2.,3.,4. element
# direkten index prepise element, pri inkdeksiranju lahko dodam tudi korak

# operacije: delete(), pop(), insert(), append(), extend()
# count(), index(), reverse(), sort()

print [1, 2, 3, 5] < [1, 2, 4]  # primerja leksikografsko po elementih, drugace pa gleda tudi dolzino

k = []
for i in range(5):
    k.append([])  # seznam 5 praznih seznamov ali l = [[] for i in range(5)]

print tuple("miran")  # terki ne mores dodajati elementov, oklepaji
l = ["Ana", "Berta", "Cilka", "Dani"]
print "-".join(l)  # vse zdruzi in vmes doda -

print "Koliko je %i/%i? Nekako %.3f." % (11, 5, 2.2)  # % znak potrebuje terko
# %s je univerzalen, lahko dodas karkoli
ime = "rok"
print ime.endswith("k")

a = b = "Ana"
print a
b += "Marija"  # pripenjanje
print b

# s.decode("utf-8") za sumnike

d = {"Miha": 12, "Miran": 29, "Matevz": None}  # slovar; notri so v bistvu terke
for k, v in d.items():
    print "%s\t%s" % (k, v)  # keys, values, items funkcije

del d["Miran"]
print d

d.setdefault("a", 48)  # doda nov element, vendar ce ze obstaja ne spremeni nic
d.get(42, "ga ni")  # ce ne najde elementa izpise ga ni

s = set([1, 2, 3])  # discard, clear, update, union, difference, intersection funkcije
# nespremenljiva mnozica je frozen set

l = ["rok", "ivanka", "ludvik", "lila"]
l.sort(lambda x, y: cmp(len(x),
                        len(y)))  # lambda funkcija, dejansko ni definirana zunaj, ampak napisana kar sproti v ukazu
print l

seznam = ["Humphrey Bogart", "Ingrid Bergman", "Paul Henreid", "Claude Rains",
          "Conrad Veidt", "Sidney Greenstreet", "Peter Lorre"]
print seznam
seznam.sort(lambda x, y: cmp((x.split()[-1]), (y.split()[-1])))  # sortira po priimkih
print seznam

f8 = mnozenje_s(8)
print f8(5)

seznam = ["rok", "zidarn", "krsko"]  # zanka for v bistvu implementira nek iterator
iterator = seznam.__iter__()
print "1. el:", iterator.next()
print "2. el:", iterator.next()

fib = fibonacci(12)  # generator vraca 1 element naenkrat, ne ustvari seznama
print fib.next(), fib.next(), fib.next(), fib.next(), fib.next(), fib.next(), fib.next()

l1 = ["a", "b", "c"]
l2 = [1, 2, 3]
l3 = "+-*"
print zip(l1, l2, l3)  # vrne istolezne pare oziroma terke

pevec = ["Predin", "Kreslin", "Lovsin"]
for i, pevec in enumerate(pevec):  # podobno kot zip, vendar z enumerate dobimo tudi indekse,
    print "Pevec %i: %s" % (i + 1, pevec)

print [x ** 2 for x in range(1, 10)]  # izpeljani seznam

[len(x) for x in l]  # enako je map(len,l)

print [line.strip() for line in file("dat.txt") if line]

print sum(x ** 2 for x in fibonacci(1000))  # generator vsote kvadratov fib stevil, ni potrebno shranjevati v seznam
# to je generatorski izraz
