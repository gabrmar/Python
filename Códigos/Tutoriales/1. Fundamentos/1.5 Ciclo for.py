""" Ciclo for

Además del condicional if, existen otras formas de controlar cuáles instrucciones se ejecutan dentro de tu código. Una de ellas es indicando
que ciertos comandos se ejecuten cierto número de veces. A este tipo de ejecución repetiva se le concen como ciclos (loops en inglés) y uno de
los ciclos más comunes es el ciclo for (para). El suguiente código es un ejemplo de como implementar un ciclo for. El código utiliza los
 siguientes tipos de variables como formas de crear un ciclo for en Python:

-Listas: Una agrupación de variables de uno o más tipos dentro de un solo nombre que representa a todo el grupo.
-Cadenas de caracteres (Strings): Es la forma en que las palabras son almacenadas en cualquier lenguaje de programación. Consta de una 
agrupación de cracteres. Una cadena de cracteres puede verse como si fuera una lista conformada únicamente por caracteres.

"""

palabras = ["hola.","¿Cómo","estás?"] # Lista llamada palabras conformada por 3 strings. Todo string se define entre comillas dobles o sencillas
palabra = "Programación" # variable string que contiene la palabra programacón. 
for letra in palabras: # La estructura de un ciclo for es la siguiente: for contador in lista o string:
    """La variable letra revisa letra por letra el contenido de la variable palabra. Es decir que primero busca la primera letra (p), luego
    la segunda (r) y así sucesivamente hasta llegar a la última (n). """
    print(letra) # Acá se muestra la letra guardaa 
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

 

