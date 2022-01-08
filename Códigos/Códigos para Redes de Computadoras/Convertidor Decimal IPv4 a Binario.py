import ipv4

dec = ipv4.rand_ipv4()

#Probar formateo de lista generada aquí. esta sólo debe usarse para firnes de presentación y 
#no para ser colocada dentro de la función dec2bin()

print(f"Dirección IPv4 en decimal:{dec}")    
bin_ipv4 = ipv4.dec2bin_ipv4(dec) # Conversión a binario
print(f"Dirección IPv4 en binario:{bin_ipv4}")