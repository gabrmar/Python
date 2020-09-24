# Colocar un par de ejemplos de funciones básicas

"""
1) Estructura básica de una función
2) Funciones con parámetros 

"""

def suma(n1,n2):
    suma = n1 + n2
    return suma

def saludo(nombre):
    print(f"bienvenido al código de funciones, {nombre}")


x = suma(1,2)
print(x)
print(suma(3,5))
saludo("Max")
saludo("María")
