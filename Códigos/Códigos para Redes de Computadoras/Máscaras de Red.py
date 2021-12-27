import ipv4

ip_red = [192, 168 ,10 ,0]
#máscara = 24
#estaciones = pow(2,32-máscara) - 2
#print(estaciones)

output = ipv4.count_bin(ip_red,10)
print(output)
print(type(output))