# Proyectos Integradores de Investigacion Operativa II - Python - 2022

# Autores: Gonzalo Oropeza y Pablo Sandoval

## Primer Proyecto de la materia de Investigación Operativa II de la facultad Ingenieria en Informatica - UCASAL

### Teoria de Juegos

### Dominadas:

El algoritmo diseñado se basa en marcar el numero de estrategias que poseen ambos jugadores. A partir de eso se aplica el concepto de estrategia dominada para eliminar una serie de estrategias inferiores hasta que quede sólo una que se pueda elegir.

Para ello se emplean la funcion estrategiaDominada que recibe como parametro la matriz de pagos; En la misma se realiza un ciclo while en el que, mientras la longitud de la misma no sea 1, itera realizando las siguientes funciones:
- dominadasJ1(): recibe la matriz y busca eliminar la estrategia que este dominada por algun otra, recorriendo por filas, lo que refiere a la perspectiva del jugador 1.
- dominadasJ2(): recibe la matriz y busca eliminar la estrategia que este dominada por algun otra, recorriendo por columnas, lo que refiere a la perspectiva del jugador ( ya que se supone que ambos jugadores son racionales)

Cuando termina el ciclo se obtiene una matriz de dimension 1, con un pago conveniente para ambos.
Se empleo la libreria numpy, para recorrer la matriz de forma eficiente y poder mostrarla por consola de forma adecuada.
### Minimax:

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

## Segundo Proyecto de la materia de Investigación Operativa II de la facultad Ingenieria en Informatica - UCASAL

### Modelo de Redes
#### Minimal Spanning Tree
#### Algoritmo de Floyd
Definido en el archivo 'Ruta.py' se construyo un programa basado en el algoritmo de Floyd, este algoritmo determina la distancia entre 2 nodos cualesquiera en la red.
Para la construccion del mismo se empleo la libreria numpy para la exposicion de los datos y sigue la siguiente logica:
- dados 3 nodos (i,j,k) con las distancias de conexion que se muestran en los 3 arcos, es mas corto llegar de j a i pasando por k, si la distancia de i a k mas la distancia de k a j es menor que la distancia de i a j
- a partir de esta idea se construyo la funcion recorriendo la matriz definiendo una fila k y una columa k como fila pivote y columna pivote respectivamente; en base a esto evalua con la matriz de distancia que representa al grafo (notese que se emplea un valor relativamente alto en referencia al valor infinito => INF)

#### Modelo de flujo máximo
Se basa en un grafo basado en una sola fuente y un solo sumidero o vertedero, utilizando arcos de capacidad infinita unidireccionales, como se muestra mediante los arcos de rayas en la figura anterior.
Para el arco (i,j), la notación proporciona las capacidades de flujo en las dos direcciones i -> j y j -> i. 
Para la construccion del mismo se uso la libreria  igraph el cual dispone del metodo del calculo y la libreria  matplotlib.pyplot para mostrar los graficos.

#### Critical Path Method