"""
La programación funcional es un estilo de programación basa en el uso
de de fucniones puras para el desarrollo de programas. Las funciones puras
son aquellas  que sólo realizan modificaciones de variables
dentro de su rutina y entregan una sola salida de manera estable.

Existen formas de hacer funciones mucho más rápido y es por medio de la notación
lambda. Se les conoce como funciones anónimas al no ser llamadas por medio de un nombre
sino que son construidas por medio de la notación lambda la cual no requiere que desarrolle
la fuinción fuera del bloque principal del programa.
"""
#función definda pura
def polinomio(x):
    y = 2*x+x**2+3
    return y
#bloque principal de programa
y = polinomio(4)
y2 =(lambda x:2*x+x**2+3)(4) #(lambda variable de entrada: procedimiento)(valor de entrada)
por2 = lambda x:3*x # una función anónima también puede ser renombrada
y3  = (lambda x,y:2*x+y)(10,7) # también aplica para multi-variables
print("resultado de la función pura:{y}".format(y=y))
print("resultado de la función anónima:{y}".format(y=y2))
print("resultado de la función anónima por2:{y}".format(y=por2(9)))
print("resultado de la función anónima multivariable:{y}".format(y=y3))

#funciones de orden superior (funciones que usan funciones como argumentos)
"""
por medio del mapeo de la función map se crean listas con base en la modificación de otra
por mediode una operación matemática. dicha operación debe estar contenida en una función,
bien sea una función definida o una anónima lambda
"""
lista = [1,2,3,4,5,6]
lista2 = list(map(lambda x:2*x+3,lista)) #formatea el mapeo para que se vuelva
# map entrega es un objeto tipo map. es por eso que debe ser formateado a lista para
#poder imprimir el resultado
lista3 = list(filter(lambda x:x%2==0,lista)) #muestra los elementos de la lista que sean pares
print(lista3)


