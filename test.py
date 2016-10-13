__author__ = 'Rok'

tim = lambda x: (x-5)**2 + 3
print(tim(8))

def d(x0, eps=1e-5): #diferencial
    return (tim(x0+eps) - tim(x0-eps))/(2*eps)

x0=8
for i in range(10):
    print("%.3f " % x0)
    x0 = x0 - 0.2 * d(x0)
    # 0.2 = stopnja ucenja, lambda -> tezko dolocit, hocem cim manjso konvergenco

#------------------------------------

import numpy as np
import matplotlib.pyplot as plt

x=np.arange(0,10,0.1)
y=tim(x)
plt.plot(x,y,"k-")
plt.show()

#------------------------------------

import Orange

data = Orange.data.Table("data/lin-painted.tab")
print(data)

X, y=data.X, data.Y #x=matrika
print(y) #vektor

print(X.shape) #vrne obliko
X=np.column_stack((np.ones(X.shape[0]),X)) #enke na prvo mesto
plt.plot(X[:, 1], y, "o")

theta=np.zeros(X.shape[1]) #init
m=X.shape[0]
alpha=0.1 #learning rate
for _ in range(1000):
    theta=theta-(alpha/m)*(X.dot(theta)-y).dot(X) #dot je skalarni produkt

mm=np.array([min(X[:,1]), max(X[:,1])])
Xmm=np.column_stack((np.ones(2)),mm)

plt.plot(X[:, 1], y, "o")
plt.plot(Xmm[:,1], Xmm.dot(theta))
plt.show()
print(Xmm.dot(theta))

def J(X,y,theta):
    return 0.5*sum((X.dot(theta)-y)**2) #kriterijska funkcija



