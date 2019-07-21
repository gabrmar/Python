#Analizador de texto

def contadorCaracteres(texto,caracter):
    cont = 0
    for i in texto:
        if i == caracter:
            cont +=1
    return cont



nombreArchivo = input("ingrese el nombre del arhivo de texto a analizar:")
nombreArchivo = nombreArchivo.lower()
if nombreArchivo == "texto": 
    archivo = open("Texto.txt")
    texto = archivo.read()
    print(texto)
    char = "r"
    c = contadorCaracteres(texto,char)
    print("El caracter {c} aparece {co} veces en el texto analizado".format(c = char, co = c))
    for char in "abcdefghijklmnopqrstuvwxyz":
        porcen = 100*(contadorCaracteres(texto,char)/len(texto))
        print("el caracter {c} aparece en un {por}% del texto".format(c = char,por = round(porcen,2)))    

