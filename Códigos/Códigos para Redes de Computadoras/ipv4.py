import random

#----- Bloque de Formateo de datos

def padding(bin_list): #Rellenar con ceros a la izquierda los valores binarios que usen menos de 8 dígitos

    if len(bin_list) < 8: 
        while len(bin_list) != 8:
            bin_list.insert(0,"0")

    return bin_list

def format_bin(bin_list): #Convertir lista entera de números binarios a cadena string para mostrar un número binario como una sola variable string
    
    cadena = ""
    for i in bin_list:
        cadena = cadena + str(i)

    return cadena

def format_IPv4(list,mode="d"): #Convertir lista valores binarios o decimales a formato de dirección IPv4
    cadena = ""
    if mode == "d":
        for i in list:
            if list.index(i) == len(list) - 1:
                cadena = cadena + str(i)
            else:
                cadena = cadena + str(i) + "."
    elif mode == "b":
        for i in list:
            list[list.index(i)] = format_bin(i)
        for i in list:
            if list.index(i) == len(list) - 1:
                cadena = cadena + str(i)
            else:
                cadena = cadena + str(i) + ". "
    
    return cadena

#----- Bloque de rutinas de utilidad

def rand_ipv4(mode="d"): #Genera una dirección IPv4 aleatoria en sistema decimal o binario. Dicha dirección es entregada como lista
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

#***********conversiones

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
            bit = bit - 1
    
    return binario

def dec2bin_ipv4(dec_ipv4_list): #Conversión de dirección IPv4 en decimal a su formato en binario
    bin_list = [0, 0, 0, 0]
    bytes = 4
    i = 0

    while i < bytes:
        bin_list[i] = dec2bin(dec_ipv4_list[i])
        i = i + 1

    return bin_list


#***********Sumas en binario

def sum_bin(a,b):
    sum = int(a,2) + int(b,2)
    bin_sum = bin(sum)
    bin_sum = bin_sum[2:]
    
    return bin_sum

#********IP con clase

def get_class(dec_ipv4_list): #Definir la clase de la dirección IPv4 dada

    clases = {"A":0,"B":[1,0],"C":[1,1,0],"D":[1,1,1,0],"E":[1,1,1,1]}
    clase = "Indetermindada. Por favor revisar el código y corregirlo."

    bin_ipv4_list = dec2bin_ipv4(dec_ipv4_list)
    byte = bin_ipv4_list[0] #Sólo el primer byte es suficiente para determinar la clase
    #print("Byte de interés",byte)  habilitar esta línea siu se desea depurar la rutina.
    
    #Ver como se puede optimizar estos condicionales con una algún ciclo usando las llaves y cancelarcuando  se haya evaluado la clase C
    if byte[0] == clases["A"]:
        clase = "A"
    elif byte[0:2] == clases["B"]:
        clase = "B"
    elif byte[0:3] == clases["C"]:
        clase = "C"
    elif byte[0:4] == clases["D"]:
        clase = "D"
    elif byte[0:4] == clases["E"]:
        clase = "E"

    return clase


#******Cálculos de host(estaciones)

def count_bin(dec_ipv4_list,number):

    #----- Contar
    # Leer https://www.geeksforgeeks.org/python-program-to-add-two-binary-numbers/

    pass


#----Otros 