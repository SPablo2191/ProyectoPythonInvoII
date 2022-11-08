import nashpy as nash
import numpy as np

def ingresarMatriz (filas: int, columnas: int):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(float(input(f"\tIngrese valor de la posición {i}, {j}: ")))
        matriz.append(fila)
    return matriz

def mostrarMatriz(matriz):
    for fila in matriz:
        print(f"\t{fila}")



# premios ejemplos programacion lineal
premios = np.array([
    [3, -1, -3],
    [-2, 4, -1],
    [-5, -6, 2]
])

# premios piedra papel o tijera
# premios = np.array([
#     [0, -1, 1],
#     [1, 0, -1],
#     [-1, 1, 0]
# ])

# premios dilema del prisionero
# premiosJugador1 = np.array([
#     [-1, -5],
#     [0, -4]
# ])

# premiosJugador2 = np.array([
#     [-1, 0],
#     [-5, -4]
# ])

premiosJugador1 = []
premiosJugador2 = []

tipoJuego = int(input("Ingrese 1 si quiere un juego de suma cero. Si no, ingrese 0: "))
while(tipoJuego != 1 and tipoJuego != 0):
    print("Opción Inválida.")
    tipoJuego = int(input("Ingrese 1 si quiere un juego de suma cero. Si no, ingrese 0: "))
    

filas = int(input(f"Ingrese la cantidad de estrategias para el jugador 1: "))
columnas = int(input(f"Ingrese la cantidad de estrategias para el jugador 2: "))

rps = []


if(tipoJuego == 1):
    print("Ingrese la matriz de pagos:")
    premiosJugador1 = ingresarMatriz(filas, columnas)
    rps = nash.Game(np.array(premiosJugador1))

elif(tipoJuego == 0):
    print("Ingrese la matriz de pagos para el Jugador 1:")
    premiosJugador1 = ingresarMatriz(filas, columnas)
    print("Ingrese la matriz de pagos para el Jugador 2:")
    premiosJugador2 = ingresarMatriz(filas, columnas)
    rps = nash.Game(premiosJugador1, premiosJugador2)
else:
    print("Opción invalida")

if(rps.zero_sum):
    print(f"Matriz de pagos:")
    mostrarMatriz(rps.payoff_matrices[0])
else:
    print(f"Matriz de pagos para el jugador 1:")
    mostrarMatriz(rps.payoff_matrices[0])

    print(f"Matriz de pagos para el jugador 2:")
    mostrarMatriz(rps.payoff_matrices[1])

equilibrios = rps.support_enumeration()

lista = list(equilibrios)
print("Probabilidad de usar cada estrategia para el jugador 1:")
for index, prob in enumerate(lista[0][0]):
    print(f"\tEstrategia {index + 1}: {prob}")

print("Probabilidad de usar cada estrategia para el jugador 2:")
for index, prob in enumerate(lista[0][1]):
    print(f"\tEstrategia {index + 1}: {prob}")