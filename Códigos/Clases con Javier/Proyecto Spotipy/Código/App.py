import time
from Clases.Usuario import usuario
from Módulos.ES_mánager import registrar,validar_registro


print("Bienvenidos a Spotipy")
time.sleep(2)
teclado = input("1. Iniciar Sesión.\n2. Registrarse.\n")
if teclado == "1":
    teclado = input("Usuario:")
    teclado2 = input("Contraseña:")
    #Acá debe haber alguina comparación entre los datos adquiridos y alguna base de datos
if teclado == "2":
    u = registrar()
    print(u)
    validar_registro()
teclado = input("1. Buscar cacnción\n2. Crear lista.\n3. Seleccionar lista\n4. Ajustes.\n")
if teclado == "1":
    teclado = input("Coloca el nombre de la canción a buscar:")
    u.buscar_canciones(teclado)
"""x = acceder_canciones() #De esta manera es quye voy a buscar canciones.
print(x) #Sin embargo, también puedo convertir esto en una función de la clase usuario
"""
"""
Objetivo
-Colocar el menú de búsqueda de cacniones OK
-Crear usuario de prueba para los inicios de sesión
-Hacer la rutina de búsqueda
-Definir si esta será una función o un método de la clase usuario.
-Colocar la rutina de reprodiucción de música dentro del ES_mánager-.
"""