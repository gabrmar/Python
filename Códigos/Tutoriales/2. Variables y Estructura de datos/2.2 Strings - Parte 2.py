"""
Las cadenas de caracteres o strings poseen muchas aplicaciones, por ello en Python luedes encontrar una gran cantidad de funciones
que facilitan su manejo haciendo que hacer códigos con strings sea algo mucho más práctico. Abajo encontrarás un ejemplo con las funciones
más comunes para mnejar strings.
"""


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


