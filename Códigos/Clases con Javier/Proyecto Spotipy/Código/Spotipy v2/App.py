import time
from Clases.Usuario import usuario
#from Módulos.ES_mánager import registrar,validar_registro,iniciar_sesión,pos_inicio,canción_encontrada
from Clases.ES_mánager import IO_mánager

#Removiendo pos_inicio del main y llevándolo a  ES_mánager
interfaz = IO_mánager()

teclado = interfaz.iniciar()

if teclado == "1":
    teclado = input("Usuario:")
    teclado2 = input("Contraseña:")
    user  = interfaz.iniciar_sesión(teclado,teclado2)
    #print(user)
    time.sleep(1)
    # Esta parte de abaajo se puede optimizar de otra forma
    opción = interfaz.pos_inicio(user)
    #-----Acá viene la parte del menú donde se pregunta por reproducir, buscar otra canción o añadir a una lista de reproducción
    #----Hay que agregar la parte donnse se vuelven a pedir los datos. Es posible que se pueda hacer una función al respecto
    interfaz.canción_encontrada(opción,user) #---------Revisar esto--------------
if teclado == "2":
    user = interfaz.registrar()
    print(user)
    interfaz.validar_registro()
    # Esta parte de abaajo se puede optimizar de otra forma 
    opción = interfaz.pos_inicio(user) #Hay un problema con el ocultar de la contraseña cuando los datos no son correctos (luego de un N)
    #-----Acá viene la parte del menú donde se pregunta por reproducir, buscar otra canción o añadir a una lista de reproducción
    interfaz.canción_encontrada(opción,user) #---------Revisar esto--------------
if teclado == "3":
    print("Gracias por usar Spotipy")