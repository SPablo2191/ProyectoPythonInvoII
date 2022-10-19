#Implementar en el lenguaje de programación de su elección el algoritmo de Minimax.
import numpy as np
from Funciones import cargarPagos
from echo import Colors, echo


def maximin(arreglo):
    max = arreglo[0][0]
    list = []
    for i in range(len(arreglo)):
        for j in range(len(arreglo[i])):
            if (max > arreglo[i][j]):
                max = arreglo[i][j]
        list.append(max)
        max = 0
    return list


def minimax(arreglo):
    min = arreglo[0][0]
    list = []
    for i in range(len(arreglo)):
        for j in range(len(arreglo[i])):
            if (min < arreglo[j][i]):
                min = arreglo[j][i]
        list.append(min)
        min = 0
    return list


def maximoMinimos(a):
    max = a[0]
    for i in range(len(a)):
        if (max < a[i]):
            max = a[i]
    return max


def minimoMaximos(a):
    min = a[0]
    for i in range(len(a)):
        if (min > a[i]):
            min = a[i]
    return min


def equilibrio(a, b):
    if (a == b):
        echo('punto silla', color=Colors.GREEN,end='')
        echo(f' => {a}', color=Colors.YELLOW)
    else:
        echo('juego inestable', color=Colors.RED)




def main():
    echo('--------', color=Colors.RED, end='')
    echo('Teoria de Juegos: Maximin y Minimax ', color=Colors.GREEN, end='')
    echo('--------', color=Colors.RED)
    while (True):
        echo('ingrese numero de estrategias:', color=Colors.BLUE, end='')
        cantEstrategias = int(input())
        estrategJ1 = cargarPagos(cantEstrategias)
        echo('--------', color=Colors.RED, end='')
        echo('Matriz de estrategias', color=Colors.RED, end='')
        echo('--------', color=Colors.RED)
        matEstrategias = np.array(estrategJ1)
        print(matEstrategias)
        minimos = maximin(matEstrategias)
        maximos = minimax(matEstrategias)
        max = maximoMinimos(minimos)
        min = minimoMaximos(maximos)
        echo('Resultado:', color=Colors.BLUE, end='')
        equilibrio(max, min)
        pregunta = input("desea ingresar otro ejercicio? s/n: ")
        if(pregunta.lower() == 'n'):
            break

# Ejemplo [-3, -2,6], [2, 0, 2],[3, -2, -4]]


main()
