"""
Por medio de la de la declaración *args, defines que la fución trabajará+
con argumentos variables, es  decir que no siemopre uesará la misma cantidad
de argumentos para operar.

el nombre args es sólo una convención; puedes usar otro nombre
"""
def function(named_arg, *args): #*args se coloca luego de los arugmentos
   print(named_arg) # acá se refiere a los argumentos fijos
   # con los que normalmente trabaja la función
   print(args) #acá se refiere a los argumentos adicoanles
   # ellos son tratados como tuplas

"""
también puedes colocar valores por defecto para los argumentos
em caso del que la función  no reciba valores en uno o más
argumentos. Ellos deben estar colocados luego de todos los
argumentos sin valores por defecto
"""

def function2(x, y, food="spam"):
   print(food)

"""
la declaración **kwargs(keyboard arguments) se utiliza para
aregar nommbre de nuevos argumentos y sus respectivos valores
cuando la función es llamada. Se les puede considerar como
un conjunto de argumentos que se pueden crear posterior a la
Definición de la función.

los **kwargs son tratados como un diccionario donde sus nombres
se convierten en llaves y sus valores en los valores del diccionario.
"""

def my_func(x, y=7, *args, **kwargs):
   print(kwargs)# sin los asteriscos
   #los argumentos de args son tratados aparte de los de kwargs

function(1, 2, 3, 4, 5)
function(1,2)
print("-------------------")
function2(1, 2) #Se imprime el valor por defecto
function2(3, 4, "egg") #Se imprime el valor "egg"
my_func(2, 3, 4, 5, 6, a=7, b=8) #imprime diccionario de dos elementos
my_func(2, 3, 4, 5, 6, c=7)#imprime diccionario de un elemento


