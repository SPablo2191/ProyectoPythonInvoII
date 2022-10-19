# Implementar en el lenguaje de programación de su elección el algoritmo de eliminación de dominadas.
import numpy as np
from Funciones import cargarPagos
from echo import Colors, echo


def dominadasJ1(mat):
    for i in range(len(mat)):
        #print(f"estrategia referente: {mat[i]}")
        e1 = mat[i]
        breaker = False
        try:
            for j in range(i+1, len(mat)):
                band = True
                eo = mat[j]
                #print(f"estrategia a comparar {eo}")
                for k in range(len(eo)):
                    if (e1[k] < eo[k]):
                        band = False
                        break
                if (band):
                    #print(f"estrategia a eliminar: {mat[j]}")
                    mat = np.delete(mat, j, 0)
                    breaker = True
                    break
        except Exception as e:
            print(f"error => {e}")
        if (breaker):
            break
    return mat


def dominadasJ2(mat):
    for i in range(len(mat)):
        #print(f"estrategia referente: {mat[:,i]}")
        e1 = mat[:, i]
        breaker = False
        try:
            for j in range(len(mat)+1):
                #print(j, len(mat))
                band = True
                eo = mat[:, j]
                #print(f"estrategia a comparar {eo}")
                for k in range(len(eo)):
                    if (e1[k] > eo[k] or j == i):
                        #print(f"entro algo: {eo[k]}")
                        band = False
                        break
                if (band):
                    #print(f"estrategia a eliminar: {mat[:,j]}")
                    try:
                        mat = np.delete(mat, j, j-1)
                    except:
                        mat = np.delete(mat, j, j)
                    #print(f"matriz obtenida:{mat}")
                    breaker = True
                    break
        except Exception as e:
            print(f"error => {e}")
        if (breaker):
            #print("entro al breaker")
            break
    return mat


def estrategiaDominada(matEstrategias):
    while (len(matEstrategias) != 1):
        matEstrategias = dominadasJ1(matEstrategias)
        matEstrategias = dominadasJ2(matEstrategias)
    return matEstrategias


def main():
    echo('--------', color=Colors.RED, end='')
    echo('Teoria de Juegos: Estrategia de dominadas ', color=Colors.GREEN, end='')
    echo('--------', color=Colors.RED)
    while (True):
        echo('ingrese numero de estrategias:', color=Colors.BLUE, end='')
        cantEstrategias = int(input())
        estrateg = cargarPagos(cantEstrategias)
        echo('--------', color=Colors.RED, end='')
        echo('Matriz de estrategias', color=Colors.RED, end='')
        echo('--------', color=Colors.RED)
        # matEstrategias = np.array([[1, 2, 4], [1, 0, 5], [0, 1, -1]])
        matEstrategias = np.array(estrateg)
        print(matEstrategias)
        print(matEstrategias)
        matPago = estrategiaDominada(matEstrategias)
        echo('Resultado:', color=Colors.BLUE, end='')
        print(matPago)
        pregunta = input("desea ingresar otro ejercicio? s/n: ")
        if (pregunta.lower() == 'n'):
            break


main()
