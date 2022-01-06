import ipv4

bin = ipv4.rand_ipv4("b")
print(f"Dirección IPv4 en binario:{bin}")    
dec_ipv4 = ipv4.bin2dec_ipv4(bin) # Conversión a decimal 
print(f"Dirección IPv4 en decimal:{dec_ipv4}")