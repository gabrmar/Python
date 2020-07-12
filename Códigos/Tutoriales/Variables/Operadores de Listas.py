
# --------------------------- EDITAR ESTE CÓDIGO ---------------------------------------------





# listas en Python, operadores de listas, funciones y métodos de listas
# los índices empiezan desde cero
vector = [1,5,6]
vector2 = ["hola","holados","galleta"]
vector3 = [3.9,2.1,3.0]
vector4 = "abecedario" #las variables string se pueden manejar como
#lista de caracteres
vector_vacío = [] #lista vacío
vector_múltiple = ["hola",1,1.0,[-1,-2,-3]] #lista con  múltiples tipos de  datos
i = 0
while i < 3:
    print(vector[i])
    i +=1
i=0
while i < 3:
    print(vector2[i])
    i +=1
i=0
while i < 3:
    print(vector3[i])
    i +=1
i=0
while i < 10:
    print(vector4[i])
    i +=1
i=0
print(vector_vacío) #puedes imprimir listas completas
print(vector) # puedes imprimir listas completas
print(vector_múltiple)
while i < 3:
    print(vector_múltiple[3][i]) #accediendo a listas dentro de listas
    i +=1 #las listas anidados es la forma para trabajar con matrices 
i=0
vector5 = vector + vector3 #concatenando listas (como si fuera String)
print(vector5)
print(vector*3) #triplicación de los elementos de la lista (como si fuera String)


#oepradores de lista
print("hola" in vector2) # evalúa lógicamente si la String "hola" está en
# la lista vector2
if "abe" in vector4: #evalúa lógicamente si la String "abe" es parte de
# la string "abecedario" contenida en vector4
    print("\"abe\" está contenida en la string \"abecedario\"")
if 3.9 in vector3:
    print("3.9 está presente en vector3")
if 10 not in vector: #evalúa lógicamente si 10 no está dentro de la lista
    print("10 no está presente en la lista")
print("Anexando un nuevo elemento en dos listas")
anexo = float(input("Agregue un número flotante aquí: "))
anexo2 = input("Agruegue una variable String aquí: ")
vector.append(anexo) #método append (adjuntar) permite agregar nuevos elementos a los vectores aumentando su tamaño
vector2.append(anexo2)#Se puede adjuntar cualquier tipo de datos
print(vector) #Recuerda que se pueden imprimir los vectores(listas) directamente
print(vector2) #Recuerda que se pueden imprimir los vectores(listas) directamente
longitud = len(vector4) #función para obtener la longitud de una lista (vector) o String
print("el valor de la longitud de la lista \"vector\" es de " +str(longitud))
print("Ahora vamos a agregar un nuevo elemento en la lista en la posición que desee.\nDado una lista de 3 elementos diga:")
anexo = int(input("Número entero a agregar: "))
índice = int(input("ubicación del número entero: "))
if índice > len(vector3) + 1:
    print("El índice reportado es mayor a la longitud de la lista más uno. El número entero se ubica en la última posición de la lista creada para él")
vector3.insert(índice,anexo)    
print(vector3)
print("La lista  a aumentado su longitud una unidad. Su nuevo valor es de "+str(len(vector3)))

#función range()

lista = list(range(10)) # crea una lista con los númeos del 0 al 9 (rango de 10 números en total)
print("lista de 10 números:\n" +str(lista))
lista = list(range(10,25)) #list(range(x1,x2) se usa para hacer una lísta con números entre los dos intervalos x1 y x2
# x1 será un número dentro de la lista, pero x2  no lo será. ver los intérvalos como cerrado en el inicio y abierto en el final
print("lista de números entre 10 y 25:\n" + str(lista))
if range(25) == range(0,25): # un rango de una lista con intervalo cero puede escribirse con uno o dos argumentos, siendo el cero el segundo
    print("los rangos comparados son iguales")
else:
    print("los rangos comparados son diferentes")
print(range(25)) #imprimir un rango muestra el intérvalo en la pantalla
print("Creación de lista con rango e intervalo definido.\n La lista tendrá un rango de 10 a 20")
paso = int(input("por favor, agrega un número entero positivo como intérvalo: "))
lista =list(range(10,20,paso)) #el tercer parámetro es un entero positivo que representa los saltos entre número y número de la lista
print(lista)
            



