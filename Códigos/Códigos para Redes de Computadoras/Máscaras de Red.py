import ipv4

address = ipv4.rand_ipv4() #Se genera lista que tiene números que representan una dirección IPv4
clase = ipv4.get_class(address)
print(f"La dirección es de clase {clase}")