import ipv4

numero = ipv4.rand_ipv4("b")
numero_2 = ipv4.rand_ipv4("b")
cadena = ipv4.format_bin(numero[0]) #Sólo se va a extraer una  de las 4 listas que confirman la dirección IPv4 en binario
cadena_2 = ipv4.format_bin(numero_2[0]) #Esto se debe a que la rutina format_bin() recibe de enetrada una lista, no una lista de listas.
a = cadena
b = cadena_2
print("Número: ",a)
print("Número 2: ",b)
sum = ipv4.sum_bin(a,b) #Toca analizar el alcance de esta función de suma cuando los valores superan los límites de un byte
print(f"La suma de los números binarios es: {sum}")

