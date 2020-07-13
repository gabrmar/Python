# manejo adicional de listas
lista = [1,2,3,4,5,6,7,"hola","galleta","comida"]
#Usa los dos puntos para  solicitar un pedazo (slice) de los elementos de la lista
p1 = lista[0:1] #todos son intervalos semiabiertos (el elemento 1 no aaprece en p1
p2 = lista[1:3] #todos son intervalos semiabiertos (el elemento 3 no aaprece en p2
p3 = lista[3:7] #todos son intervalos semiabiertos (el elemento 7 no aaprece en p3
p4 = lista[7:9] #todos son intervalos semiabiertos (el elemento 9 no aaprece en p4
p5 = lista[7:]  #desde el elemento 7 hasta el final (elemento 7 sí hace parte de p5)
p6 = lista[:7]  #desde el inicio hasta el elemento 7, el cual no hará parte de p6
p7 = lista[::2] #todos los elementos de la lista con un paso de 2
p8 = lista[1:9:2] #todos los elementos entre la posición 1 y 9 con un paso de dos
#Elemento 7 no hace parte de p8
p9 = lista[-1:] #las posiciones negativas se cuentan empezando la lista desde el último elemento
#"comida" está en la posición -1"
p10 = lista[-1:2] #da  una lista vacía. No existen elementos más allá de la posición -1
p11 = lista[-3:-1] # desde la posición -3 hasta la -1 sin incluir a este último
p12 = lista[::-1] # usando los pasos negativos puedes invertir la lista
print(p1)
print(p2)
print(p3)
print(p4)
print(p5)
print(p6)
print(p7)
print(p8)
print(p9)
print(p10)
print(p11)
print(p12)
