""" Ciclo for

Además del condicional if, existen otras formas de controlar cuáles instrucciones se ejecutan dentro de tu código. Una de ellas es indicando
que ciertos comandos se ejecuten cierto número de veces hasta que se hayan repetido dicha cantidad de repeticiones. A este tipo de ejecución 
repetiva se le concen como ciclos (loops en inglés).
"""
palabras = ["hola.","¿Cómo","estás?"]
palabra = "string"
for word in palabras:
    print(word)
#el ciclo for puede usar el contador word para ir imprimiendo
# los valores presnetes en la lista palabras. el Uso del operador
# de lista in nos permite que el contador word sólo se incremente
# dentro de los valores que hacen parte de los índices de la lista.
for i in range(10):
    print("iteración número " + str(i))
# los rangos puenden usarse  como límites del incremento de un contador
# cuando se se defino un valor inicial para dicho contador, este comienza
# en cero.

for x in palabra:
 print(x)
"""
las variables tipo string pueden ser usadasa como límite del contador. De esta
manera las strings hacen parte de los elementos iterables en python, es decir
que son  aquellas variables u organizaciones de las mismas  sirven para regular
el flujo del contador en un ciclo for
"""

 

