'''
Este proyecto usa los datos de la API no oficial de Rick y Morty.

Se obtienen una cantidad de episodios de la página 1 de la API.

El comando with se usa para abrir el archivo.

Se importa el módulo json para acceder a los datos en el archivo JSON 
Tanto JSON como los dict de python tienen estructuras muy similares.

json.load convierte el archivo json en un diccionario de Python.
'''

#--------------Sub-rutinas--------------------------------------------------

def Formatear_Salida(diccionario,idioma="IN"):
    if idioma == "ESP":
        lista_llaves = ["identificador","nombre","fecha emisión","episodios","personajes","enlace","fecha creación"]
    else:
        lista_llaves = ["id","name","air_date","episode","characters","url","created"]
    lista_valores = []
    lista_personajes = []
    for valor in diccionario.values():
        lista_valores.append(valor)
    i = 0
    j = 0
    while i < len(lista_valores):
        if lista_llaves[i] == "characters" or lista_llaves[i] == "personajes": 
            lista_personajes = lista_valores[i]
            print(lista_llaves[i]+":\n")
            while j < len(lista_personajes):
                print(str(j+1)+"- "+lista_personajes[j])
                j=j+1
            print("\n")
        else:
            print(lista_llaves[i]+": "+str(lista_valores[i])+"\n")
        i = i+1
   


def Encontrar_Episodio(lista,episodio,idioma="IN"):
    for i in lista:
        if i["id"] == episodio:
            salida = Formatear_Salida(i,idioma)
            print("\n")
            break 

def Contar_Personaje(lista,personaje): #Toca hacer un ciclo donde se revise la lista de personajes dentro de la lista de resultadso        
    rick = "https://rickandmortyapi.com/api/character/1"
    morty = "https://rickandmortyapi.com/api/character/2"
    summer = "https://rickandmortyapi.com/api/character/3"
    objetivo = ""
    contador_personaje = 0
    if personaje == "Rick":
        objetivo = rick
    if personaje == "Morty":
        objetivo = morty
    if personaje == "Summer":
        objetivo = summer
    #If personajes in lista_personajes
    for i in lista: #recorrido dentro de la lista
        lista_personajes = i["characters"]
        for j in lista_personajes:
            if j == objetivo:
                contador_personaje = contador_personaje + 1 
    print( personaje + " apareció en "+ str(contador_personaje)+ " episodios")
    return 


import json


traduccion = {
    'id': 'identificador',
    'name': 'nombre',
    'air_date': 'fecha emisión',
    'characters': 'personajes',
    'episode': 'episodio',
    'url': 'enlace',
    'created': 'fecha creación',
    'count': 'conteo',
    'pages': 'páginas',
    'next': 'siguiente',
    'prev': 'previo',
}

#--------------Código principal-----------------------------------------

archivo =  open('C:/Users/gm_ll/OneDrive - UNIVERSIDAD AUTONOMA DEL CARIBE/Backup/Gmecatronics/Sistemas informáticos/Python/Códigos/Clases con Javier/episodes.json')
datos = json.load(archivo)
print('La variable datos es de tipo: ', type(datos))
resultados = datos["results"]

"""
Puedes comentar las secciones del código que no quieras imprimir para facilitar la revisión.
"""

#----------Punto 1----------------
print("-------------Punto 1--------------")
print("la longitud de variable datos es ", len(datos))

#----------Punto 3----------------
print("-------------Punto 3--------------")
print("La cantidad de episodios presentes en el JSON es", len(resultados))

#----------Punto 4----------------
print("-------------Punto 4--------------")

Encontrar_Episodio(resultados,19)
#----------Punto 5----------------
print("-------------Punto 5--------------")
Encontrar_Episodio(resultados,8,"ESP")

#----------Punto 6----------------
print("-------------Punto 6--------------")
for i in range(len(resultados)+1):
    Encontrar_Episodio(resultados,i,"ESP")

#----------Punto 7----------------
print("-------------Punto 7--------------")
Encontrar_Episodio(resultados,18,"ESP")
Encontrar_Episodio(resultados,19,"ESP")
Encontrar_Episodio(resultados,20,"ESP")

#----------Punto 8----------------
print("-------------Punto 8--------------")
Contar_Personaje(resultados,"Rick")
Contar_Personaje(resultados,"Morty")
Contar_Personaje(resultados,"Summer")

