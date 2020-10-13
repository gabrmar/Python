"""
- Funciones báscias en strings en Python (Esto puede ir en otra función)
- Compraciones con un IF en una string así como el operador in y not in  
- Función ord y Función chr (Quizás en un nuevo código) así como función max y min 
 Link: https://thepythonguru.com/python-strings/
 Buscar un enlace en español 
"""


# Basarse en ejemplos del código base de string


lista = ["ella", "tú", "nosotros"] # Definiendo lista de tres cadenas de caracteres (3 strings).
l = len(lista) # Ésta función almacena el largo de la lista (cantidad de elementos) en una variable.
print(l)
string = "-".join(lista)  # Transforma listas de strings en una sola string por medio de un seperador (el guión esta vez)
# se puede usar cualquer caracter como separador entre los elementos de la lista
print(string)
string2 = "00000esta es la historia de Ramiro00000" # Ejemplo de una string con elementos en el extremo que no son de interés
print(string2)
string2 = string2.strip("0") # strip permite elminar caracteres que estén en los extremos de una string. En este caso el 0.
# También sirve para elminar espacios de más en un string.
print(string2)
string2 = string2.replace("Ramiro","Jaime") #reemplaza una parte de la string por otra
print(string2)
if string2.startswith("esta") == True: #pregunta si el string empieza con una palabra en especifico
    # la parte de == True: es más por pedagogía, mas no es necesaria
    string2 = string2.replace("esta","Esta")
    print(string2)
string3 = "bienvenido a la ciudad de Cartagena"
if string3.endswith("Cartagena") == True: # pregunta si el string termina con uan palabra en especifico
    # == True: también es opcional
    string3 = string3.replace("Cartagena","Barranquilla")
    print(string3)
string4 = "GaLleTa CON queso"
string4 = string4.lower() # Convertir string a minúscula
print(string4)
string4 = string4.capitalize() # Convertir la primera letra del string en mayúscula
print(string4)
string4 = string4.upper() #convertir string a mayúscula
print(string4)
string = string.split("-")# opuesto a join, separa una string en elementos de una lista por medio de un separador
print(string)

#----------------------------------------------If con Strings--------------------------

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

1) Información sobre ASCII

"""

