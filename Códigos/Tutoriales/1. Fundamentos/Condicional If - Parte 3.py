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
    if Codigos > 30 and Codigos < 60: # Esta condición sólo es verdadera si el número de códigos es mayor de 30 y menor de 60. Ambas condiciones
        # deben cumplirse para que la condición se considera verdadera.
        print("Ya tienes cierta experiencia programando.")
    elif Codigos > 60: # Segunda condición a evaluar en caso de que la primera sea falsa.
        print("Sin duda ya no eres un novato.")
    else: # Instrucciones a ejecutar en caso de que niguna de las conficiones anteriores sean verdaderas.
        print("Bueno, ya comenzaste. Pronto perderás la cuenta de la cantidad de códigos que habrás hecho.")
    # Sección de código para preguntar por algo más complejo que servirá de base para realizar el operador lógico AND. 
Respuesta2 = input("Tengo algo de curiosidad. ¿De causualidad alguno de los códigos que has realizado tiene que ver con inteligencia artificial? Sí/No: " )   
if Respuesta2 == "Sí" or Respuesta2 == "Si" and Codigos > 60: # Si el usuario escribe Sí o Si  y tras de eso había puesto una cantidad de
    # Códigos hechos mayores a 60, entonces esta condición es verdadera.
    print("Vaya, vaya. Parece que estoy hablando con un veterano de la programación...")
    print("Déjame decirte que si hay un lenguaje idea para crear inteligencias artificales, ese es Python.")
elif Respuesta2 == "No" or Respuesta2 == "no": #Si el usuario dice que no,con mayúscula o sin ella, la condición es verdadera.
    print("Déjame decirte que es una de las aplicaiones más intersantes que te puedo recomendar con Python. \n Averigua un poco de ellas.")
    # Explicar backslash 
else: # Ahora el else se usa para definir lo que se va a ejecutar en caso de que el usuario no escriba ni Sí ni no
    print("No te entendí bien.") # No olvides que lo que sigue debajo del else también necesita de 
    # 4 espacios, es decir una sangría, para indicar de que éstas instrucciones dependen de que la condición del if sea falsa.

print("") 
print("Disculpa. Me tengo que ir a hacer cosas de bots. Nos vemos pronto") # Las instrucciones que no tiene espacios al inicio no dependen de una condición if
# para ser ejecutadas


"""


https://entrenamiento-python-basico.readthedocs.io/es/latest/leccion4/operadores_logicos.html

"""