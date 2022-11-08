from criticalpath import Node

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

    return tareas

def printTareas(tareas):
    print("Tareas del Proyecto:")
    print("Nombre - Predecesoras - Duracion")
    for fila in tareas:
        print(f"\t{fila}")

def rutaCritica(tareas, titulo="Titulo Grafo"):
    grafo = Node(titulo)

    for tarea in tareas:
        # print(f"nodo agregado al grafo: {tarea[0]}")
        grafo.add(Node(tarea[0], duration=tarea[2]))
        
    for tarea in tareas:
        for precedente in tarea[1]:
            # print(f"Linkeo: nodo {precedente} -> nodo {tarea[0]}")
            try:
                grafo.link(
                    grafo.lookup_node(precedente), 
                    grafo.lookup_node(tarea[0])
                ) 
            except KeyError as e:
                print(f"ERROR: Nodo precedente no encontrado = {e}")

    printTareas(tareas)

    grafo.update_all()
    # print(grafo.first_nodes)
    # print(grafo.last_nodes)
    rutaC = grafo.get_critical_path(as_item=True)
    stringRuta = ""
    for index, tarea in enumerate(rutaC):
        if(index < len(rutaC) - 1):
            stringRuta += tarea.name + " -> "
        else:
            stringRuta += tarea.name
    
    print("Resultados:")
    print(f"\tRuta Crítica: {stringRuta}")
    print(f"\tDuración de la Ruta Crítica: {grafo.duration}")


# ejDiaposNoResuelto = [
#     ["A", [], 3],
#     ["B", [], 2],
#     ["C", [], 4],
#     ["D", [], 3],
#     ["E", ["A", "B"], 2],
#     ["F", ["E"], 4],
#     ["G", ["F"], 2],
#     ["H", ["D"], 1],
#     ["I", ["G", "H"], 2],
#     ["J", ["C", "I"], 4]
# ]


if __name__ == "__main__":
    # ejDiaposResuelto = [
    #     ["A", [], 5],
    #     ["B", [], 6],
    #     ["C", ["A"], 3],
    #     ["D", ["A"], 8],
    #     ["E", ["B", "C"], 2],
    #     ["F", ["B", "C"], 11],
    #     ["G", ["D"], 1],
    #     ["H", ["E"], 12]
    # ]
    # rutaCritica(ejDiaposResuelto, "resuelto")

    tareas = ingresarTareas()

    rutaCritica(tareas)
