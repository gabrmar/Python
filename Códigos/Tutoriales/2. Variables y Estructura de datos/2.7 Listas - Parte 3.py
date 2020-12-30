"""
Las listas tienen una serie de funciones integradas que permiten modificar su contenido sin necesidad de agregar los cambios en una nueva
variable. Estas funciones se conocen como métodos y estas son algunas de sus características son las siguientes:

    -Un método tiene la siguente sintaxis: lista.método()
    -No es necesario guardar los cambios en una neva lista, Es decir que los métodos de lista modifican el contenido de la lista en la cual
    son llamados.

Por otro lado, también hay funciones que se pueden usar en las listas sin ser necesariamente métodos. Estas funciones cumplen con las siguientes
características:

    -Una función tiene la siguiente sintaxis: función(argumento_1,argumento_2...argumento_final)
    -El resultado de las funciones sí puede ser guardado en una nueva variable. Es decir que se puede hacer esto: var = función(argumentos)
    y luego usar la variable var para el resto del código.
    -Las funciones no necesariamente modifican el contenido de la lista que se use como argumento a diferencia de los métodos de lista
    que siempre lo hacen.

En este código podrás ver algunos ejemplos de funciones y métodos de listas en Python
"""

l1 = [1,2,3,4,5,0,3,3,3,10,3]

# Métodos comunes para listas

print(f"El primer elemento de la lista es {l1[0]}")
l1.pop(0) # Índice
print(f"Ahora es {l1[0]} luego de usar el método pop()")
print("Nueva lista:",l1)
l1.remove(3) # Elemento a eliminar
print("Luego de remover usando remove():",l1)
x = 10 
l1.append(x) # Agregando la variable x a la lista
print(f"Luego de añadir el elemento {x} usando append():",l1)
l1.reverse() # Invirtiendo el orden de la lista
print("Luego de invertir la lista por medio de reverse():",l1)
l1.sort() # Organizando los elemento de la lista de menor a mayor
print("Luego de organizar la lista por medio de sort():",l1)
y = 3
r = l1.count(y) # Contando las veces en que la variable y aparece en la lista
print(f"El elemento {y} se repite {r} veces en la lista.")

#Funciones comunes para listas

mínimo = min(l1) # Mínimo de una lista de números
máximo = max(l1) # Máximo de una lista de números
# Las funciones max() y min() también pueden usarse con variables que no estén agrupadas en listas. Por ejemplo:
max2 = max(1,2,3)
print(mínimo,máximo,max2)
sumatoria = sum(l1) #suma de todos los elemento de una lista
print("Suma de todos los elementos de de la lista l1:",sumatoria)

