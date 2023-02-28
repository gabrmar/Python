import time
from Clases.Usuario import usuario
from Módulos.ES_mánager import registrar,validar_registro

print("Bienvenidos a Spotipy")
time.sleep(2)
teclado = input("1. Iniciar Sesión\n2. Registrarse.\n")
if teclado == "1":
    teclado = input("Usuario:")
    teclado2 = input("Contraseña:")
    #Acá debe haber alguina comparación entre los datos adquiridos y alguna base de datos
if teclado == "2":
    u = registrar()
    print(u)
    validar_registro()
