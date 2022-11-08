import numpy as np
lamda = int(input("ingrese valor de lambda:"))
mu = int(input("ingrese valor de mu:"))
Q_servidores = int(input("ingrese cantidad de servidores:"))

P = []
C = []

factor_de_uso = lamda/mu  
L = lamda/(mu-lamda)  
W = 1/(mu-lamda) 
Wq = lamda/(mu*(mu-lamda)) 
Lq = Wq * lamda  


P0 = 1-factor_de_uso
P.append(P0)
pacum = []
for i in range(1, 17):
    Ultimo_P = P[-1]
    Nuevo_P = (1- Ultimo_P)*(Ultimo_P**(i-1))
    P.append(Nuevo_P)
    pacum.append(sum(P))


print(np.array(P))
print(np.array(pacum))
