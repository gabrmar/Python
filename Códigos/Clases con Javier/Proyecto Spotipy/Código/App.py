import time
from Clases.Usuario import usuario
from Módulos.ES_mánager import registrar

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

"""
Aspectos por mejorar:

1. Reducir el número de variables de teclado. - OK
2. Agregar método mágico __str__ en la clase usuario para imprimir los datos junto con OK
la contraseña protegida por asteriscos. 
3. Crear una rutina/función para el registro.
4. Hacer la confirmación de los datos al final de la fase de registro de manera que si
el usuario lo necesita, puede reinicar la fase de registro.

"""

#teclado = input("Agregar opciones luego de registrarte/iniciar sesión")
