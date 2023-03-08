import time
from Clases.Usuario import usuario
from Módulos.ES_mánager import registrar,validar_registro,iniciar_sesión

def pos_inicio(): #Tal vez se pueden inclir como parte de la clase ES_Mánager
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
            time.sleep(2)
        print("¿Qué desea hacer?")
        teclado = input("1. Reproducir\n2. Buscar otra canción\n3. Salir\n")
        if teclado == "1":
            print(canción.letra)
        if teclado == "2":
            teclado = input("Coloca el nombre de la canción a buscar:")
            canción = u.buscar_canciones(teclado)
            while type(canción) == str:
                print("Intenta de nuevo o escribe x para salir")
                time.sleep(2)
                teclado = input("Coloca el nombre de la canción a buscar:")
                if teclado == "x" or teclado == "X":
                    break
                canción = u.buscar_canciones(teclado)
            if teclado == "3":
                print("Gracias por usar Spotipy")
    

print("Bienvenidos a Spotipy")
time.sleep(2)
teclado = input("1. Iniciar Sesión.\n2. Registrarse.\n3. Salir\n")
if teclado == "1":
    teclado = input("Usuario:")
    teclado2 = input("Contraseña:")
    u = iniciar_sesión(teclado,teclado2)
    #print(u)
    time.sleep(2)
    # Esta parte de abaajo se puede optimizar de otra forma
    pos_inicio()
    #-----Acá viene la parte del menú donde se pregunta por reproducir, buscar otra canción o añadir a una lista de reproducción
    #----Hay que agregar la parte donnse se vuelven a pedir los datos. Es posible que se pueda hacer una función al respecto
if teclado == "2":
    u = registrar()
    print(u)
    validar_registro()
    # Esta parte de abaajo se puede optimizar de otra forma 
    pos_inicio() #Hay un problema con el ocultar de la contraseña cuando los datos no son correctos (luego de un N)
    #-----Acá viene la parte del menú donde se pregunta por reproducir, buscar otra canción o añadir a una lista de reproducción
if teclado == "3":
    print("Gracias por usar Spotipy")
