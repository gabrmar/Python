# datos tipo tupla 
""""
Similares a las listas, las tuplas son secuencias de valores que no puede ser modificadas una vez son creadas.
"""
tupla = ("galleta","pollo",3.14632)
tupla2 = "hola",3,2,-1 #se puede crear tuplas sin paréntesis
print(tupla)
print(tupla2)
#tupla[0] = 20 #quita el comentario de esta línea y tendrás un error de tipo
tupla3 = () #tupla vacía
print(tupla3)

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

