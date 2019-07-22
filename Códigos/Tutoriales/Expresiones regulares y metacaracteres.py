import re # módulo de expresiones regulares

#las expresiones regulares son un conejunto de funciones diseñadas
# para eltrabajo de caracteres  para trabajos bastante especfícos y
# y normalmente relacionado con manejos de palabras en un idioma puntual

patrón = r"galleta" #definiendo expresión regular
patrón2 = r"@gmail.com" #Definiendo expresión regular
patrón3 = r"a" 

"""
las expresiones regulares se pueden hacer en conjunto con algo conocido como metacaracteres.
Estos son caracteres que tienen un significado más allá del literal y ofrecen funciones especiales
que  amplian el rango de uso de las expresiones regulares.

"""
patrón4 = r"gr.y" #el punto funciona como metacaracter esta vez operando como caracter comdín,
# es decir que cualquier caracter en la posición del punto hará parte de la coincidencia del patrón,
# ya que lo que importa es que los dos primeros caracteres sean "gr" y el útimo sea "y". El valor
# del caracter 3  es un comodín. Puedes colocar varios puntos seguidos para definir los caracteres
# que serán comodines.El único elemento que no será reconocido por el punto es el caracter de nueva línea (\n)
#La letra r significa que la string se vuelve una string cruda (raw String)

patrón5 = r"^gr.y$" # "^" y  "$" representan  inicio y fin de una string. Usar este patrón  para
# detectar coincidencias implica que sólo entrarán aquellas cadenas de caracteres de 4 elementos
# que comiencen por "gr", tengan un caracter comodín y terminen en "y".

patrón6 = r"[aeiou]" #colocar caracteres dentro de una expresión regular entre corchetes forma
# un metacaracter que representa una lista de posibles caracteres para coincidencia. No se usará
# para revisar si una cadena comienza por "aeiou", sino que se puede usar para saber si una cadena
# tiene vocales incluidas.

patrón7 = r"[aeiou][y]" #acá son dos condiciones las que hacen parte del patrón. Primero se evalúa
#cualquiera de los caracteres del primer corchete y luego evalúa el caracter "y" del segundo.
#Sólo aquellas cadenas que cumplan con ambos corchetes, serán mostrados en un re.search()

patrón8 = r"[^A-Z]" #^ dentro de un metacaracter entre corchetes invierte la búsqueda del patrón
# es decir que los elementos  dentro del corchete no serán para buscar coincidencias sino para buscar
# aquellas cadenas que no coincidan con dichos elementos. En este caso se usa como el patrón de los
# elementos no deseados (letras maýusculas de todo el alfabeto)
# en este caso, si hay cadenas con caracteres mayúsculos y minúsculos, las búsquedas van a aceptar
# que dicha cadena cumple con las condiciones del patrón a pesar porque reconoce los elementos que no
# hacen parte de las mayúsculas dentro de la cadena.

"""
pueden usarse varios tipos de metacacteres por medio de corchetes. Eston son algunos ejemplos
[a-z] todas las eltra del alfabeto en miníscula
[0-9] todos los dígitos
[G-P] todas las letras mayúsculas entre G y P
[A-Za-z]todas las letras del alfbeto en mayúscula o minúscula
ejemplo:
[A-Z][A-Z][0-9]e evalúan cadenas que tengan un caracter en mayúscula, seguido  otro caracter en mayúscula y un dígito
"""

if re.match(patrón,"galletasjdasjdhagalletafdjfjd"): #re.match evalúa si
    # una String comienza con una substring específica(el patrón).
    # mira que no necesitan ser comparadas con un True para que fucnionen
    # ya que ellos son objetos iterables y su comparación con un booleano
    # no funicionará adecuadamenete
    print("Patrón detectado")
else:
    print("No hay coincidencias")


if re.search(patrón2,"gmll920628@gmail.com"): #search busca si hay una substring dentro de la string a evaluar
    #puede buscar la coincidencia en cualquier parte del string  y no sólo en el inicio como en el caso de match
    print("Este es un correo de gmail")
else:
    print("Este no es un correo de gmail")

if re.search(patrón2,"Aquí está mi @gmail.com"):
    print("Este es un correo de gmail")
else:
    print("Este no es un correo de gmail")

if re.search(patrón2,"dadaskdjaskdasj@gmail.comjdsdhasdhsdh<"):
    print("Este es un correo de gmail")
else:
    print("Este no es un correo de gmail")

s1 = re.search(patrón,"galletajdasjdhagalletafdjfjd")
if s1: #si el iterable con resultados de la búsqueda existe 
    print(s1.group()) #imprime la coincidencia
    print(s1.start()) #imprime la posición donde empuieza la coincidencia (extremo abierto del intérvalo)
    print(s1.end())   #imprime la posición  donde termina la ocincidencia (extremo cerrado del intérvalo)
    print(s1.span())  #imprime el intervalo completo donde está la coincidencia (intérvalo semiabierto)
#es importante observar que searchd deja de buscar cuando  encuentra una coincidencia, es decir que no detecta
# si el patrón se repite nuevameente en otras áreas.

s2 = re.sub(patrón,"GALELTA","galletajdasjdhagalletafdjfjd",0) #la función sub reemplaza todas las substring
#que coinciden con el patrón y son reemplazadas por un nuevo patrón. Se puede agregar un número que indique
#número máximo de reemplazos por hacer dentro de la string. Si no se coloca  este número máximo, se asume que
#No hay límites en el reemplazo de los cracteres 
print(s2)


print(re.findall(patrón3, "personalmente, que viva  toda galleta")) # entrega lista de las veces de coincidencis
# entre el string y el patrón
print (list(re.finditer(patrón3, "personalmente, que viva  toda galleta"))) # finditer hace lo mismo pero entregando un iterable
# en vez de una lista



if re.match(patrón4, "grey"): #Coincide
   print("Match 1")

if re.match(patrón4, "gray"): #Coincide
   print("Match 2")

if re.match(patrón4, "blue"):
   print("Match 3")

if re.match(patrón4, "gr2y"): #Coincide
   print("Match 4")

if re.match(patrón4, "gr y"): #Coincide
   print("Match 5")

if re.match(patrón5, "grey"): #Coincide
   print("Match 1.2")

if re.match(patrón5, "gray"): #Coincide
   print("Match 2.2")

if re.match(patrón5, "stingray"):
   print("Match 3.2")

if re.match(patrón5, "grai"):
   print("Match 4.2")

if re.match(patrón5, "prey"):
   print("Match 5.2")

if re.match(patrón5, "galletagraygalleta"):
   print("Match 6.2")

if re.match(patrón5, "gr2y was the day"):
   print("Match 7.2")

if re.search(patrón6, "grey"):#Coincide
   print("Match 1.3")

if re.search(patrón6, "qwertyuiop"):#Coincide
   print("Match 2.3")

if re.search(patrón6, "rhythm myths"):
   print("Match 3.3")

if re.search(patrón7, "grey"):#Coincide
   print("Match 1.4")

if re.search(patrón7, "qwertyuiop"):
   print("Match 2.4")

if re.search(patrón7, "rhythm myths"):
   print("Match 3.4")

if re.search(patrón8, "this is all quiet"): #Coincide
   print("Match 1.8")

if re.search(patrón8, "AbCdEfG123"): #Coincide
   print("Match 2.8")

if re.search(patrón8, "THISISALLSHOUTING"):
   print("Match 3.8")



    


          

