def ingresarMatriz(filas: int, columnas: int):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(float(input(f"Ingrese valor de la posición {i}, {j}: ")))
        matriz.append(fila)
    return matriz

def mostrarMatriz(matriz):
    for fila in matriz:
        print(f"\t{fila}")

