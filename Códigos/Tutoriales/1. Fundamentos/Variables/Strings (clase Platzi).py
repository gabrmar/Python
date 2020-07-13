#Prueba de uso de Strings en Python según clase de Platzi
s1 = "hola"
s2 = "Hola"
if s1 > s2:
    print("Hola")
else:
    print("Hola 2")
# La compración entre cadenas de caracteres (strings) se hace la siguiente manera:
"""
Se hace comparación el primer caracter de cada  string. Si son iguales en valor ASCII,
entonces se repite el proceso con los cracteres inmediatos. Si todos los caracteres
correspondientes tienen el mismo valor ASCII, es porque las strings son iguales.

NOTA: es importante resaltar que una letra en miníscula tiene un valor ASCII difernete
al de su versión en mayúscula.
"""
x = "Galaeta"
#Se pueden crear substrings por medio de lo que se llama en inglés como string slicing (slices)
#Es la manera en que se pueden extraer pedazos de un cadena de caracteres en Python.
print(x[0]) #Puedes pedir un caracter por medio de un índice (empiezan desde cero).
print (x[0:2]) #pidiendo espacio desde la posición 0 hasta la 2. el elemento 0
#Si aparece en la substring, pero el elemento 2 no. es decir que en [0:2] el 
#segundo límite es no inclusivo, por lo cual la substring resultante constará
#De los elementos desde la posición 0 hasta la 1.
print(x[1:]) #Pidiendo los elementos desde la posición 1 hasta la última.
print(x[0:4:2]) #Pidiendo una substring desde la posición 0 hasta la 3 (4 no includo)
#En saltos de dos. 
print(x[::-1])#Pidiendo string desde el principio hasta el final con pasos negativos
# de -1. Esto isgnifica que se entrega la cadena de caracteres invertida


### ----- IMPORTANTE lo que pasa acá ------####
for i in range(20000):
    if i == "h":
        break
print(i)    
"""Se puede probar con cualquier número en range() y el resultado siempre será el mismo:
la condición nunca se cumple puesto que no hay forma en que la compración entre un número
entero y un caracter o una string de verdadero ya que no es posible que sean iguales, por
lo cual el valor siempre es falso. Lo interesante es que comparar dos datos de tipos tan
diferentes no genera errores en Python porque no es un lenguaje de tipado fuerte, es decir
que las variables no están ligadas a una defición que condiciona el tipo de datos que ellas
manejan sino que su uso dentro del código es mucho más dinámico y hay que tener cuidado con
ello para que no ocurran funcionamientos inesperados como el mencionado anteriormente."""
