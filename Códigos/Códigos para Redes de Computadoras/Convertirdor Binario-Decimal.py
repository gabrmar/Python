import ipv4

binario = input("Coloca el número binario a convertir: ")
decimal = ipv4.bin2dec(binario) #Está en consideración si se necesita colocar el formateo dentoro de la librería IPv4
print(f"El número {binario} convertido en decimal es {decimal}")