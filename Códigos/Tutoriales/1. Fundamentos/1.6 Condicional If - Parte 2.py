# Condificional If

"""
Para hacer que el código no se vea afectado por el tema de las tildes podemos hacer que la condición sea un poco más detallada. por ejemplo,
Podemos hacer que si el usuario escriba "Sí" o "Si", ambas opciones ejecuten las mismas instrucciones. Para ello se utiliza un concepto conocido
como los operadores lógicos. Ellos no son más que palabras que usamos en nuestro día a día para conectar ideas y en la programación los podemos 
usar para hacer condiciones más específicas. En este caso usaremos el operador OR (O en español). Revisemos el código del bot simple: 
"""


Nombre = input("¿Cuál es tu nombre? ") # Ingresando nombre 
print("Hola "+ Nombre + "." + " Bienvenido") # Bienvenida al usuario
Respuesta = input("¿Tienes experiencia programando? Sí/No: ")
if Respuesta == "Sí" or Respuesta == "Si": # Sí el usuario escribe Sí o Si, la condición será verdadera 
    print("Bueno, creo que Python no será desafío para tí") # Recuerda que primero debe colocarse los 4 espacios (la sangría)
    #  para especificar que estas intrucciones dependen de que la condición del if sea verdadera.
else: # Ahora el else se usa para definir lo que se va a ejecutar en caso de que el usuario no escriba ni "Sí" o "Si"
    print("No te preocupes. Python es un lenguaje excelente para empezar") # No olvides que lo que sigue debajo del else también necesita de 
    # 4 espacios, es decir una sangría, para indicar de que éstas instrucciones dependen de que la condición del if sea falsa.

print("") 
print("Sigamos aprendiendo Python. Nos vemos pronto") # Las instrucciones que no tiene espacios al inicio no dependen de una condición if
# para ser ejecutadas


"""
El operador lógico OR permite unir dos condiciones para formar una condición más grande. Ésta condición se considera verdadera cuando una de
Las condiciones es verdadera. En el caso de que las dos condiciones sean verdaderas, también la condición en general se considera verdadera,
es decir que una condición  formada por condiciones conectadas por medio de un OR sólo se considera falsa cuando ambas condiciones que la
integran son falsas.  Esta tabla resume todo lo relacionado con el operador OR:

Operador Lógico   Python          Ejemplo                                         ¿Cuándo es verdad?
O                 Or              El carro es de color negro o de                 Si el carro es gris, entonces es verdad. Si el carro es  
                                  color es gris                                   negro, también es verdad; y sí el carro tiene tanto gris
                                                                                  como negro, entonces también es verdad.

Acá les dejo un buen enlace si quieren más información sobre operadores lógicos:

https://entrenamiento-python-basico.readthedocs.io/es/latest/leccion4/operadores_logicos.html

"""