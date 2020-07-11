#Funciones en Python

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

def uniónPalabras(word,word2): #No es necesario definir el tipo de arugmento de entrada para la función
    print(word+" "+word2)

def multiplicar(num1,num2):
    mul = num1*num2
    print(mul)
    
def división(num1,num2): # funciones con return
    quotient = num1/num2
    return quotient # colocar un return antes del fin de un función impide que se ejecute todo el código que sigue despúes de él
# la declaración return finaliza la ejecución de una función.

"""
Algo muy importante a resaltar que es se pueden crear funciones que tengan como argumentos otras funciones.
"""
def multiFunción(f1,f2,f3,a,b,c,d,e,f):
    f1(a,b) #de essta manera se puede utilizar cualquier función de dos parámetros como argumentos
    f2(c,d)
    result = f3(e,f) # se puede usar cualquier función de dos parámetros con return
    return result


saludo()
uniónPalabras("galleta","pan")
multiplicar("hola",3) # multiplicar strings(lista de caracteres) por números enteros positivos
multiplicar(4,3)
multiplicar(4,3.1416)
"""
Otra String de  documentación de ejemplo
"""
multiplicar([1,2,3,4,5,6],3) # multiplicar listas por números enteros positivos
multiplicar([1,2,3,4,5,6],2)
multiplicar([[1,2,2],[1,1,1]],3) # multiplicar listas de listas por números enteros positivos
cociente = división(100,3)
print("El resultado de la división es: " + str(cociente))

"""
las funciones en Python tiene la habilidad de ser tratadas en algunos casos como variables.
Esto se puede aprovechar para renomrar las funciones según conveniencia.
"""
multi = multiplicar #Renombre de la función multiplicar. Nótese que no es necesario colocar los paréntesis de las funciones
multi(2,2)
print("Activando multiFunción")
x = multiFunción(uniónPalabras,multiplicar,división,"hola"," programa",3,3,8,4) #nombres de funciones sin paréntesis
print(x)