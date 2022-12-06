'''
Este proyecto usa los datos de la API no oficial de Rick y Morty.

Se obtienen una cantidad de episodios de la página 1 de la API.

El comando with se usa para abrir el archivo.

Se importa el módulo json para acceder a los datos en el archivo JSON 
Tanto JSON como los dict de python tienen estructuras muy similares.

json.load convierte el archivo json en un diccionario de Python.
'''

def Formatear_Salida(diccionario,idioma="IN"):
    lista_llaves = []
    lista_valores = []
    lista_personajes = []
    for llave in diccionario.keys():
        lista_llaves.append(llave)
    for valor in diccionario.values():
        lista_valores.append(valor)
    i = 0
    while i < len(lista_valores):
        if lista_llaves[i] == "characters": # <----como esta confirmada esta lista de personajes?
            lista_personajes = lista_valores[i]
        #print(lista_llaves[i]+": "+str(lista_valores[i])+"\n")
        print(lista_personajes)
        i = i+1
   


def Encontrar_Episodio(lista,episodio):
    for i in lista:
        if i["id"] == episodio:
            salida = Formatear_Salida(i)
            break 



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
Encontrar_Episodio(resultados,19)

