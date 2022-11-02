# Proyectos Integradores de Investigacion Operativa II - Python - 2022

# Autores: Gonzalo Oropeza y Pablo Sandoval

## Teoria de Juegos

### Primer Proyecto de la materia de Investigación Operativa II de la facultad Ingenieria en Informatica - UCASAL

#### Dominadas:

El algoritmo diseñado se basa en marcar el numero de estrategias que poseen ambos jugadores. A partir de eso se aplica el concepto de estrategia dominada para eliminar una serie de estrategias inferiores hasta que quede sólo una que se pueda elegir.

Para ello se emplean la funcion estrategiaDominada que recibe como parametro la matriz de pagos; En la misma se realiza un ciclo while en el que, mientras la longitud de la misma no sea 1, itera realizando las siguientes funciones:
- dominadasJ1(): recibe la matriz y busca eliminar la estrategia que este dominada por algun otra, recorriendo por filas, lo que refiere a la perspectiva del jugador 1.
- dominadasJ2(): recibe la matriz y busca eliminar la estrategia que este dominada por algun otra, recorriendo por columnas, lo que refiere a la perspectiva del jugador ( ya que se supone que ambos jugadores son racionales)

Cuando termina el ciclo se obtiene una matriz de dimension 1, con un pago conveniente para ambos.
Se empleo la libreria numpy, para recorrer la matriz de forma eficiente y poder mostrarla por consola de forma adecuada.
#### Minimax:

Basandonos en el siguiente concepto que define el teorema Minimax:
"En un juego de suma cero entre dosjugadores, donde cada jugador conoce el número finito de estrategias de su
oponente, es posible aplicar una estrategia racional que permite a ambos jugadores minimizar la pérdida máxima esperada. Para esto cada jugador sólo debe escoger aquella estrategia que tiene la recompensa más alta entre los pagos más bajos ofrecidos por todas sus estrategias. Esto garantiza que la pérdida a sufrir no será mayor al valor de esa recompensa que resulta ser la más baja de las máximas esperadas"

A partir de esto se desarrollo un modelo, en el que, se carga la matriz de pagos para ambos jugadores y se buscar determinar si existe "punto silla" o si es un juego inestable, cargando en vectores los minimos de cada fila(funcion maximin()) y los maximos de columna (funcion minimax()); A partir de los mismos se busca obtener el maximo del vector de minimos (maximoMinimos()) y el minimo del vector de maximos (minimoMaximos()), y se los compara:
- Si el maximo de minimos es igual al minimo de maximos, entonces se habla de "Punto Silla", donde , ningún jugador puede aprovechar la estrategia de su oponente para mejorar su propia posición.
- Sino, es un juego inestable donde el otro jugador puede predecir la estrategia del otro, y asi, puede aprovechar esta información para mejorar su posición.


#### Estrategias mixtas con programación lineal

El algoritmos diseñado se basa en como obtener las probabilidades de uso de cada estrategia para cada jugador en un juego de dos jugadores, ya sea de suma cero o no.

Para lograrlo, 

#### Equilibrios de Nash


