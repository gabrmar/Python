# Condificional If

"""
Aspectos a incluir:

    -Aplicación con operador AND
    -Explicación del operador AND
    -Uso de condicionales anidados por medio del else if y el elif 
    -Colocar Link nuevamente 
"""


Nombre = input("¿Cuál es tu nombre? ") # Ingresando nombre 
print("Hola "+ Nombre + "." + " Bienvenido") # Bienvenida al usuario
Respuesta = input("¿Tienes experiencia programando? Sí/No: ")
if Respuesta == "Sí" or Respuesta == "Si": # Sí el usuario escribe Sí o Si, la condición será verdadera 
    print("Bueno, creo que Python no será desafío para tí") # Recuerda que primero debe colocarse los 4 espacios (la sangría)
    #  para especificar que estas intrucciones dependen de que la condición del if sea verdadera.
    Codigos = int(input("¿Cuántos códigos has programado? "))
    if Codigos > 30:
        print("Ya tienes cierta experiencia programando.")
    elif Codigos > 60:
        print("Sin duda ya no eres un novato.")
    else:
        print("Bueno, ya comenzaste. Pronto perderás la cuenta de la cantidad de códigos que habrás hecho.")
    # Sección de código para preguntar por algo más complejo que servirá de base para realizar el operador lógico AND.    

else: # Ahora el else se usa para definir lo que se va a ejecutar en caso de que el usuario no escriba ni "Sí" o "Si"
    print("No te preocupes. Python es un lenguaje excelente para empezar") # No olvides que lo que sigue debajo del else también necesita de 
    # 4 espacios, es decir una sangría, para indicar de que éstas instrucciones dependen de que la condición del if sea falsa.

print("") 
print("Sigamos aprendiendo Python. Nos vemos pronto") # Las instrucciones que no tiene espacios al inicio no dependen de una condición if
# para ser ejecutadas


"""


https://entrenamiento-python-basico.readthedocs.io/es/latest/leccion4/operadores_logicos.html

"""