__author__ = 'Rok'

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Basket(object):
    bid = 0

    def __init__(self, owner=""): #konstruktor
        self.owner = owner
        Basket.bid += 1
        self.id = Basket.bid #razredna splemenljivka, kot static
        self.content = [] #seznam artiklov, par(artikel, kolicina)

    def add(self, item, quantity):
        self.content.append((item, quantity))

    def add_multiple(self, aList):
        for item, quantity in aList:
            self.add(item, quantity)

    def total(self):
        tot = 0
        for item, quantity in self.content:
            tot += quantity * item.price
        return tot

    def remove_multiple(self, aList):
        for item in aList:
            self.remove(item)

class EnhancedBasket(Basket): #dedovanje
    def remove(self, item):
        for art in reversed(self.content):
            if art[0] == item:
                self.content.remove(art)

    def add(self, item, quantity):
        print "izdelek '%s', kolicina %s: cena %.2f" % \
              (item.name, quantity, item.price*quantity)
        Basket.add(self, item, quantity)

    def __str__(self): #izpis, toString
        names = []
        for item, quantity in self.content:
            names.append("%s (%s)" % (item.name, quantity))
        return "<" + ", ".join(names) + ">"

    def __contains__(self, s):
        for item, quantity in self.content:
            if item.name == s:
                return True #ni treba vracat False, ker ce ni True vrne None, kar je v bistvu False

    def __len__(self):
        return len(self.content)


#-----------------------------------------------------------------------------------------------------------------------
#main

b = EnhancedBasket()
banane = Item("banane", 1.20)
b.add(banane, 20)
b.add(Item("mleko", 1.40), 12)

print b.total()
print b.content
b.remove_multiple([banane])
print b.content

plenice = Item("plenice", 3.80)

dodaj_v_b = b.add #vezana funkcija na objekt b
dodaj_v_b(plenice, 4) #objekt, oziroma spremenljivka, ki je kar funkcija
#poznamo tudi nevezane metode

print b.__contains__("mleko")

#casting
print int(3.2)
print int("2a", 16) #hexa
print int("100111", 2) #binarno

t=(1,2,3)
t2=list(t) #tuple pretvori v list
print t2

print set("tudi kaj drugega") #niz pretvori v mnozico
print sorted(list(set("tudi kaj drugega")))
print "".join(sorted(list(set("tudi kaj drugega"))))

seznamImen = map(lambda t: t[0].name, b.content) #ustvari nov seznam na podlagi prejsnega, brez for zanke
drageReci = filter(lambda t: t[0].price > 10, b.content) #filtrira na podlagi pogoja, delna operacija mapa
vsota = reduce(lambda x, y: x+y, map(lambda t: t[0].price * t[1], b.content)) #gre cez celoten seznam a na koncu vrne le en objekt, rezultat ne seznam
print vsota
#all (vsi elementi resnicni), any (vsaj eden resnicen), max, min, sorted, reversed

#izpeljana seznama
#seznamImen = [t[0].name for t in b.content]
#drageReci = [t for t in b.content if t[0].price > 10]


