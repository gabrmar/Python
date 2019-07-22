# continuación de  metacaracteres
import re

patrón1 = r"egg(spam)*"

"""
colocar un elemento entre paréntesis y luego un asterico(*) como metacaracter
tiene un efecto en la búsqueda. Ahora se busca un elemento que tenga la cadena
"egg" seguida bien sea de un cero o  más "spam".Esto no implica que deban
estar juntos, de lo contrario sería suficiente colocar r"eggspam", sino que el elemento
"spam" puede estar  más adelante dentro de la cadena.

[a^]* también se puede usar sin necesidad de paréntesis. Im plica que se
busquen cero o más repeticiones de "a" o "^"
"""

patrón2 = r"g+" # metacaracter + indica que se busca al menos una repetición de "g"
patrón3 = r"ice(-)?cream" #zero or more repetitions (guión o crema) No entender
patrón4 = r"9{1,3}$" #las llaves indican la búsqueda delementos presentes entre el íntervalo cerrado descrito
# acá se buscan toda las cadenas que tengan de 1 a 3 nueves en su interior.
# el símbolo de dolares colocado para indicar que sólo se quieren los caracteres dentro de ese rango
# es decir que una cadena con una parte que tenga 4 nueves no será incluida a pesar de que claramente
# hay 3 nueves dentro de la cadena.
patrón5 = r"a(bc)(de)(f(g)h)i" # as expresiones regulares pueden tener sus cracteres agrupados
# entre paréntesis. Estas asociaciones son llamadas grupos y se puede acceder a ellas por medio de funciones

patrón6 = r"(?P<first>abc)(?:def)(ghi)" #los grupós pueden ser accesibles o no accesibles por medio de la función
# group(). Por defecto todos son accesobles, pero por medio del uso de los metacaracteres "?P<>" se define un
# grupo con nombre (named group). la estructura es la siguiente: (?P<nombre de grupo>contenido)
# Los grupos con nombres pueden ser accedidos tanto por su número de grupo como por su nombre de grupo
# Por medio de los metacaracteres "?:" se privatiza un grupo haciendo que no sea accesible por medio de la
# fucnión group  ni por la función groups. La estructura es la siguiente: (?:contenido)

patrón7 = r"gr(a|e)y" #metacaracter "|" significa un O lógico. es decir que la expresión regular puede tener
# tanto la "a" como la "e" como tercer caracter y puede usar a los dos como elemento de patrón. 

if re.match(patrón1, "egg"): #Coincide
   print("Match 1")

if re.match(patrón1, "eggholasdfjsdifjidfjsispamegg"): #Coincide aunque no esté al lado de "egg"
   print("Match 2")

if re.match(patrón1, "spam"):
   print("Match 3")
if re.match(patrón1, "eggspamspamspamm"): #Coincide
   print("Match 4")

if re.match(patrón2, "g"): #Coincide
   print("Match 1.2")

if re.match(patrón2, "gggggggggggggg"): #Coincide
   print("Match 2.2")

if re.match(patrón2, "abc"):
   print("Match 3.2")

if re.match(patrón3, "ice-cream"): #Coincide
   print("Match 1.3")

if re.match(patrón3, "icecream"): #Coincide
   print("Match 2.3")

if re.match(patrón3, "sausages"):
   print("Match 3.3")

if re.match(patrón3, "ice--ice"):
   print("Match 4.3")

if re.match(patrón4, "9"): #Coincide
   print("Match 1.4")

if re.match(patrón4, "999"): #Coincide
   print("Match 2.4")

if re.match(patrón4, "9999"):
   print("Match 3.4")
   
match = re.match(patrón5, "abcdefghijklmnop")
if match:
   print(match.group()) # muestra todo el patrón
   print(match.group(0))# También muestra todo el patrón
   print(match.group(1)) # muestra el siguiente grupo (paréntesis) de izquierda a derecha 
   print(match.group(2))
   print(match.groups()) #muestra los grupos en una tupla desde el grupo 1 en adelate
   
print("---------------------")

match = re.match(patrón6, "abcdefghi")
if match:
   print(match.group("first")) #Nombre del grupo
   print(match.groups()) # aparecerán todos los grupos que no estén privatizados
   print(match.group(2)) #este número dería mostrar "def", pero como ese grupo está privado
   # mostrará al siguoente grupo, es decir a "ghi"

match = re.match(patrón7, "gray")
if match:
   print ("Match 1.5") #Coincide

match = re.match(patrón7, "grey")
if match:
   print ("Match 2.5")    #Coincide

match = re.match(patrón7, "griy")
if match:
    print ("Match 3.5")
