"""
Las list

-Introducción
-Segmentación de lista
-Operadores de lista (No incluir la funciones de pop y append porque irán en la próxima sección)
-Funciones de lista (Incluir las funciones de compresión de listas)
"""

"""
Introducción aquí
"""

# listas en Python, operadores de listas, funciones y métodos de listas
# los índices empiezan desde cero
lista = [1,5,6]
lista2 = ["hola","hola_dos","galleta"]
lista3 = [3.9,2.1,3.0]
lista4 = "abecedario" #las variables string se pueden manejar como
#lista de caracteres
lista_vacío = [] #lista vacío
lista_múltiple = ["hola",1,1.0,[-1,-2,-3]] #lista con  múltiples tipos de  datos
#Recorridos con While
"""
Comentarios pendientes
"""
i = 0
while i < 3:
    print(lista[i])
    i +=1
i=0
while i < 10:
    print(lista4[i])
    i +=1
i=0
# Recorridos con for

"""
Comentarios
"""
l1 = len(lista)
l2 = len(lista4)
i1 = range(l1)
i2 = range(l2)
for i in i1:
    print(f"lista, elemento {i}:{lista[i]}")
for i in i2:
    print(f"lista4, elemento {i}:{lista4[i]}")

print(lista_vacío) #puedes imprimir listas completas
print(lista) # puedes imprimir listas completas
print(lista_múltiple)
while i < 3:
    print(lista_múltiple[3][i]) #accediendo a listas dentro de listas
    i +=1 #las listas anidados es la forma para trabajar con matrices 
i=0

# Operaciones entre listas
lista5 = lista + lista3 #concatenando listas (como si fuera String) por medio de la suma 
print(lista5)
print(lista*3) #triplicación de los elementos de la lista (como si fuera String)

"""
Referencias

-Refernecia notaciones de suma. Quizás en SoloLearn vea más de esto

"""