# Colocar un par de ejemplos de funciones básicas

"""
1) Estructura básica de una función
2) Funciones con parámetros 

"""

def ejemplo():
    # Las funciones en Python se escriben así: def nombre_de_función():
    # dentro de los paréntesis puedes colocar las variables que la función necesite para trabajar, pero también puedes hacer funciones
    # que no necesiten variables de entrada para funcionar.

def suma(n1,n2): # Definiendo función suma
    suma = n1 + n2
    return suma

def saludo(nombre):
    print(f"bienvenido al código de funciones, {nombre}")


x = suma(1,2)
print(x)
print(suma(3,5))
saludo("Max")
saludo("María")
