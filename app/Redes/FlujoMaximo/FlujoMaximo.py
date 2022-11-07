import igraph as ig
import matplotlib.pyplot as plt
from Grafos import ingresarGrafoSinPesos
def ingresarCapacidad(grafo):
    capacidades = []
    for i in range(grafo.vcount()+1):
        capacidadInd = int(input(f"Ingrese capacidad de nodo {i+1}:"))
        capacidades.append(capacidadInd)
    grafo.es["capacity"] = capacidades

def main(grafo,fuente=0,sumidero=1):
    if(fuente == sumidero):
        return
    else:
        flow = grafo.maxflow(3, 0, capacity=grafo.es["capacity"])
        fig, ax = plt.subplots()
        ig.plot(
            grafo,
            target=ax,
            layout="circle",
            vertex_label=range(grafo.vcount()),
            vertex_color="lightblue"
        )
        plt.title(f"Flujo Maximo: {flow.value}")
        plt.show()


g = ingresarGrafoSinPesos(directed=True)
ingresarCapacidad(g)
fuente = int(input(f"ingrese nodo fuente entre 0 y {g.vcount()}: "))
sumidero = int(input(f"ingrese nodo fuente entre 0 y {g.vcount()}: ")) 
main(g,fuente,sumidero)

# g = ig.Graph(
#     6,
#     [(3, 2), (3, 4), (2, 1), (4, 1), (4, 5), (1, 0), (5, 0)],
#     directed=True
# )
# g.es["capacity"] = [7, 8, 1, 2, 3, 4, 5]