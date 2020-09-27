#Funciones en Python

"""
Las funciones nos permiten reutilizar instrucciones de código ya que nos permite tratarlos como bloque de código que podemos solicitar (invocar)
en  cualquier otra parte de nuestro programa sin tener que copiar y pegar nada; basta con colocar el nombre de la función y el Python es capaz
de reconocer que hace referencia a un tipo de instrucciones agrupadas bajo ese nombre de la función.

En este código se verán ejemplos de como crear y utilizar funciones en Python. ALgunos de los ejemplos utilizan un tipo de variables conocidas
como listas. Al final del código hay un enlace con más información sobre las listas y como se usan en Python.

"""

def saludo(): # toda funciópn comienza con la declaración def
    # es necesario terminar la linea donde está def con dos puntos.
    print("bienvenido a  tu primera función hecha en Python")

# Justo como en otros lenguajes de programación como en  C++, las funciones deben ser definidas antes de ser llamadas, es decir 
# que escriben primero antes del código donde son llamadas.

def mensajeDeEntrada():
    """
    las Strings de documentación (comilla triple) son una forma de realizar comentarios más extensos. De esta manera se evita la necesidad 
    de uusar el símbolo numeral para cada línea de comentario.

    Es importante tener en cuenta que estas documentaciones sí son compiladas como parte del código (consumen espacio). Sé conciso.
     Ellas son tratadas como parte del código
    """
    print("""Este es un mensaje de prueba de una función sin argumentos de entrada""") 

def uniónPalabras(word,word2): #No es necesario definir el tipo de arugmento de entrada para la función. word y word2 pueden ser variables 
    # de cualquier tipo y esto es una ventaja que se puede aprovechar en cualquier función de Python.
    print(word+" "+word2) # Ésta función se encarga de concatener dos variables tratadas como strings.

def multiplicar(num1,num2): #Función para multiplicar dos valores. Pueden ser enteros o flotantes e igual va a funcionar.
    mul = num1*num2
    print(mul)
    
def división(num1,num2): # Función para dividir dos valores cualquiera
    quotient = num1/num2
    return quotient # colocar un return antes del fin de un función impide que se ejecute todo el código que sigue despúes de él
# la declaración return finaliza la ejecución de una función. Esa es la razón por la cual el return se coloca al final de cualquier
# función. También el uso del return permite guardar un valor resultante de una función para usarla en otras partes del código después.

"""
NOTA IMPORTANTE

Algo muy importante a resaltar que es se pueden crear funciones que tengan como argumentos otras funciones.

"""
def multiFunción(f1,f2,f3,a,b,c,d,e,f): #Función que utiliza otras funciones como argumentos
    f1(a,b) # de esta manera se puede utilizar cualquier función de dos parámetros como argumentos
    f2(c,d) # acá definimos una función f2 que también trabaja con dos argumentos cualquiera
    result = f3(e,f) # acá se está definiendo una tercar función de dos parámetros pero se asume que esta función tiene un return
    # para que de ella se pueda sacar un valor y guardarlo en la variable result
    return result # regresando el valor de la variable result para ser usando fuera de la función multifunción

"""
Una vez que las funciones están defindas, es momento de usarlas en el código. De aquí en adelante se ve como se invocan las funciones defindas
anteriormente.
"""

saludo() # Llamando a la función saludo 
uniónPalabras("galleta","pan") # Llamando a la función uniónPalabras usando los strings "galleta" y "pan" como valores de entrada (argumentos)
multiplicar("hola",3) # Multiplicar strings(lista de caracteres) por números enteros positivos. Cuando mutiplicas un número entero (3) con 
# una vaiable string ("hola"), el resultado es la misma string repetida tantas veces como el número entero lo indique ("holaholahola")
multiplicar(4,3)
multiplicar(4,3.1416)

multiplicar([1,2,3,4,5,6],3) # multiplicar listas por números enteros positivos. AL igual que con los strings, las listas se extienden 
# repitiendo sus valores tantas veces  como lo indica el número entero (3).
multiplicar([1,2,3,4,5,6],2)
multiplicar([[1,2,2],[1,1,1]],3) # multiplicar listas de listas por números enteros positivos
cociente = división(100,3)
print("El resultado de la división es: " + str(cociente))

"""
las funciones en Python tiene la habilidad de ser tratadas en algunos casos como variables.
Esto se puede aprovechar para renomrar las funciones según conveniencia.
"""
multi = multiplicar #Renombre de la función multiplicar. Nótese que el nombre de la función  va sin paréntesis cuando se le va a renombrar.
# De lo contrario se generará un error a la hora de correr el código. 
multi(2,2) # De esta manera se les puede dar apodos a las funciones y utilizaros para llamarlos en vez de sus nombres originales
print("Activando multiFunción")
x = multiFunción(uniónPalabras,multiplicar,división,"hola"," programa",3,3,8,4) #nombres de funciones sin paréntesis. También se generará
# un error en el código si se les coloca los paréntesis.
print(x)


"""
Referencias:

Listas en Python: https://devcode.la/tutoriales/listas-python/

"""