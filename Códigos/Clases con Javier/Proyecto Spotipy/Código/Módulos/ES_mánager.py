import time
from Clases.Usuario import usuario
from Bases_de_Datos.Base_Usuarios import consultar_usarios
from Módulos.Excepciones import except_mánager

def registrar():

    excepciones = except_mánager()
    datos = []
    datos.append(input("Nombre:"))
    datos.append(input("Correo:"))  
    datos.append(input("Celular:"))
    datos.append(input("Contraseña:"))
    datos.append(input("confirmar contraseña:"))
    #---Validación del registro----
    excepciones.revisar_registro(datos)
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
            validar_registro() #Interesante, recursivdad en acción
            print(u)
        else:
            raise ValueError("Opción no válida. Sólo S o N")
        
def iniciar_sesión(usuario,contraseña):
    usuarios = consultar_usarios()
    filtro = False
    filtro2 = False
    for i in usuarios:
        if i.nombre == usuario:
            filtro = True
            break
    for i in usuarios:
        if i.contraseña == contraseña:
            filtro2 = True
            break
    if filtro and filtro2:
        print("Usuario autenticado\n")
        return True
    else:
        print("Credenciales incorrectas\n")
        return False