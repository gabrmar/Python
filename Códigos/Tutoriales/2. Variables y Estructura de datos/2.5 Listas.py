"""
Las list

-Introducción
-Segmentación de lista
-Operadores de lista (No incluir la funciones de pop y append porque irán en la próxima sección)
-Funciones de lista (Incluir las funciones de compresión de listas)
"""

"""
Las listas son un tipo especial de variables que permiten guardar más de un dato incluyendo valores de diferetes tipos de variables.
Con ellas se pueden hacer códigos de forma más sencilla al agrupar datos en común en una sola lista a la cual podemos usar para ver uno
o varios elementos, modifcarlos e imprimir toda la lista.
"""

lista = [1,5,6]
lista2 = ["hola","hola_dos","galleta"]
lista3 = [3.9,2.1,3.0]
lista4 = "abecedario" # Las variables string se pueden manejar como
# Lista de caracteres
lista_vacío = [] # Lista vacía sin ningún elemento
lista_múltiple = ["hola",1,1.0,[-1,-2,-3]] # Lista con múltiples tipos de datos
#Recorridos con While
"""
Se puede acceder a cada uno de los elemetnos de las listas por medio de un número que represente la posición del dato dentro de la lista.
Este numero es conocido com índice y en Python empiezan desde el número cero, es decir que una lista con 3 elementos tiene los índices 0,
1 y 2 donde cada uno de ellos se usa para seleccionar al primer, segundo y tercer elemento de la lista respectivamente.

"""
# Recorriendo las listas
# Recorrido por medio del ciclo While

i = 0 # Definiendo variable para los índices
while i < 3:
    print(lista[i]) # Imprimiendo uno a uno los elementos de la lista 
    i +=1 # Incrementando el condator para ir al siguiente elemento. esto es igual a colocar "i = i+1". Esto se le conoce como operadores
    # in situ o In-place operations.
i=0
while i < 10:
    print(lista4[i])
    i +=1
i=0

# Recorridos con For

"""
Dado que los ciclos For en Python no funcionan con contadores como los Whiles sino con variables iterables, es necesario definir una
para poder recorrer listas por medio de ciclos For. Para ello usaremos la función range() para poder hacer los recorridos.
"""
l1 = len(lista) # La función len permite obtener la longitud de la lista, es decir un número que muestra la cantidad de elementos dentro
# de la lista
l2 = len(lista4)
i1 = range(l1) # La función range crea una lista de números ordenada desde 0 hasta un límite definido.
i2 = range(l2)
for i in i1: # Recorriendo con la lista creada por la función range() para recorrer la lista llamada lista[]
    print(f"lista, elemento {i}:{lista[i]}")
for i in i2: # Recorriendo con la lista creada por la función range() para recorrer la lista llamada lista4[]
    print(f"lista4, elemento {i}:{lista4[i]}")

"""
Revisar de aquí para aabajo 
"""

print(lista_vacío) # Puedes imprimir listas completas sólo colocando el nombre de la lista dentro de la función print()
print(lista)
print(lista_múltiple)
# Impresión de lista de listas usando un ciclo while
while i < 3:
    print(lista_múltiple[3][i]) # Para acceder a un elemento que está dentro de una lista que está dentro de otra lista se necesitan dos
    # índices. El primer índice permite elegir la lista que quieres seleccionar mientras que el segúndo índice permite elegir el elemento
    # de la lista que quieres mostrar.
    i +=1
i=0

"""
Sigue por aquí
"""

# Operaciones entre listas
lista5 = lista + lista3 #concatenando listas (como si fuera String) por medio de la suma 
print(lista5)
print(lista*3) #triplicación de los elementos de la lista (como si fuera String)
 
"""
Referencias

- 1) Fución Range(): https://www.micro.recursospython.com/recursos/la-funcion-range.html
- 2) Operaciones in situ: https://riptutorial.com/es/python/example/10874/operaciones-in-situ
-Refernecia notaciones de suma. Quizás en SoloLearn vea más de esto

"""