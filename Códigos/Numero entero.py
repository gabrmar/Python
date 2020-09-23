#Número entero 

num = input("Digite el número: ")
num = float(num)
entero = int(num)

diferencia = num - entero

if(diferencia == 0):
    print(f"El número {num} es entero")
else:
    print(f"El número {num} no es entero")

    