import ipv4

dec = ipv4.rand_ipv4()

print(f"Dirección IPv4 en decimal:{dec}")    
bin_ipv4 = ipv4.dec2bin_ipv4(dec) # Conversión a binario
print(f"Dirección IPv4 en binario:{bin_ipv4}")