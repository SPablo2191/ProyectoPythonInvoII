import numpy as np


def FloydAlgoritmo(Grafo):
    matriz = np.array(Grafo)
    for i in range(vertices):
        for j in range(vertices):
            for k in range(vertices):
                matriz[j][k] = min(matriz[j][k], matriz[j][i] + matriz[i][k])
    print(matriz)

# Ejemplo de la materia
vertices = 5
INF = 9999
g = [[0, 3, 10, INF, INF],
     [3,  0, INF, 5, INF],
     [10, INF, 0, 6, 15],
     [INF, 5, 6,  0, 4],
     [INF, INF, INF, 4, 0]
     ]
aux = g
print('Original:')
print(np.array(aux))
print('Resultado:')
FloydAlgoritmo(g)
