decimal = 200
binario = [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ]
bit = 7
if decimal > 255:
    print("El número decimal seleccionado debe ser menor a 256")
else:
    for i in binario:
        binario[bit] = decimal%2
        decimal = decimal//2
        bit = bit -1
    print(binario)