"""
-Introducción
-Segmentación de lista
-Operadores de lista (No incluir la funciones de pop y append porque irán en la próxima sección)
-Funciones de lista (Incluir las funciones de compresión de listas)
"""

# listas en Python, operadores de listas, funciones y métodos de listas
# los índices empiezan desde cero
vector = [1,5,6]
vector2 = ["hola","hola_dos","galleta"]
vector3 = [3.9,2.1,3.0]
vector4 = "abecedario" #las variables string se pueden manejar como
#lista de caracteres
vector_vacío = [] #lista vacío
vector_múltiple = ["hola",1,1.0,[-1,-2,-3]] #lista con  múltiples tipos de  datos
#Recorridos con While
i = 0
while i < 3:
    print(vector[i])
    i +=1
i=0
while i < 10:
    print(vector4[i])
    i +=1
i=0
# Recorridos con for
"""
Ejemplo de recorrido con for
"""

print(vector_vacío) #puedes imprimir listas completas
print(vector) # puedes imprimir listas completas
print(vector_suma) 
print(vector_múltiple)
while i < 3:
    print(vector_múltiple[3][i]) #accediendo a listas dentro de listas
    i +=1 #las listas anidados es la forma para trabajar con matrices 
i=0

# Operaciones entre listas
vector5 = vector + vector3 #concatenando listas (como si fuera String) por medio de la suma 
print(vector5)
print(vector*3) #triplicación de los elementos de la lista (como si fuera String)

"""
Referencias

-Refernecia notaciones de suma. Quizás en SoloLearn vea más de esto

"""