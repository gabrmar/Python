import ipv4

decimal = int(input("Coloca el número decimal que quieres convertir a binario: "))
binario = ipv4.dec2bin(decimal)
dirección = ipv4.format_bin(binario)
print(f"El número {decimal} convertido en binario es {binario}")