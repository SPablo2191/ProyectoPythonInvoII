# Proyectos Integradores de Investigacion Operativa II - Python - 2022

# Autores: Gonzalo Oropeza y Pablo Sandoval

## Teoria de Juegos

### Dominadas

El algoritmo diseñado se basa en marcar el numero de estrategias que poseen ambos jugadores. A partir de eso se aplica el concepto de estrategia dominada para eliminar una serie de estrategias inferiores hasta que quede sólo una que se pueda elegir.

Para ello se emplean la funcion estrategiaDominada que recibe como parametro la matriz de pagos; En la misma se realiza un ciclo while en el que, mientras la longitud de la misma no sea 1, itera realizando las siguientes funciones:
- dominadasJ1(): recibe la matriz y busca eliminar la estrategia que este dominada por algun otra, recorriendo por filas, lo que refiere a la perspectiva del jugador 1.
- dominadasJ2(): recibe la matriz y busca eliminar la estrategia que este dominada por algun otra, recorriendo por columnas, lo que refiere a la perspectiva del jugador ( ya que se supone que ambos jugadores son racionales)

Cuando termina el ciclo se obtiene una matriz de dimension 1, con un pago conveniente para ambos.
Se empleo la libreria numpy, para recorrer la matriz de forma eficiente y poder mostrarla por consola de forma adecuada.

### Minimax

Basandonos en el siguiente concepto que define el teorema Minimax:
"En un juego de suma cero entre dosjugadores, donde cada jugador conoce el número finito de estrategias de su
oponente, es posible aplicar una estrategia racional que permite a ambos jugadores minimizar la pérdida máxima esperada. Para esto cada jugador sólo debe escoger aquella estrategia que tiene la recompensa más alta entre los pagos más bajos ofrecidos por todas sus estrategias. Esto garantiza que la pérdida a sufrir no será mayor al valor de esa recompensa que resulta ser la más baja de las máximas esperadas"

A partir de esto se desarrollo un modelo, en el que, se carga la matriz de pagos para ambos jugadores y se buscar determinar si existe "punto silla" o si es un juego inestable, cargando en vectores los minimos de cada fila(funcion maximin()) y los maximos de columna (funcion minimax()); A partir de los mismos se busca obtener el maximo del vector de minimos (maximoMinimos()) y el minimo del vector de maximos (minimoMaximos()), y se los compara:
- Si el maximo de minimos es igual al minimo de maximos, entonces se habla de "Punto Silla", donde , ningún jugador puede aprovechar la estrategia de su oponente para mejorar su propia posición.
- Sino, es un juego inestable donde el otro jugador puede predecir la estrategia del otro, y asi, puede aprovechar esta información para mejorar su posición.

### Estrategias mixtas con programación lineal

El algoritmos diseñado se basa en como obtener las probabilidades de uso de cada estrategia para cada jugador en un juego de dos jugadores, ya sea de suma cero o no.

Para lograrlo, utilizamos el modulo **optimize** de la libreria **scipy**. El mismo cuenta con un metodo llamado **linprog()** para resolver modelos de programamación lineal. Los parámetros que recibe el método son los siguientes:
- c: es un array unidimensional con los coeficientes de la funcion a optimizar.
- A_ub: es un array bidimensional, en donde cada fila representa los coeficientes para cada variable para una restriccion de inecuación. Este array entonces tiene todos los coeficientes del lado izquierdo de las restricciones que tienen forma de ineciación.
- b_ub: es un array unidimensional, en donde cada valor representa el lado derecho de una restriccion de inecuación.
- A_eq: es un array bidimensional, en donde cada fila representa los coeficientes para cada variable para una restriccion de igualdad. Este array entonces tiene todos los coeficientes del lado izquierdo de las restricciones de igualdad.
- b_eq: es un array unidimensional, en donde cada valor representa el lado derecho de una restriccion de igualdad.
- bounds: es una tupla con subtuplas, en donde cada subtupla tiene los limites inferior y superior que puede tener cada variable.
- method: es un string que representa el método que se va a utilizar para resolver el modelo. Se puede colocar tanto "simplex" como "revised simplex", pero estos métodos serán quitados en versiones posteriores de scipy, por lo que utilizamos el método "highs", el cual tiene una mejor performace y es el método por defecto.

De esta forma, el programa realizado recibe por consola una matriz de pagos, ya que el juego es de suma cero, y luego genera los arrays necesarios para resolver el juego con estrategias mixtas para la perspectiva del jugador 1 y del jugador 2.

### Equilibrios de Nash

El programa realizado para obtener los equilibrios de Nash de un juego utiliza la libreria nashpy, la cual recibe una matriz de pagos (si es que el juego es de suma cero) o dos matrices de pagos (si el juego no es de suma cero).

Entonces, el programa recibe la/s matriz/ces y se las pasa el método Game() de la libreria. Con esto, obtenemos las probabilidades de usar cada estrategia para cada jugador.

## Modelo de Redes

### Minimal Spanning Tree

En este programa se recibe por consola los arcos del grafo escribiendo la relacion entre pares de nodos. Por consola se ingresa el numero de nodo fuente del arco y luego se ingresa el numero de nodo destino del arco. Hay que tener en cuenta que los nodos se enumeran del 0 en adelante. Luego de ingresado el arco, se pregunta si desea agregar más arcos, por lo que se repite el proceso anterior de indicar nodo fuente y nodo destino. La libreria igraph dinamicamente construye el grafo en base a los numeros ingresados.

Este programa utiliza las siguientes librerias:
- [igraph](https://igraph.readthedocs.io/en/0.10.2/index.html): utilizada para definir la estructura de grafo y a su vez tiene el metodo para un grafo spanning_tree(weights), donde weights es un array con los pesos de cada arco en el grafo.
- matplotlib: utilizada para graficar el grafo con los arcos pertenecientes al árbol de mínima expansión.
### Algoritmo de Floyd

Definido en el archivo 'Ruta.py' se construyo un programa basado en el algoritmo de Floyd, este algoritmo determina la distancia entre 2 nodos cualesquiera en la red.
Para la construccion del mismo se empleo la libreria numpy para la exposicion de los datos y sigue la siguiente logica:
- dados 3 nodos (i,j,k) con las distancias de conexion que se muestran en los 3 arcos, es mas corto llegar de j a i pasando por k, si la distancia de i a k mas la distancia de k a j es menor que la distancia de i a j
- a partir de esta idea se construyo la funcion recorriendo la matriz definiendo una fila k y una columa k como fila pivote y columna pivote respectivamente; en base a esto evalua con la matriz de distancia que representa al grafo (notese que se emplea un valor relativamente alto en referencia al valor infinito => INF)

### Modelo de flujo máximo

Se basa en un grafo basado en una sola fuente y un solo sumidero o vertedero, utilizando arcos de capacidad infinita unidireccionales, como se muestra mediante los arcos de rayas en la figura anterior.
Para el arco (i,j), la notación proporciona las capacidades de flujo en las dos direcciones i -> j y j -> i. 
Para la construccion del mismo se uso la libreria  igraph el cual dispone del metodo del calculo y la libreria  matplotlib.pyplot para mostrar los graficos.

### Critical Path Method

El programa CPMv2 recibe por consola las tareas de un proyecto de la siguiente forma:
1. Recibe el nombre de la tarea. Si se recibe vacío, acaba el proceso de ingresar tareas al proyecto.
2. Recibe la duración de la tarea.
3. Recibe el nombre de una tarea precedente a la que se esta ingresando y se repite el paso 3. Si se recibe vacío, acaba el proceso de ingresar tareas precedentes.
4. Se vuelve al paso 1.

Con las tareas, duracion y precedencias del proyecto, se utiliza la libreria [criticalpath](https://github.com/chrisspen/criticalpath) para obtener la ruta crítica del proyecto.

## Teoria de colas
### Modelo M/M/1
El sistema de espera se caracteriza porque los tiempos de llegadas y los tiempos de servicio (mu) se distribuyen de manera exponencial y tienen un único servidor. Según sus características la disciplina de la cola es FIFO y el tamaño de la población de entrada es infinito, es decir, el número de clientes en el sistema no afecta a la tasa de llegadas (lambda).

### Modelo M/M/S
Se diferencia respecto al modelo M/M/1 en que el número de servidores s puede ser cualquier número natural tal que s ≥ 1.  Cuando el número de servidores es mayor que 1, las expresiones de las formulas cambian tal cual se pueden observar en el archivo MMs.py 

### Modelo M/D/1
Una cola M/D/1 no es un tipo especial de cola, sino que a partir de una cola normal, se especifica un orden de salida y de llegada a esta cola la cual:
- M: Llegadas seguidas de un proceso Markov, teniendo como velocidad de llegada definida por  λ, donde 1/ λ es el tiempo entre las llegadas => se emplea para la distribucion exponencial
- D: El tiempo de servicio de cada cliente es determinista (D). La tasa de servicio es definida por μ, donde 1/μ es el tiempo entre servicios. Siendo que el tiempo es determinista, entonces sera exactamente 1/μ para cada cliente (excepto que haya un "empate" en la probabilidad de distribución).
- 1: Un unico servidor
Para la simulación, se construyo una clase cliente (Customer.py) en donde cada instacia sera el arribo de un cliente de un cliente a la cola, teniendo como atributos:
- cid: Identificador del cliente, para distinguirlo durante la simulación.
- arrival_time : tiempo de llegada del cliente a la cola
- departure_time : tiempo de Salida del cliente a la cola

Despues en la funcion simulate_md1() se reciben los siguientes parametros:
- lambd:para la distribucion exponencial de llegada del proximo cliente
- mu : frecuencia de los clientes que son servidos, a mayor sea valor, mayor sera la cantidad de clientes atendidos en una unidad de tiempo.
- max_time: marca el tiempo de duración de la simulación
- verbosity: permite configurar la salida que arroje el programa.puede ser:
- 0: no muestra nada
- 1: muestra el estado de la cola en cada instante
- 2: muestra lo clientes que llegar y se van en cada instante.
Por ultimo, este programa retorna 2 vectores:
- los clientes atendidos
- los clientes que aun quedaron por ser atendidos cuando se termino el tiempo de simulación.
