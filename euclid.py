__author__ = 'Rok'
import random

def evkl_pred(v1, v2): # deljenje pred korenjenjem
    diffs = [(a-b)**2 for a,b in zip(v1, v2)
        if a != None and b != None ]
    return (sum(diffs)/len(diffs))**0.5

def evkl_po(v1, v2): # deljenje po korenjenju
    diffs = [(a-b)**2 for a,b in zip(v1, v2)
        if a != None and b != None ]
    return (sum(diffs)**0.5)/len(diffs)

v1 = [ random.random() for _ in range(1000) ]
v2 = [ random.random() for _ in range(1000) ]

#spustim vsako drugo vrednost
v2_manjka = [ e if i % 2 == 0 else None for i,e in enumerate(v2) ]

print("Deljenje pred korenjenjem")
print("Cela seznama: ", evkl_pred(v1, v2))
print("Z manjkajocimi:", evkl_pred(v1, v2_manjka))
print()
print("Deljenje po korenjenju")
print("Cela seznama: ", evkl_po(v1, v2))
print("Z manjkajocimi:", evkl_po(v1, v2_manjka))