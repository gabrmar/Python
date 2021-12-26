import ipv4, random
bin = [[],[],[],[]]  #Plantilla para rellenar una dirección IPv4 aleatoria
i = 0
while i < 4:
    j = 0
    while j < 8:
        bin[i].append(random.randint(0,1))
        j = j + 1
    i = i + 1

print(bin)    
dec_ipv4 = ipv4.bin2dec_ipv4(bin) # Conversión a decimal 
print(dec_ipv4)