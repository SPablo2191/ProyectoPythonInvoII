# Implementar en el lenguaje de programación de su elección el algoritmo de eliminación de dominadas.
import numpy as np
from Funciones import cargarPagos
from echo import Colors, echo
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
        echo('Resultado:', color=Colors.BLUE, end='')
        pregunta = input("desea ingresar otro ejercicio? s/n: ")
        if(pregunta.lower() == 'n'):
            break

main()