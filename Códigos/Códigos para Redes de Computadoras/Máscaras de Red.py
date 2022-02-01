import ipv4
i = 0
while i < 100:
    address = ipv4.rand_ipv4() #Se genera lista que tiene números que representan una dirección IPv4
    IPv4 = ipv4.format_IPv4(address)
    print("Verificando clase de la dirección", IPv4 )
    clase = ipv4.get_class(address)
    print(f"La dirección {IPv4} es de clase {clase}")
    i = i + 1