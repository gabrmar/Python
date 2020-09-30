""" Ciclo for

Además del condicional if, existen otras formas de controlar cuáles instrucciones se ejecutan dentro de tu código. Una de ellas es indicando
que ciertos comandos se ejecuten cierto número de veces. A este tipo de ejecución repetiva se le concen como ciclos (loops en inglés) y uno de
los ciclos más comunes es el ciclo for (para). El suguiente código es un ejemplo de como implementar un ciclo for. El código utiliza los
 siguientes tipos de variables como formas de crear un ciclo for en Python:

-Listas: Una agrupación de variables de uno o más tipos dentro de un solo nombre que representa a todo el grupo. Más información de las listas
Al final del código.
"""

palabras = ["hola.","¿Cómo","estás?"] # Lista llamada palabras conformada por 3 strings. Todo string se define entre comillas dobles o sencillas
palabra = "Programación" # variable string que contiene la palabra programacón. 
for letra in palabras: # La estructura de un ciclo for es la siguiente: for contador in lista o string:
    """La variable letra revisa letra por letra el contenido de la variable palabra, es decir que primero busca la primera letra (p), luego
    la segunda (r) y así sucesivamente hasta llegar a la última (n). """
    print(letra) # Acá se muestra la letra guardada 

for i in range(10): # La función range nos permite crear una lista formada por números enteros. al usar 10 como valor, estamos formando una
    # lista de números enteros que va desde cero hasta 9.
    print("iteración número " + str(i)) # para mostrar una variable, puedes agregarla como una suma y coloarla dentro del str(variable) para
    # que sea tratada como texto, no como número.
    # En Python las variables que sirven sirven para regular el flujo del contador en un ciclo for se le conocen como iterables.
    # range(i,x) define una lista iterable que empieza desde el número i y termina en el número x-1.

for x in palabra:
 print(x)


"""
Referencias

Listas en Python: https://devcode.la/tutoriales/listas-python/

"""
 

