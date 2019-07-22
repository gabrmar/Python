# secuencias especiales
import re

patrón1 = r"(.+) \1" # esta secuencia especial indica
# que el patrón es dinámico y es acquel en donde la cadenea
# empieza con una palabra que se repite una vez

patrón2 = r"(\D+\d)" # uno o más no-dígitos (\D+) y un dígito(\d)

patrón3 = r"\b(cat)\b" # la palabra gato entre dos caracteres de frontera


match = re.match(patrón1, "word word") #Coincide
if match:
   print ("Match 1")

match = re.match(patrón1, "?! ?!") #Coincide
if match:
   print ("Match 2")    

match = re.match(patrón1, "abc cde")
if match:
   print ("Match 3")

match = re.match(patrón2, "Hi 999!")

if match:
   print("Match 1.2")

match = re.match(patrón2, "1, 23, 456!")
if match:
   print("Match 2.2")

match = re.match(patrón2, " ! $?")
if match:
    print("Match 3.2")

match = re.search(patrón3, "The cat sat!") #Coincide (fronteras de espacio)
if match:
   print ("Match 1.3")

match = re.search(patrón3, "We s>cat<tered?") #Coincide (fronteas de caracter)
if match:
   print ("Match 2.3")

match = re.search(patrón3, "We scattered.")
if match:
   print ("Match 3.3")
