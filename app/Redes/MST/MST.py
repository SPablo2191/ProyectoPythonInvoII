import igraph as ig
import matplotlib.pyplot as plt
import random
from Grafos import ingresarGrafoConPesos

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