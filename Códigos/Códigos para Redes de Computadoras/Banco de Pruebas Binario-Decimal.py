import random, ipv4 # Módulo para funciones pseudo-aleatorias y librería personalizada de IPv4

print("Bienvenido") 
pruebas = 2
binario = [0, 0, 0, 0, 0, 0, 0, 0]
aciertos = 0
i = 0
while i < pruebas:
    j = 0
    while j < len(binario):
        binario[j] = random.randint(0,1) # Geberando número binario "al azar"
        j = j + 1
    print("número binario número {a}: {b}".format(a=i+1,b=binario))

    # -------Sección de validación de número decimal-----------

    decimal_calc = ipv4.bin2dec(binario)

    decimal = int(input("¿Cuál es el valor decimal del número binario mostrado?:"))
    i = i + 1

    # ------Sección de presentación de resultados--------

    if decimal == decimal_calc:
        print(f"¡Correcto! el valor decimal de {binario} es {decimal}")
        aciertos = aciertos + 1
    else:
        print(f"Incorrecto. El valor decimal de {binario} es {decimal_calc}")

print(f"puntuación: {aciertos} correctas de {pruebas} intentos.")