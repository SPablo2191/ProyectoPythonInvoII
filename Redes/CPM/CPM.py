import igraph as ig
import matplotlib.pyplot as plt

def ingresarTareas():

    tareas = []

    nombre = input(f"Ingresar nombre de la tarea (no ingrese nada para terminar): ")
    while(nombre != ""):
        duracion = float(input(f"Ingresar duracion de la tarea: "))

        prevs = []
        print(f"Ingreso predecesores de la tarea (no ingrese nada para terminar): ")
        prev = input("\tNombre tarea predecesora: ")
        while(prev != ""):
            prevs.append(prev)
            prev = input("\tNombre tarea predecesora: ")

        tareas.append([nombre, prevs, duracion])
        nombre = input(f"Ingresar nombre de la tarea (no ingrese nada para terminar): ")

    print("Tareas Ingresadas:")
    print("Nombre - Predecesoras - Duracion")
    for fila in tareas:
        print(fila)

    return tareas

def generarGrafo(tareas):
    # Lista de nodos del grafo
    nombreNodos = ["inicial"]
    for tarea in tareas:
        try:
            nombreNodos.index(tarea[0])
        except:
            nombreNodos.append(tarea[0])

        for predecesor in tarea[1]:
            try:
                nombreNodos.index(predecesor)
            except:
                nombreNodos.append(predecesor)
    # print(nodos)
    nodos = []
    arcos = []
    pesosArcos = []

    for nombre in nombreNodos:
        if(nombre != "inicial"):
            nodos.append(f"inicio{nombre}")
            nodos.append(f"fin{nombre}")
            arcos.append([len(nodos)-2, len(nodos)-1])
        else:
            nodos.append(nombre)

    for tarea in tareas:
        pesosArcos.append(tarea[2])
    

    for tarea in tareas:
        if(len(tarea[1]) == 0):
            try:
                # print("Poniendo los primeros arcos en 0")
                indiceInicioTarea = nodos.index(f"inicio{tarea[0]}")
                arcos.append([0, indiceInicioTarea])
                pesosArcos.append(0)
            except:
                print("error")

        

    for tarea in tareas:
        for predecesor in tarea[1]:
            try:
                indiceFinPredecesor = nodos.index(f"fin{predecesor}")
                indiceInicioTarea = nodos.index(f"inicio{tarea[0]}")
                arcos.append([indiceFinPredecesor, indiceInicioTarea])
                pesosArcos.append(0)
            except:
                print("error de busqueda de indice")


    # Lista de arcos del grafo (La cual se va a usar con igraph)

    # for tarea in tareas:
    #     for predecesor in tarea[1]:
    #         try:
    #             indiceTarea = nodos.index(f"inicio{tarea[0]}")
    #             indicePredecesor = nodos.index(f"fin{predecesor}")
    #             arcos.append([indicePredecesor, indiceTarea])
    #             pesosArcos.append(tarea[2])
    #         except:
    #             print("error")
            
    # print(arcos)
    # print(pesosArcos)

    grafo = ig.Graph(arcos, directed=True)
    grafo.vs["name"] = nodos
    grafo.es["duration"] = pesosArcos

    grafo.es["width"] = 2.0
    return grafo


def cpm(grafo: ig.Graph):
    # paso adelantado
    print("Calculo de paso adelantado:")
    cuadrado = 0

    for index, nodo in enumerate(grafo.vs):
        nodo["cuadrado"] = 0
        print(f"\tNodo {index}: {nodo['name']}, cuadrado: {nodo['cuadrado']}")
        entrantes = nodo.in_edges()
        listaCuadrados = []
        for en in entrantes:
            
            nodo["cuadrado"] += en.source["cuadrado"]
            print(en["duration"])



def mostrarGrafo(grafo: ig.Graph):
    fig, ax = plt.subplots()
    ig.plot(
        grafo, 
        fig = fig,
        target=ax, 
        layout="rt", 
        bbox=(3000,3000),
        # vertex_width = 0.4,
        vertex_color="lightblue",
        vertex_label = grafo.vs["name"],
        vertex_label_size = 12,
        edge_width=grafo.es["width"],
        edge_label=grafo.es["duration"],
        edge_background="white",
    )
    plt.show()

if __name__ == "__main__":
    # tareas = ingresarTareas()
    # tareas = [
    #     ['A', ['B', 'C', 'D'], 20.0],
    #     ['B', ['C', 'D'], 1.0],
    #     ['C', ['D'], 4.0],
    # ]
    tareas = [
        ["A", [], 3],
        ["B", [], 2],
        ["C", [], 4],
        ["D", [], 3],
        ["E", ["A", "B"], 2],
        ["F", ["E"], 4],
        ["G", ["F"], 2],
        ["H", ["D"], 1],
        ["I", ["G", "H"], 2],
        ["J", ["C", "I"], 4]
    ]
    grafo = generarGrafo(tareas)
    # mostrarGrafo(grafo)
    cpm(grafo)
    