import ipv4

aux = input("Coloca el número binario a convertir: ")

#-----formateando entrada para que sea una lista de valores enteros 

binario = []
for i in  aux:
    binario.append(int(i))

decimal = ipv4.bin2dec(binario) #Está en consideración si se necesita colocar el formateo dentoro de la librería IPv4
print(decimal) 