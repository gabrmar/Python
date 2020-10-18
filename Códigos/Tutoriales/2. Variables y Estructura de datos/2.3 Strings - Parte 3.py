"""
- Pulir las funciones print
- Agregar comentairos
- Posible introducción corta sobre ASCII y Unicode 

 """

 #----------------------------------------------If con Strings--------------------------

x = "Mensjae"
a = x[1]
print(a)
b = ord(a)
print(a,b)
code = 100
c = chr(code)
print(code,c)
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

"""
Refrencias:

1) ASCII: https://es.wikipedia.org/wiki/ASCII
2) Unicode: https://es.wikipedia.org/wiki/Unicode

"""
