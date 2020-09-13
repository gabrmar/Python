import random  # Móulo de funciones generadores de valores aleatorios 


def ordenamiento_de_burbuja(lista): # Función de ordenamiento burbuja
    n = len(lista) # Función que obtiene el tamaño de la lista

    for i in range(n):
        for j in range(0, n - i - 1): # O(n) * O(n) = O(n * n) = O(n**2)  Big O notation. Esta es una función O(n^2)

            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]  # Notación ene Python para intercambiar elementos
                # Se puede probar esta notación para hacer otro tipo de operaciones además de intercambiar valores de la lista.

    return lista # Regresar lista

if __name__ == '__main__':
    tamano_de_lista = int(input('De que tamano sera la lista? '))  # Se define el tamaño de la lista

    lista = [random.randint(0, 100) for i in range(tamano_de_lista)] # Generación de lista con números aleatorios
    print(lista)

    lista_ordenada = ordenamiento_de_burbuja(lista) # Llamando a la función de ordenamiento burbuja
    print(lista_ordenada)