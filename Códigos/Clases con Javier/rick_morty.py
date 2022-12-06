'''
Este proyecto usa los datos de la API no oficial de Rick y Morty.

Se obtienen una cantidad de episodios de la página 1 de la API.

El comando with se usa para abrir el archivo.

Se importa el módulo json para acceder a los datos en el archivo JSON 
Tanto JSON como los dict de python tienen estructuras muy similares.

json.load convierte el archivo json en un diccionario de Python.
'''

def Formatear_Salida(diccionario,idioma="IN"):
    if idioma == "ESP":
        lista_llaves = ["identificador","nombre","fecha emisión","episodiojes","personajes","enlace","fecha creación"]
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
            print(lista_llaves[i]+":")
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
resultados = datos["results"]

#----------Punto 1----------------
print("-------------Punto 1--------------")
print("la longitud de variable datos es ", len(datos))

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
