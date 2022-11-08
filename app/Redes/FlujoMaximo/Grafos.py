import igraph as ig
def ingresarGrafoSinPesos(directed=False):
    vertices: list = []

    respuesta = "si"
    print("Cada numero representa el numero de arco")
    print("Ingreso de los arcos del grafo (0 es el inicial):")
    while(respuesta == "si"):
        nodoInicial = int(input("\tIngrese el primer nodo del arco: "))
        nodoFinal = int(input("\tIngrese el segundo nodo del arco: "))
        vertices.append([nodoInicial, nodoFinal])
        respuesta = input("¿Desea ingresar arcos? si/no: ")

    return ig.Graph(vertices,directed)

def ingresarGrafoConPesos():
    vertices: list = []
    pesos = []

    respuesta = "si"
    print("Cada numero representa el numero de arco")
    print("Ingreso de los arcos del grafo (0 es el inicial):")
    while(respuesta == "si"):
        nodoInicial = int(input("\tIngrese el primer nodo del arco: "))
        nodoFinal = int(input("\tIngrese el segundo nodo del arco: "))
        vertices.append([nodoInicial, nodoFinal])
        peso = float(input("\tIngrese el peso del arco: "))
        pesos.append(peso)
        respuesta = input("¿Desea ingresar arcos? si/no: ")

    grafo = ig.Graph(vertices)
    grafo.es["peso"] = pesos

    return grafo
