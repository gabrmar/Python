# datos tipo tupla 
""""
Similares a las listas, las tuplas son secuencias de valores que no puede ser modificadas una vez son creadas.
"""
tupla = ("galleta","pollo",3.14632)
tupla2 = "hola",3,2,-1 #se puede crear tuplas sin paréntesis
tupla_platzi = (1,) #Esta es la manera en que se crean tuplas de un solo elemento (el elemento 1).
# esto es necessario para que el elemento no corra el riesgo de ser reconocido como otro tipo de variable
# en el ejemplo de tupla_platzi, si no ser hace (1,) y se opta por (1) o 1 simplemente, entonces Python
# tomará esa variable como un entero y no como tupla.
print(tupla)
print(tupla2)
print(tupla_platzi)
#tupla[0] = 20 #quita el comentario de esta línea y tendrás un error de tipo porque no se pueden asginar elementos
# a una tupla luego de su creación
tupla3 = () #tupla vacía
print(tupla3)

#Las tuplas no se pueden modifcar como se hace en el caso de una lista, sino que es necesaria la creación
# de una nueva tupla que tenga los cambios que se requieren. En eso se puede decir que hay simulitud entre 
# una tupla y una variable string.

#Desempacando tuplas
print ("-------------------")
tupla = (1, "galleta", 3) #tupla
a, b, c = tupla #asignando  los elemetos de la tupla a tres variables
print(a)
print(b)
print(c)
a, b = b, a #cambiando los valores de las tuplas a otras posiciones
#esto también aplica con listas
print(a)
print(b)
print(c)
a, b, *c, d = [1, 2, 3, 4, 5, 6, 7, 8, 9] #el asterisco significa que
# esta variable será un iterable que tomará todas las vairables que
# las otras variables no hayan tomado
print(a)
print(b)
print(c)
print(d) # d=9
print("----------------------")
a, b, c, *d = [1, 2, 3, 4, 5, 6, 7, 8, 9] #el asterisco significa que
# esta variable será un iterable que tomará todas las vairables que
# las otras variables no hayan tomado
print(a)
print(b)
print(c)
print(d)# d = iterable

