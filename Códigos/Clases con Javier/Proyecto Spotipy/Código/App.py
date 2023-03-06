import time
from Clases.Usuario import usuario
from Módulos.ES_mánager import registrar,validar_registro,iniciar_sesión


print("Bienvenidos a Spotipy")
time.sleep(2)
teclado = input("1. Iniciar Sesión.\n2. Registrarse.\n")
if teclado == "1":
    teclado = input("Usuario:")
    teclado2 = input("Contraseña:")
    u = iniciar_sesión(teclado,teclado2)
    print(u)
    time.sleep(2)
    #----Hay que agregar la parte donnse se vuelven a pedir los datos. Es posible que se pueda hacer una función al respecto
if teclado == "2":
    u = registrar()
    print(u)
    validar_registro()
teclado = input("1. Buscar cacnción\n2. Seleccionar lista\n3. Ajustes.\n")
if teclado == "1":
    teclado = input("Coloca el nombre de la canción a buscar:")
    canción = u.buscar_canciones(teclado)
    print(canción) #Probar esta variante para casos exitosos y fracasos
    while type(canción) == str:
        print("Intenta de nuevo o escribe x para salir")
        time.sleep(2)
        teclado = input("Coloca el nombre de la canción a buscar:")
        if teclado == "x" or teclado == "X":
            break
        canción = u.buscar_canciones(teclado)
        print(canción)


"""
Objetivo
-Colocar el menú de búsqueda de cacniones OK
-Crear usuario de prueba para los inicios de sesión
-Hacer la rutina de búsqueda OK 
-Definir si esta será una función o un método de la clase usuario. OK
-Colocar la rutina de reprodiucción de música dentro del ES_mánager-.
"""