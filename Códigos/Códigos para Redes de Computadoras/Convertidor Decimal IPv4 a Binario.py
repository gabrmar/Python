import ipv4, random
dec = []  #Plantilla para rellenar una dirección IPv4 aleatoria
i = 0
while i < 4:
    dec.append(random.randint(0,255))
    i = i + 1

print(f"Dirección IPv4 en decimal:{dec}")    
bin_ipv4 = ipv4.dec2bin_ipv4(dec) # Conversión a binario
print(f"Dirección IPv4 en binario:{bin_ipv4}")