# módulos (librerías en Python)

import random #equivalente de Include de C
from math import pi,sqrt # importe selectivo de elementos de la librería math
"""
Trabajar sobre estoe en el futuro

from <module> import *  (importe de todas las entidades lo cual genera riesgos de conflictos de nombres)

Así como también:

import module as <alias name>

from module import n as a, m as b, o as c

"""
# Se importó la constante pi y la función de raíz cuadrada sqrt
from math import remainder as residuo # puedes cambiar el nombre de la variable o función
# por un nombre que sea más cómodo para el programador
from itertools import count, accumulate,takewhile, product, permutations  # importe selectivo de la función count
# la función takewhile,accumulate, función prodcut y función permitations
for i in range(5):
    value = random.randint(1,6) #generador de números enteros entre 1 y 6
    print(value)
print(pi) # nótese que la constante no tiene que ser asignada a una variable.
# Basta con llamarla de manera selectiva para usarla.
x = residuo(10,4) #la función remainder ahora puede ser llamada usando la
# palabra residuo
print(x)

for i in count(90): #coutnt cuenta desde 90 hasta el infinito
  print(i)
  if i >=100: 
    break # interrupción de ciclo infinuto
nums = list(accumulate(range(8))) # accumulate entrega una suceción de valores fijos hasta donde se defina el rango
print(nums)
print(list(takewhile(lambda x: x<= 20, nums))) #tomar elementos de la lista mientras la función preduicado sea cierta
# Función predicado definoda por notación lambda


letters = ("A", "B") #tupla de letras
print(list(product(letters, range(2)))) # producto de la tupla de letras con una lista de rango (2)
print(list(permutations(letters)))#permutaciones posibles entre los elementosde la tupla






