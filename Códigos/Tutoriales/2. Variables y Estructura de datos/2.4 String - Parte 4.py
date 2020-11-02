"""
Python te permite obtener partes de una cadena de caracteres; puede ser tanto un sólo elemento como una parte más grande de la cadena. Es
decir que de la string "cadena" podríamos obtener cualquiera de sus letras así como sus sílabas, la mitad de la palabra o más. la parte
que necesites la puedes obtener por medio de obtener partes de la string que en inglés se conocen como rebanadas (slices).
"""

x = "Galleta" 
print(x[0]) # Puedes pedir un caracter por medio de un número que represente su posición dentro del string. El número 0 representa el
# primer símbolo, el 1 el segundo y así sucesivamente
print (x[0:2]) # Pidiendo los elementos que están desde la posición 0 hasta la 2. Se puede ver que el elemento 0 Sí es tomado pero el 
# elemento 2 no, es decir que en [0:2] el segundo límite es no es incluído, por lo cual la porción tomada consta de los elementos desde la
# posición 0 hasta la 1.
print(x[1:]) # Pidiendo los elementos desde la posición 1 hasta la última
print(x[0:4:2]) # Pidiendo una porción de la string desde la posición 0 hasta la 3 (4 no includo) saltando valores de dos en dos. 
print(x[::-1])# Pidiendo una porción desde el principio hasta el final con pasos negativos de -1. Esto isgnifica que se entrega la cadena
# de caracteres al revés