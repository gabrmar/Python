#-----conversiones

def bin2dec(bin_list):
    decimal = 0
    bit = 7

    for i in bin_list:
        if i == 1:
            decimal = decimal + pow(2,bit)
        bit = bit - 1

    return decimal

#-----Sumas en binario
#-----Cálculos de host(estaciones)
#----Otros 