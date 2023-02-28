import time
from Clases.Usuario import usuario

def registrar():

    datos = []
    datos.append(input("Nombre:"))
    datos.append(input("Correo:"))  
    datos.append(input("Celular:"))
    datos.append(input("Contraseña:"))
    datos.append(input("confirmar contraseña:"))
    if datos[-2] == datos[-1]:
        u = usuario(datos[0],datos[1],datos[2],datos[3])
    else:
        verificación = False
        while(verificación== False):
            print("La contraseña no fue confirmada. Por favor revisar.")
            time.sleep(2)
            teclado4 = input("Contraseña:")
            teclado5 = input("confirmar contraseña:")
            if teclado4 == teclado5:
                verificación = True
        u = usuario(datos[0],datos[1],datos[2],datos[3])
        
    del datos
    return u 

def validar_registro():

    confirmación = False
    while confirmación == False:
        confirmación = input("¿Son estos datos correctos?S/N:")
        if confirmación == "S" or confirmación == "s":
            print("Registro exitoso")
            time.sleep(1)
            print("Bienvenido")
            #Toca generar un registro del usuario en algún lado.
            #Quizás la creación de la instancia sea suficeinte para ello, pero no creo
        elif confirmación == "N" or confirmación == "n":
            u = registrar()
            print(u)