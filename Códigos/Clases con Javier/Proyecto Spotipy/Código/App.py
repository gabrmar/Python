import time
from Clases.Usuario import usuario

print("Bienvenidos a Spotipy")
time.sleep(2)
teclado = input("1. Iniciar Sesión\n2. Registrarse.\n")
if teclado == "1":
    teclado = input("Usuario:")
    teclado2 = input("Contraseña:")
    #Acá debe haber alguina comparación entre los datos adquiridos y alguna base de datos
if teclado == "2":
    teclado = input("Nombre:")
    teclado2 = input("Correo:")
    teclado3 = input("Celular:")
    teclado4 = input("Contraseña:")
    teclado5 = input("confirmar contraseña:")
    if teclado4 == teclado5:
        u = usuario(teclado,teclado2,teclado3,teclado4)
    else:
        verificación = False
        while(verificación== False):
            print("La contraseña no fue confirmada. Por favor revisar")
            time.sleep(2)
            teclado4 = input("Contraseña:")
            teclado5 = input("confirmar contraseña:")
            if teclado4 == teclado5:
                verificación = True
        u = usuario(teclado,teclado2,teclado3,teclado4)
    
    print(u) #Impresión de prueba

"""
Aspectos por mejorar:

1. Reducir el número de variables de teclado.
2. Agregar método mágico __str__ en la clase usuario para imprimir los datos junto con 
la contraseña protegida por asteriscos. 
3. Crear una rutina/función para el registro.
4. Hacer la confirmación de los datos al final de la fase de registro de manera que si
el usuario lo necesita, puede reinicar la fase de registro.

"""

#teclado = input("Agregar opciones luego de registrarte/iniciar sesión")
