"""
Python como lenguaje ofrece algunas opciones que no son comunes en otros lenguajes de programación. Por ejemplo, En Python es posible colocarle
apodos a las funciones en el caso que el programador considere una buena idea cambiar el nombre. Eso se usa mucho cuando se trabaja con 
fucniones que no fueron generadas por uno y por ello no es tan secnillo modificar el nombre original como lo es colocarle un nombre temporal
dentro del código. Por otro lado, Python también permite crear funciones que reciben otras funciones como variables de entrada lo cual resulta
bastante práctico en algunos códigos como el que veremos a continuación.
"""

def area_rectangulo(l1,l2): # Definiendo la función para el cálculo de área de un rectángulo
     area = l1*l2
     return area

def area_triangulo(b,h): # Definiendo la función para el cálculo de área de un triángulo
     area= b*h/2
     return area

def area_escalada (f,l1,l2,n): # Definiendo función que escala el área 
     a = f(l1,l2) # En esta línea se especifica que cualquier función que se coloque va a recbir de parámetros las variables l1 y l2
     escalado = a*n # Escalando el resultado de la función f
     return escalado

"""
La gran ventaja de la función area_escalada es que puede escalar el valor de cualquier función que necesite dos valores para operar, es decir
l1 y l2. Esto permite que area_escalada sea mucho más fácil de usar con otras funciones sin necesidad de hacer códigos con muchas líneas 
de código.
"""


funcion = area_rectangulo # En Python es posible cambiar el nombre de las funciones según prefiera el programador
a = funcion(2,3) # Llamando la función area_reactángulo usando su nuevo nombre
print(f"El área del rectángulo es {a}")
n1 = 10 # Definiendo un valor para la escala
b = area_escalada(funcion,2,3,n1) # Escalando el área usando la función de area_rectángulo con su nuevo nombre
print(f"El área del rectángulo escalada por {n1} es {b}")
n2 = 4 
c = area_escalada(area_triangulo,3,5,n2) # Escalando el área usando la función de area_triangulo
print(f"El área del triángulo escalada por {n2} es {c}")

