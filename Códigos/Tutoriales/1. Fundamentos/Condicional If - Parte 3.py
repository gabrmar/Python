# Condificional If

"""
Aspectos a incluir:

    -Aplicación con operador AND
    -Explicación del operador AND
    -Explicación del !=
    -Explicación del \n
    -Uso de condicionales anidados por medio del else if y el elif 
    -Colocar Link nuevamente 
    -Probar los códigos pasados de los conddicionales If
"""
Codigos = 0 # Ecxplicar el por qué desde esta línea.

Nombre = input("¿Cuál es tu nombre? ") # Ingresando nombre 
print("Hola "+ Nombre + "." + " Bienvenido") # Bienvenida al usuario
Respuesta = input("¿Tienes experiencia programando? Sí/No: ")
if Respuesta == "Sí" or Respuesta == "Si": # Sí el usuario escribe Sí o Si, la condición será verdadera 
    print("Bueno, creo que Python no será desafío para tí") # Recuerda que primero debe colocarse los 4 espacios (la sangría)
    #  para especificar que estas intrucciones dependen de que la condición del if sea verdadera.
    Codigos = int(input("¿Cuántos códigos has programado? ")) # colocar el uso del int() convierte los datos que vamos a tomar en datos
    # enteros. Si no se hiciera eso, entonces el número sería interpretado como un texto y no como un valor de número.
    if Codigos > 30 and Codigos < 60: # Esta condición sólo es verdadera si el número de códigos es mayor de 30 y menor de 60. Ambas condiciones
        # deben cumplirse para que la condición se considera verdadera.
        print("Ya tienes cierta experiencia programando.")
    elif Codigos > 60: # Segunda condición a evaluar en caso de que la primera sea falsa.
        print("Sin duda ya no eres un novato.")
    else: # Instrucciones a ejecutar en caso de que niguna de las conficiones anteriores sean verdaderas.
        print("Bueno, ya comenzaste. Pronto perderás la cuenta de la cantidad de códigos que habrás hecho.") 
    if Codigos != 0: # Si la cantidad de códigos no es cero, entocnes la condición es verdadera     
        Respuesta2 = input("Tengo algo de curiosidad. ¿De causualidad alguno de los códigos que has realizado tiene que ver con inteligencia artificial? Sí/No: " )  
        if Respuesta2 == "Sí" or Respuesta2 == "Si" and Codigos > 60: # Si el usuario escribe Sí o Si y tras de eso había puesto una cantidad de
            # Códigos hechos mayores a 60, entonces esta condición es verdadera.
            print("Vaya, vaya. Parece que estoy hablando con un veterano de la programación...")
            print("Déjame decirte que si hay un lenguaje idea para crear inteligencias artificales, ese es Python.")
        elif Respuesta2 == "No" or Respuesta2 == "no": #Si el usuario dice que no ,con mayúscula o sin ella, la condición es verdadera.
            print("Déjame decirte que es una de las aplicaiones más intersantes que te puedo recomendar con Python. \nAverigua un poco de ellas.")
            # el \n sirve para que el resto de la frase siga en una línea nueva
        else: # Ahora el else se usa para definir lo que se va a ejecutar en caso de que el usuario no escriba ni Sí ni no
            print("No te entendí bien.") # No olvides que lo que sigue debajo del else también necesita de 
            # 4 espacios, es decir una sangría, para indicar de que éstas instrucciones dependen de que la condición del if sea falsa.
elif Respuesta == "No" or Respuesta == "no": # Sí el usuario escribe No o no, la condición será verdadera
    print("Tranquilo. Python es un buen lenguaje para aprender a programar") 


print("") 
print("Disculpa, me tengo que ir a hacer cosas de bots. Nos vemos pronto") # Las instrucciones que no tiene espacios al inicio no dependen de 
# una condición if para ser ejecutadas

"""
EL uso del OR nos permite aceptar más formas en las que el usuario puede escribir "Sí" o "No", sin embargo aún hay varias formas en las que un
usuario puede escribir en caso de que no tenga una buena ortografía, por ejemplo puede escribir sin tilde, sin mayúscula inicial o incluso con 
mayúscula donde no debería haber mayúscula.Todas estas posibilidades pueden incluirse por medio de más operadores OR. Te invito a que jueges con
éste código y hagas los cambios en las condiciones con los OR y AND que consideres para que el bot responda mejor a lo que escriba el usuario.  
"""

"""
https://entrenamiento-python-basico.readthedocs.io/es/latest/leccion4/operadores_logicos.html

"""