# Condificional If

"""
El condicional if (si) es una  forma de hacer control a las instrucciones del progromama. Por medio de de la sentencia if es posible decidir
cuáles instrucciones y cuales no dependiendo de una o varias condiciones. El siguiente programa sirve para elaborar un bot simple con el que
puedes dialogar dependiendo de lo que respondas. En este código no sólo se muestra cómo usar el condicional if sino como  pedir datos y 
guardarlos en variables. 

La estructura de un condicional If en Python es la siguiente:

if condición:
    instrucciones en caso de ser verdad
else:
    instrucciones en caso de ser falsa

La primera parte expresa qué condición queremos evaluar con el if y las instrucciones a ejecutar si al condición es cierta. En caso de que sea
falsa, entonces se ejecutan las instruccciones de la sección else.

En este código verrás el uso del siguiente tipo de dato en Python:

-Cadenas de caracteres (Strings): Es la forma en que las palabras son almacenadas en cualquier lenguaje de programación. Consta de una 
agrupación de cracteres. Una cadena de cracteres puede verse como si fuera una lista conformada únicamente por letras o letras y números.
Todo string se define entre comillas dobles o sencillas. Por ejemplo, "hola", 'perro' o "2 gatos".
"""


Nombre = input("¿Cuál es tu nombre? ") # por medio de la función input() podemos pedir datos a un usuario
print("Hola "+ Nombre + "." + " Bienvenido") # Puedes usar el símbolo + para unir varias palabras en una sola frase que se puede mostrar 
# en consola
Respuesta = input("¿Tienes experiencia programando? Sí/No: ")
if Respuesta == "Sí": # Si lo es que escribe el usuario es Sí, entonces  se ejecurará la línea de abajo 
    print("Bueno, creo que Python no será desafío para tí") # Respuesta si el usuario escribe "Sí". Primero debe colocarse 4 espacios, también
    #  conocida como una sangría para especificar que estas intrucciones dependen de que la condición del if sea verdadera.
else: # La parte del else se usa para definir lo que se va a ejecutar en caso de que el usuario no escriba "Sí"
    print("No te preocupes. Python es un lenguaje excelente para empezar") # Lo que sigue debajo del else también necesita de 4 espacios, es 
    # decir una sangría, para indicar de que  éstas instrucciones dependen de que la condición del if sea falsa.

print("") # Espacio en blanco
print("Sigamos aprendiendo Python. Nos vemos pronto") # Como esta instrucción no tiene espacios al inicio, entonces se está dejando claro que
 # esta instrucción no depende de la condición if.


"""
Como verás, este código no es perfecto. Por ejemplo, que pasa si no escribes "Sí" con la mayúscula inicial? el código actualmente no podrá 
detectar eso como un Sí y de una aplicará las instrucciones del else, es decir que sólo si se escribe exactamente Sí es que se cumple la
condición. ¿Cómo se puede mejorar el código entonces? Puedes hacer tus propias propuestas, sin embargo la solución la explicaremos en los 
próximos códigos.
"""