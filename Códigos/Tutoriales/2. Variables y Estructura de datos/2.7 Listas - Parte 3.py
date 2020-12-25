"""

4) Verificar si se necesitan referencias para este código
"""
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

#Incluir sort, reverse y todas las demás fucniones y métodos de listas encontrados en los marcadores
#Pop,remove,insert,range,append,sort,reverse,count

l1 = [1,2,3,4,5,3,3,3]

#Funciones numéricas para listas

mínimo = min(l1) # Mínimo de una lista de números
máximo = max(l1) # Máximo de una lista de números
# Las funciones max() y min() también pueden usarse con variables que no estén agrupadas en listas. Por ejemplo:
max2 = max(1,2,3)
print(mínimo,máximo,max2)
sumatoria = sum(l1) #suma de todos los elemento de una lista
print("Suma de todos los elementos de de la lista l1:",sumatoria)

