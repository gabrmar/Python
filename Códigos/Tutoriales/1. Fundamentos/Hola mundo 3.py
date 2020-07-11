"""
Una de las ventajas de Python sobre otros lenguajes es que no es de tipado fuerte, es decir que no tienes que declarar
que tipo de variable que vas a usar para poder trabajar con ella. Miremos el siguiente ejemplo:
"""

#Nota: En Python se pueden hacer comentrios de varias líneas usando las comillas triples

x = 7 #No es necesario declarar x como una variable entera para por usarla como tal
x = x + 2 # es posible cambiarle el valor sin ningún problema
print(x)
x = "hola" #Incluso puedes cambiar el tipo de dato que le asignas a la misma variable y Python lo reconoce sin problemas
print(x)

