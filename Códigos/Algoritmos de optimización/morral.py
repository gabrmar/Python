# 0-1 knapsack problem  (versión donde los pesos no se pueden dividir)

def morral(tamano_morral, pesos, valores, n): # Definiendo función morral especificando su tamaño, lista de pesos, lista de valores de
    # de valores y número de pesos a trabajar

    #Como se trata de una función recursiva, es necesario definir los casos base
    if n == 0 or tamano_morral == 0:  # si el número de pesos o el tamaño del morral es cero, entonces, regresa cero como base
        return 0

    if pesos[n - 1] > tamano_morral: # Si el último peso de la lista es mayor al tamaño del morral
        return morral(tamano_morral, pesos, valores, n - 1) # función recursiva con un peso menos

    return max(valores[n - 1] + morral((tamano_morral - pesos[n - 1]), pesos, valores, n - 1),morral(tamano_morral, pesos, valores, n - 1))
    # Se compara el máximo entre  la mochila con el peso del primer elemento contra el la mochila sin tener el peso de dicho elemento

if __name__ == '__main__':
    valores = [60, 100, 120] # Lista de valores
    pesos = [10, 20, 30] # Lista de pesos 
    tamano_morral = 50 # Tamaño del morral
    n = len(valores) # el número de pesos es igual a la longitud de la lista de valores

    resultado = morral(tamano_morral, pesos, valores, n)
    print(resultado) # Mostrar el resultado

"""
Referencias

1) https://en.wikipedia.org/wiki/Knapsack_problem
2) https://www.geeksforgeeks.org/python-max-function/


"""