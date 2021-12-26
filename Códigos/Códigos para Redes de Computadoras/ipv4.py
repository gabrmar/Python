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
#----Otros 