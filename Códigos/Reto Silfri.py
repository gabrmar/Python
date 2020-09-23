

num1 = int(input("Primer número: "))
num2 = int(input("Segundo número: "))

numeros = [num1,num2]

lista_ordenada = sorted(numeros)

print("El número mayor es " + str(lista_ordenada[1]))