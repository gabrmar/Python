# condicional if y operadores lógicos (And, Or y Not)

"""
El condicional if (si) es una  forma de hacer control a las instrucciones del progromama. Por medio de de la sentencia if es posible decidir
cuáles instrucciones y cuales no dependiendo de una o varias condiciones. El siguiente programa sirve para elaborar un bot simple con el que
puedes dialogar dependiendo de lo que respondas. En este código no sólo se muestra cómo usar el condicional if sino como  pedir datos y 
guardarlos en variables. 

Operadores lógicos

Un aspecto a tener en cuenta antes de empezar con el código, es un concepto conocido como los operadores lógicos. Ellos no son más que palabras
que usamos en nuestro día a día para conectar ideas y en la programación los podemos usar para hacer condiciones más específicas. Los operado-
res más comunes son los siguientes:

Operador Lógico   Python          Ejemplo                                         ¿Cuándo es verdad?
Y                 And             Edad es mayor a 20 y edad es menor a 50         Tanto la edad debe ser mayor a 20 y menor 50. Ej: 35
O                 Or              Color es negro o color es gris                  El color puede ser negro o rojo o bien tener ambos colores                 
No                Not             El número de carros rojos no es 3               Sólo cuando el número de carros no es 3

Acá les dejo un buen enlace si quieren más información sobre operadores lógicos:

https://entrenamiento-python-basico.readthedocs.io/es/latest/leccion4/operadores_logicos.html

No siendo más, comencemos.

"""

# Bot Simple

# Este bot fue creado por Carlos, así que puede identificarlo a través de algunas preguntas, pero también puede comunicarse con otros usuarios.
# Este bot es un poco culto, así que le gusta hacer algunas preguntas sobre música y escritura.
# PD: No le gustan mucho los niños.

año = int(input("¿En qué año estamos? ")) #Pedir entrada y tratar el dato como valor entéro
edad = int(input("ingresa tu edad: "))
if edad >= 18: # Si el la edad es mayor o igual a 18 años, entonces el bot pregutará por el nombre del usuario. Sino, no lo hará 
    print("Eres mayor de edad")
    nombre = input("¿Cuál  es tu nombre? ") #Python reconoce caractéres de otros idiomas en su texto como lo son las tíldes 
    año_nacimiento = int(input("¿En qué año naciste? "))
    edad_usuario = año - año_nacimiento #El bot corroborará si le estás diciendo la verdad calculando la edad por su cuenta
    if not edad == edad_usuario: # operador lógico Not. La condición se cumple si la edad no es igual a la edad calculada 
          print("mmmm...algo extraño pasa. Vamos a confirmar")
          edad = int(input("ingresa tu edad: ")) # Pregunta de nuevo la edad para corroborar
    if nombre == "Carlos" or nombre == "carlos" and año_nacimiento == 1990 and edad == edad_usuario: #operador lógico Or y operador lógico And
    # El bot reconoce a Carlos cuando se cumplen tres condiciones: el nombre, que el año sea 1990 y que la edad registrada coincida con el 
    # Cálculo de edad del bot. En caso del nombre, el bot puede reconocer a Carlos sin importar la mayúscula inicial. Esto se debe al uso del
    # or indicando que la condición se puede cumplir si el nombre es escrito con mayúscula inicial o no.    
        print("Bienvenido Carlos, programador de este código")
        print("Ahora debes responder una pregunta de autenticación") 
        respuesta = input("¿Cuál fue el primer sobrenombre que te pusiste? " )
        if respuesta == "Gohan" or respuesta == "gohan": #Si aciertas en el apodo, el bot estará seguro que eres Carlos, sino te tratará como
            # un usuario 
            print("¡Perfecto¡ Definitvamente eres Carlos")
        else:
            print("Confirmación reprobada. Usted no es Carlos.")
            print("Bienvenido usuario")
    else:
       print("Bienvenido usuario")
    # A partir de este momento el bot inicia una pequeña charla con el usuario. Sus respuestas dependen de las respuestas del usuario 
    gusto = input("¿te gusta la música instrumental? ")
    if gusto == "Sí":
        print("¡que buen gusto tienes!")
        # la delcaración elif es la forma que se usa en Python para escribir "Else If"
        # no es necesario usarlo, ya que bien puedes colocar en una línea la delcaración Else y en la siguente el condicional If
    elif gusto == "sí": 
        print("¡que buen gusto tienes!")
    elif gusto == "si":
        print("¡que buen gusto tienes, pero no olvides la tilde diacrítica!")
    elif gusto == "Si":
        print("¡que buen gusto tienes, pero no olvides la tilde diacrítica!")
    elif gusto == "No":
        print("lástima :(")
    elif gusto == "no":
        print("lástima")
         
else: # la declaración if y su declaración else deben tener la mísma sangría(indentation) para que la sintaxis sea correcta
        print("eres menor de edad.\nTe faltan "+ str(18-edad) + " años para llegar a los 18. El bot para niños está en otro repositorio.")

"""Incluir referencias sobre operadores lógicos en español"""
