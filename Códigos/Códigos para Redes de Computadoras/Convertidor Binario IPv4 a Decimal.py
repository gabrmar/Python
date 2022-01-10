import ipv4

bin = ipv4.rand_ipv4("b")
#Colocar acá la rutina/función donde se formatea la dirección binaria
dirección = ipv4.format_IPv4(bin,"b")
print(f"Dirección IPv4 en binario: {dirección}")    
dec_ipv4 = ipv4.bin2dec_ipv4(bin) # Conversión a decimal 
#Segundo formateo pero esta vez de lista decimal a dirección IPv4
dirección_dec = ipv4.format_IPv4(dec_ipv4)
print(f"Dirección IPv4 en decimal: {dirección_dec}")