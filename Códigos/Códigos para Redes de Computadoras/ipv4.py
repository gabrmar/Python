import random

#----Misceláneos 

def padding(bin_list):

    if len(bin_list) < 8: 
        while len(bin_list) != 8:
            bin_list.insert(0,"0")

    return bin_list

def formant_bin(bin_list):
    
    #----Convertir lista entera a cadena string
    cadena = ""
    for i in bin_list:
        cadena = cadena + str(i)
    

    return cadena

def rand_ipv4(mode="d"):
    if mode=="d":
        dec_ipv4 = []  #Plantilla para dirección IPv4
        i = 0
        while i < 4:
            dec_ipv4.append(random.randint(0,255))
            i = i + 1
        address = dec_ipv4
    elif mode=="b":
        bin_ipv4 = [[],[],[],[]]  #Plantilla para dirección IPv4
        i = 0
        while i < 4:
            j = 0
            while j < 8:
                bin_ipv4[i].append(random.randint(0,1))
                j = j + 1
            i = i + 1
        address = bin_ipv4 

    return address

#-----conversiones

def bin2dec(bin_str): #Convertir un binario de 8 bits a decimal
    
    #---Formateando string binaria a lista

    bin_list = []
    for i in  bin_str:
        bin_list.append(int(i))
    bin_list = padding(bin_list) #Añadiendo ceros para tener el tamaño de 8 bits en caso de ser menor a este

    decimal = 0
    bit = 7

    for i in bin_list:
        if i == 1:
            decimal = decimal + pow(2,bit)
        bit = bit - 1

    return decimal

def bin2dec_ipv4(bin_ipv4_list): #Convertir una dirección IPv4 en binario a su versión decimal
    decimal_list = [0,0,0,0]
    bytes = 4
    i = 0

    while i < bytes:
        decimal_list[i] = bin2dec(bin_ipv4_list[i]) 
        i = i + 1
    return decimal_list

def dec2bin(decimal): #Convertir un número decimal a binario
    binario = [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ]
    bit = 7

    if decimal > 255:
        print("El número decimal seleccionado debe ser menor a 256")
    else:
        for i in binario:
            binario[bit] = decimal%2
            decimal = decimal//2
            bit = bit -1
    
    binario = formant_bin(binario)
    return binario

def dec2bin_ipv4(dec_ipv4_list): #Conversión de dirección IPv4 en decimal a su formato en binario
    bin_list = [0, 0, 0, 0]
    bytes = 4
    i = 0

    while i < bytes:
        bin_list[i] =dec2bin(dec_ipv4_list[i])
        i = i + 1
    
    # ----Formateando salida a estilo de IPv4

    cadena = ""
    for i in bin_list:
        if bin_list.index(i) == len(bin_list) -1:
            cadena = cadena + i
        else:
            cadena = cadena + i +". "

    return cadena


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