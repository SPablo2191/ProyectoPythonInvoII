import numpy as np
lamda = int(input("ingrese valor de lambda:"))
mu = int(input("ingrese valor de mu:"))
Q_servidores = 1

P = []
C = []

rho = lamda/mu
L = lamda/(mu-lamda)  
W = 1/(mu-lamda)  
Wq = lamda/(mu*(mu-lamda))  
Lq = Wq * lamda  


P0 = 1-rho
P.append(P0)
pacum = []
for i in range(1, 40):
    Pn = P[-1]
    Pi = Pn * rho
    P.append(Pi)
    pacum.append(sum(P))


print(np.array(P))
print(np.array(pacum))
