import igraph as ig
import matplotlib.pyplot as plt
import random


def ingresarGrafoSinPesos():
    vertices: list = []

    respuesta = "si"
    print("Cada numero representa el numero de arco")
    print("Ingreso de los arcos del grafo (0 es el inicial):")
    while(respuesta == "si"):
        nodoInicial = int(input("\tIngrese el primer nodo del arco: "))
        nodoFinal = int(input("\tIngrese el segundo nodo del arco: "))
        vertices.append([nodoInicial, nodoFinal])
        respuesta = input("¿Desea ingresar arcos? si/no: ")

    return ig.Graph(vertices)

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

grafo = ingresarGrafoConPesos()

for index, vertice in enumerate(grafo.vs):
    grafo.vs[index]["label"] = index

arcos_mst = grafo.spanning_tree(weights=grafo.es["peso"], return_tree=False)

grafo.es["color"] = "green"
grafo.es[arcos_mst]["color"] = "midnightblue"
grafo.es["width"] = 1.0
grafo.es[arcos_mst]["width"] = 3.0

# {(1, 2), (1, 5), (2, 3), (2, 4), (3, 4), (3, 5), (4, 3), (4, 6), (5, 2), (5, 6)}

fig, ax = plt.subplots()
ig.plot(
    grafo, 
    target=ax, 
    layout="grid", 
    vertex_color="lightblue",
    vertex_label = grafo.vs["label"],
    edge_width=grafo.es["width"],
    edge_label=grafo.es["peso"],
    edge_background="white",
)

plt.show()

# Segunda prueba
# g = ig.Graph.Lattice([5, 5], circular=False)
# g.es["weight"] = [random.randint(1, 20) for _ in g.es]

# mst_edges = g.spanning_tree(weights=g.es["weight"], return_tree=False)

# g.es["color"] = "green"
# g.es[mst_edges]["color"] = "midnightblue"
# g.es["width"] = 1.0
# g.es[mst_edges]["width"] = 3.0

# fig, ax = plt.subplots()
# ig.plot(
#     g,
#     target=ax,
#     layout="grid",
#     vertex_color="lightblue",
#     edge_width=g.es["width"],
#     edge_label=g.es["weight"],
#     edge_background="white",
# )
# plt.show()