import random

print("Bienvenido") 
pruebas = 2
binario = [0, 0, 0, 0, 0, 0, 0, 0]
aciertos = 0
i = 0
while i < pruebas:
    j = 0
    while j < len(binario):
        binario[j] = random.randint(0,1)
        j = j + 1 
    print("número binario número {a}: {b}".format(a=i+1,b=binario))

    decimal_calc = 0
    bit = 7

    for k in binario:
        if k == 1:
            decimal_calc = decimal_calc + pow(2,bit)
        bit = bit - 1

    decimal = int(input("¿Cuál es el valor decimal del número binario mostrado?:"))
    i = i + 1


    if decimal == decimal_calc:
        print(f"¡Correcto! el valor decimal de {binario} es {decimal}")
        aciertos = aciertos + 1
    else:
        print(f"Incorrecto. El valor decimal de {binario} es {decimal_calc}")

print(f"puntuación: {aciertos} correctas de {pruebas} intentos.")