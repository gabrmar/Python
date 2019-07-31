import string  # módulo para manejo de strings
import random  # módulo para manejo de funciones aleatorias


def gen_Letras(l):
    s1 = ""
    abc = string.ascii_uppercase  # Alfabeto ASCII letras mayúsculas
    for i in range(l):
        # elección al azar de un elemento de la variable abc
        s = random.choice(abc)
        s1 = s + s1
    return s1


def gen_numeros(l):
    n1 = ""
    numbers = string.digits  # Todos los dígitos decimales
    for i in range(l):
        n = random.choice(numbers)
        n1 = n + n1
    return n1


def gen_password(s, d):
    x = gen_Letras(s)
    y = gen_numeros(d)
    z = x + y
    return z

# creación de rutina para almacenar los nombres creados en una lista (array/vector)
def registrar(serial, log):
    log.append(serial)  # Adjunta elementos a una lista
    print(
        "Registro completo. Serie {a} fue añadido a la lista".format(a=serial))
    print(log)


def validar(log):
    i = 0
    r = 0  # contador de elemntos repetidos
    match = []  # lista de posiciones de coincidencias
    while i < len(log):
        j = i + 1
        while j < len(log):
            if log[i] == log[j]:
                r = r + 1
                match.append(i)
            j = j + 1
        i = i + 1
    if r > 0:
        print("Elementos repetidos")
        print("Coincidencias encontradas:{x}".format(x=r))
        print("Posiciones con coincidencias:{x}".format(x=match))
        print("Reportando coincidencias para cambio de contraseñas")
    else:
        print("No se encontraron coincidencias.\nTodo en orden")

    # Corrección de la lista.
    i = 0
    for i in range(len(match)):
        log[match[i]] = gen_password(2, 5)
    print("Validación terminada")
    if len(match) > 0:
        print(
            "Coincidencias eliminadas. La nueva lista es: \n{x}".format(x=log))


robots = []  # lista vacía. Se puede ir llenando con nuevos elementos
z = gen_password(5, 2)
z2 = gen_password(5, 2)
z3 = gen_password(5, 2)
registrar(z, robots)
registrar(z2, robots)
registrar(z3, robots)
print(robots)  # se imprimen todos los elementos de la lista sin espacios.
validar(robots)

# Realizar código de prueba definitivo
# Organizar comentarios
