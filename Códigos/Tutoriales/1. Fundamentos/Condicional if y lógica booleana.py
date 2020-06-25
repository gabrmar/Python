# condicional if y operadores lógicos (And, Or y Not)

"""
Aspectos por mejorar:

1) Leve descripción teórica o al menos refencias  sobre operadores lógicos
2) Teoría sobre  el condicional if
3) Cambio de variables por nombres menos personales
4) Descripción de los códigos presentes en este archivo

"""

año = int(input("¿En qué año estamos? ")) #Pedir entrada y tratar el dato como valor entéro
edad = int(input("ingresa tu edad: "))
if edad >= 18:
    print("eres mayor de edad")
    nombre = input("¿Cuál  es tu nombre? ") #Python reconoce caractéres de otros idiomas en su texto como lo son las tíldes 
    año_nacimiento = int(input("¿En qué año naciste? "))
    edad_gabriel = año - año_nacimiento
    if not edad == edad_gabriel: # operador lógico Not. La condición se cumple si la edad no es igual a la edad calculada 
          print("mmmm...algo extraño pasa. Vamos a confirmar")
          edad = int(input("ingresa tu edad: "))
    if nombre == "Gabriel" or nombre == "gabriel" and año_nacimiento == 1992 and edad == edad_gabriel: # operador lógico Or y operador lógico And
        print("Bienvenido Gabriel, programador de este código")
        print("Ahora debes responder una pregunta de autenticación")
        respuesta = input("¿Cuál fue el primer sobrenombre que te pusiste? " )
        if respuesta == "Leirbag" or respuesta == "leirbag": 
            print("¡perfecto¡ Definitvamente eres Gabriel")
        else:
            print("Confirmación reprobada.")
    else:
       print("Bienvenido usuario")     
else: # la declaración if y su declaración else deben tener la mísma sangría(indentation) para que la sintaxis sea correcta
        print("eres menor de edad.\nTe faltan "+ str(18-edad) + " años para llegar a los 18")
        gusto = input("¿te gusta la música instrumental? ")
        if gusto == "Sí":
         print("¡que buen gusto tienes!")
         #la delcaración elif es la forma que se usa en Python para escribir "Else If"
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

"""Incluir referencias sobre operadores lógicos en español"""
