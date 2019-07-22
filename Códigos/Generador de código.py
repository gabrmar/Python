import string #módulo para manejo de strings
import random #módulo para manejo de funciones aleatorias

#Generador de contraseñas
#June the 26th: Password generator started according to Excercism requirements.
#June the 27th: First readings on Python String and Ramdom module.
#June the 28th: Start of the letter generation code based on length.
def gen_Letras(l):
    s1 = ""
    abc = string.ascii_uppercase #Alfabeto ASCII letras mayúsculas 
    for i in range(l):
        s = random.choice(abc)
        s1 = s + s1
    return s1


def gen_numeros(l):
    n1 = ""
    numbers = string.digits
    for i in range(l):
        n = random.choice(numbers)
        n1 = n + n1
    return n1

def gen_password(s,d):
    x = gen_Letras(s)
    y = gen_numeros(d)
    z = x + y
    return z
#creación de rutina para almacenar los nombres creados en una lista (array/vector)

def registrar(serial,log):
    log.append(serial) #Adjunta elementos a una lista
    print("Registro completo. Serie {a} fue añadido a la lista".format(a = serial))
    print(log)

def validar(log): #terminar esta función
    i = 0
    while i < len(log):
        j = i + 1
        while j <= len(log):
            if log[i] == log[j]:
                print("Elementos repetidos")
            else:
                print("Elementos diferentes")
            j = j + 1
        i = i + 1





"""
letter = string.ascii_letters #todo elalfabeto en mayúsculas y minúsculas
letter2 = string.ascii_lowercase #todo el alfabeto en minúscula
letter3 = string.ascii_uppercase # todo el alfabeto en mayúscula
print(letter+" "+letter2+" "+letter3)
letter4 = random.choice(letter) # elección al azar de un elemento de la variable letter
letter5 = random.choice(letter)
print(letter4)
print(letter5)
letter6 = letter4 + letter5
print(letter6)
"""
#num = string.digits #Todos los dígitos decimales
"""
x = gen_Letras(3)
print(x)
y = gen_numeros(2)
z = x + y
"""
robots = []  #lista vacía. Se puede ir llenando con nuevos elementos
#print("la longitud de la lista es {x}".format(x=len(robots)))
#z = gen_password(2,2)
#robots = z
#print(robots)
#z2 = gen_password(5,1)
#print(z2)
#robots = robots + z2
#print(robots) # se imprimen todos los elementos de la lista sin espacios.
z = "hola"
z2 = "hola_"
z3 = "galleta"
registrar(z,robots)
registrar(z2,robots)
registrar(z3,robots)
validar(robots)