import igraph as ig
import matplotlib.pyplot as plt
from Grafos import ingresarGrafoSinPesos


def ingresarCapacidad(grafo):
    capacidades = []
    for i in range(grafo.vcount()+1):
        capacidadInd = int(input(f"Ingrese capacidad de nodo {i+1}:"))
        capacidades.append(capacidadInd)
    grafo.es["capacity"] = capacidades


def main(grafo, fuente=0, sumidero=1):
    if (fuente == sumidero):
        return
    else:
        flow = grafo.maxflow(3, 0, capacity=grafo.es["capacity"])
        fig, ax = plt.subplots()
        ig.plot(
            grafo,
            target=ax,
            layout="circle",
            edge_label=grafo.es["capacity"],
            vertex_label=range(grafo.vcount()),
            vertex_color="lightblue"
        )
        plt.title(f"Flujo Maximo: {flow.value}")
        plt.show()

print('--------', end='')
print('Modelo de Redes: Algoritmo de Flujo Maximo', end='')
print('--------')
g = ingresarGrafoSinPesos(directed=True)
ingresarCapacidad(g)
# Ejemplo
# g = ig.Graph(4,[(0, 1), (0, 3), (0, 2), (1, 2), (1, 4), (2, 4), (2, 3), (3, 4),(3,2)],directed=False)
# g.es["capacity"] = [20, 10, 30,  40, 30  , 20, 10, 20]
fuente = int(input(f"ingrese nodo fuente entre 0 y {g.vcount()-1}: "))
sumidero = int(input(f"ingrese nodo fuente entre 0 y {g.vcount()-1}: "))
main(g, fuente, sumidero)
