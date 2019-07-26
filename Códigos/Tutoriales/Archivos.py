# Abriendo archivos en Python
import os #Importa  funciones para sistemas operativos. No es necesario para abrir archivos
os.getcwd() #ppuedes usar este comando para  ver el directorio de trabajo actual
miArchivo = open("archivo.txt") #el argumento de la función open es la ruta
#Las variantes de open las puedes consultar en el repertorio de imagenes de Solo Learn
contenido = miArchivo.read() # accede al contenido presente en el archivo
print(contenido)
# de acceso (path) al archivo. Puedes sólo colocar su nombre si está en el
#directorio de programa actual
miArchivo.close() #cerrar el archivo

print("Abriendo el archivo por partes")
"""
La apertura por bytes te permite ir accediendo al conteido del archivo por pedazos.
el usuario establece cuántos bytes quieren ser leidos. Cada vez que solicita más bytes
por medio de más files.read(), se entregará contenido del archivo desde donde termnó el
fragmento del contenido solicitado anterior.
"""
file = open("archivo.txt")
print("primera porción. Primeros 15 bytes")
print(file.read(15))
print("segunda porción. segundos 15 bytes")
print(file.read(15))
print("tercera porción. 5 bytes más de contenido")
print(file.read(15))
print("Última porción. muestra todos los bytes faltantes ")
print(file.read()) # se deja sin parámetro para que muestr todo lo que haga falta
print(file.read()) # Ya no puede mostrar más contenido. llegó al final del archivo en la línea anterior
file.close()

print("leyendo archivo de texto en líneas")
file = open("archivo.txt")
lineas = file.readlines() #lee el archivo y lo almacena en una lista donde cada elemento es una línea del archivo
print(lineas)
file.close()

print("alternativa para leer el texto en líneas")
file = open("archivo.txt")
for line in file: #uso del ciclo for dentro de las líneas de un archivo
    print(line)
file.close()


"""
Es importante resaltar que cuando se escribe sobre un archivo ya existente, no se conserva nada
de lo qye ya estaba dentro de este. No confudir escribir con  agregar o quitar partes del contenido ya existente
Una vez que entras el modo escritura por medio de open, el conteido anterior es borrado y queda en blanco listo
para que reciba el nuevo contenido que agregará el programa.
"""
print("escribiendo en arcihvos")
texto = input("Agrega el texto que quieres colocar en el archivo: ")
file = open("archivo 2.txt","w") # la w signifca que vamos a escribir sobre el archivo.
# si el archivo no existe, es creado por medio de esta línea
file.write(texto) #agregar contenido en el archivo
file.close()
file = open("archivo 2.txt") # también se puede colocar la letra r para indicar lectura (opcional)
print(file.read())
file.close()

"""
una forma asegurar que el archvo es cerrdo luego de una operación es por medio de la decalaración
finally, garantizando que  este estará cerrado incluso en caso de errores.
"""
print("abriendo archivo con try y finally")
try:
   f = open("archivo.txt")
   print(f.read())
finally:
   f.close()
   print("archivo cerrado exitosamente")
   
"""
otra forma es usar la declración with como forma de crear una variable temporal que se usará para
la apertura del archivo. Al final de la declaración with se cierra el documeto
"""
print("Abriendo archivo con la delcaración with")
with open("archivo.txt") as documento:
     print(documento.read())





