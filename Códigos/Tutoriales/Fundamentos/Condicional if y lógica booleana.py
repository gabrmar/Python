# condicional if y operadores lógicos (and, or y not)
año = int(input("¿En qué año estamos? "))
edad = int(input("ingresa tu edad: "))
if edad >= 18:
    print("eres maayor de edad")
    nombre = input("¿cuál  es tu nombre? ")
    año_nacimiento = int(input("¿En qué año naciste? "))
    edad_gabriel = año - año_nacimiento
    if not edad == edad_gabriel: # operador lógico not 
          print("mmmm...algo extraño pasa. Vamos a confirmar")
          edad = int(input("ingresa tu edad: "))
    if nombre == "Gabriel" or nombre == "gabriel" and año_nacimiento == 1992 and edad == edad_gabriel: # operador lógico or y operador lógico and
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
