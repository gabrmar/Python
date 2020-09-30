# variable tipo Diccionario
"""
Los diccionarios en Python sn estructuras de datos en donde
se organizan elementos emparejados con un elemento de idenficiación
llamado llave. Son similares a las listas, sólo que cada elemento
es una combinación entre la variable a guardar y su llave
"""
"""
edades = {"Juan":26,"Pedro":22,"Mateo":25} #se escribe entre llaves
# {llave 1: valor 1, llave 2: valor 2,...}
print(edades["Juan"])

primary = { # los valores pueden ser listas
"red": [255, 0, 0], 
"green": [0, 255, 0], 
"blue": [0, 0, 255], 
}
print(primary["red"])
#print(primary["hola"]) #si habilitas esta línea, se produce un error de llave
#No se ha creado una llave con nombre "hola"

vacío = {} #diccionario vacío
#print(vacío[0]) #se produce error de llave porque no existen llaves en este diccionario

#los diccionarios no pueden usar listas como llaves. Eso produce un error de tipo
# los diccionarios tampoco pueden ser usados como llaves de otros diccionarios

edadPablo = int(input("Falta agregar la edad de Pablo en la lsita. ¿Cuántos años tiene? "))
edades["Pablo"] =edadPablo #puedes seguir agregando elementos al diccionario. Estos quedarán al final del mismo
print(edades)
edades["Pedro"] = int(input("Resulta que la edad de Pedro no es 22. ¿Cuántos años tiene Pedro? "))
print("Edad corregida. Gracias")
print(edades)

#Se puede preguntar si cierta llave está presente en el diccionario

if "Pablo"in edades:# Si la llave "Pablo está en el diccionario
    print("Pablo ya fue agregado en la lista. Llave verificada")
if "Marcos" not in edades: # Si la llave "Marcos" no está en el diccionario 
    edadMarcos = int(input("Falta agregar la edad de Marcos en la lsita. ¿Cuántos años tiene? "))
    edades["Marcos"] =edadMarcos
    print("Marcos ha sido agregado")
print(edades)

i = 0
while i < 2: #Puedes usar While 1 o While True si quieres que el ciclo sea infinito
    print("Puedes pregutar por la edad de cualquiera de las personas registradas")
    nombre = input("coloca el nombre y recibe su edad ")
    consulta = edades.get(nombre, "nombre no encontrado. Pregunta de nuevo. ") #get busca la llave que corresponde a la colocada en argumentos
    # y muesta el valor que le corresponde. similar a haber sado edades[nombre]; la diferencia radica en la capcidad de colocar un valor
    # personalizado en caso de que la llave no sea encontrada (el valor por defecto es None, pero puede ajustarse para colocar strings u otros datos
    print(consulta)
    i = i + 1
"""


#------Espacio creado gracias a los aportes del curso de Python en Platzi -------------#
Platzi = {} #Creación  de diccionario vacío
Platzi["Llave 1"] = 10 # puedes asignar los elementos del diccionario uno poruno
Platzi["Llave 2"] = 8
Platzi["Llave 3"] = 11
Platzi["Llave 4"] = 15
for key in Platzi: # se recorre el diccionario usando las llaves como interable (puede llamarse key o como el programador quiera) 
    print(key)
for key in Platzi.keys(): # Esta es otra forma es usar las llaves como iterable. El resultado es el mismo
    print(key)
for valores in Platzi.values(): # También se puede recorrer el diccionario usando los valores como interables.
    print(valores)
for k, v in Platzi.items(): # Se puede hace runa iteración con dos contadores al tiempo para poder tanto las llaves como los valores
    # En cada ciclo
    print("Llave:{} , Valor:{}".format(k,v))
print(len(Platzi)) #Len() también se puede usar para calcular la longitud de diccionarios 



