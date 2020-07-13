# Strings (formateo y funciones adicionales)
"""
el uso de strings en Python no es muy diferente del uso de
ellas en otros lenguajes, sin embargo  Python ofrece algunas
fucniones  adicionales para facilitar el su trabajo. una de
esas ventajas son las funciones para facilitar el formateo (casting)
de variables  a variables tipo string
"""

numeros =[1,2,3,4]
mensaje = "los números son {0},{1},{2} y {3}".format(numeros[0],numeros[1],numeros[2],numeros[3])
"""
se puede ver que  por medio de métodos de formateo se puede agregar números dentro de un string sin necesidad
de recurrir a concatenaciones por meio de sumas, sino que basta con utilizar números entre llaves que representen
los números que serán formateados a string
"""
print(mensaje)
print("los números para esta prueba son {s1} y {s2}".format(s1=10,s2=115)) #también se puede usar con argumentos fijos
#como se haría en cualquier función creada por el ususario. Sólo recuerda colocar las variables dentro del mensaje string
      

#funciones básicas de Strings para Python

lista = ["ella", "tú", "nosotros"]
l = len(lista) # Ésta función almacena el largo de la lista (cantidad de elementos) en una variable.
print(l)
string = ",".join(lista)  # transforma listas de strings en una sola por medio de un seperador (la coma esta vez)
# se puede usar cualquer caracter como separador entre los elementos de la lista
print(string)
string2 = "00000esta es la historia de Ramiro00000"
string2 = string2.strip("0") # strip permite elminar caracteres que estén en los extremos de una string. En este caso el 0.
# También sirve para elminar espacios de más en un string.
print(string2)
string2 = string2.replace("Ramiro","Jaime") #reemplaza una parte de la string por otra
print(string2)
if string2.startswith("esta") == True: #pregunta si el string empieza con una palabra en especifico
    # la parte de == True es más por  pedagogía, mas no es necesaria
    string2 = string2.replace("esta","Esta")
    print(string2)
string3 = "bievenido a la ciudad de Cartagena"
if string3.endswith("Cartagena") == True: # pregunta si el string termina con uan palabra en especifico
    # == True también es opcional
    string3 = string3.replace("Cartagena","Barranquilla")
    print(string3)
string4 = "GaLleTa CON queso"
string4 = string4.lower() #convertir string a minúscula
print(string4)
string4 = string4.capitalize() # Convertir la primera letra del string en mayúscula
print(string4)
string4 = string4.upper() #convertir string a mayúscula
print(string4)
string = string.split(",")# opuesto a join, separa una string en elementos de una lista por medio de un separador
print(string)