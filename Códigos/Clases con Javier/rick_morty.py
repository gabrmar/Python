'''
Este proyecto usa los datos de la API no oficial de Rick y Morty.

Se obtienen una cantidad de episodios de la página 1 de la API.

El comando with se usa para abrir el archivo.

Se importa el módulo json para acceder a los datos en el archivo JSON 
Tanto JSON como los dict de python tienen estructuras muy similares.

json.load convierte el archivo json en un diccionario de Python.
'''

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

archivo =  open('C:/Users/gm_ll/OneDrive - UNIVERSIDAD AUTONOMA DEL CARIBE/Backup/Gmecatronics/Sistemas informáticos/Python/Códigos/Clases con Javier/episodes.json')
datos = json.load(archivo)
print('La variable datos es de tipo: ', type(datos))
print("la longitud de variable datos es ", len(datos))
#print(datos["info"])
#print(datos["results"]) <----  es una lista
resultados = datos["results"]
for i in resultados:
    if i["id"] == 19:
        print(i)    