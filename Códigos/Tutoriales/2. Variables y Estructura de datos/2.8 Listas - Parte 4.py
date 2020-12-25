#Compresiones de listas

"""
Las lsitas pueden ser creadas por medio de reglas que definan las cualidades
de los elementos que los integran. Dichas cualidades son definidas por
instrucciones de código de manera similar a como una función matemática
define el trazo de un gráfico
"""



#comprensión de lista de cubos
row = [3 for i in range(8)]


cubos =[i**3 for i in range(5)] # usa el contador i y lo eleva al cubo
# en un ciclo desde 0 a 5 (5 no incluido)
print(cubos)

pares = [i**2 for i in range(10) if i**2%2==0] # puedes agregar condicionales
# para segiuir especificando las reglas de la lista
print(pares)

#galleta = [2*i for i in range(10**100)] #habilita esta línea  y tendrás un error de memoria
# por agotamiento de memoria por usar un rango muy grande para la lista (lista de demsiado tamaño)
# el programa intentará por un tiemp cumplir con la istrucción, pero fallará y arrojará el MemoryError
#print(galleta)


#..............


if all(i > número for i in cubos): #si todos los números son mayores a la variable número
    print("todos los números son mayores a {n}".format(n = número))
else:
    print("No todos los números son mayores a {n}".format(n = número))
if any(i > 50 for i in cubos): # si cualquiera de los números es mayor a 50
    print("hay al menos un número mayor a 50")
else:
    print("no hay ningún númerio mayor a 50")
for v in enumerate(cubos): #impirime tuplas de los elementos de la lista con su índice repectivo
    print(v)
