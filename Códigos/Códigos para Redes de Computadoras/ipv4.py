#-----conversiones

def bin2dec(bin_list):
    decimal = 0
    bit = 7

    for i in bin_list:
        if i == 1:
            decimal = decimal + pow(2,bit)
        bit = bit - 1

    return decimal

def bin2dec_ipv4(bin_ipv4_list):
    decimal_list = [0,0,0,0]
    bytes = 4
    i = 0

    while i < bytes:
        decimal_list[i] = bin2dec(bin_ipv4_list[i]) 
        i = i + 1
    return decimal_list

def dec2bin(dec):
    pass

#-----Sumas en binario


#-----Cálculos de host(estaciones)

def count_bin(dec_ipv4_list,number):
    bytes = 4

    #-----Extraer números
    aux = []

    for i in dec_ipv4_list:
        aux.append(bin(i)) #Al formatear lo valores como binario quedan guardados como cadenas de caracteres con el prefijo 0b
    for i in aux:
        aux[aux.index(i)] = i[2:] #Eliminando prefijo 0b

    print(aux)

    # Agregar ceros de relleno en cada octecto

    i = 0
    while i < len(aux):
        if len(aux[i]) < 8:
            while len(aux[i]) < 8:
                aux[i] = "0" + aux[i]
        i = i + 1

        

    print(aux)

    #----- Concatenar
    aux2 = ""

    for i in aux:
        aux2 = aux2 + i
    
    #----- Contar
    # Leer https://www.geeksforgeeks.org/python-program-to-add-two-binary-numbers/

    pass


#----Otros 