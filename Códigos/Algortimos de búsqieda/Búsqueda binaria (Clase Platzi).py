# -*- coding: utf-8 -*- 
# Para reconicimiento de caracteres especiales como símbolos
# propios del español

# Definición de función de búsqueda binaria en uan lista.
# Sólo funciona con números binarios.
def binary_search(numbers, number_to_find, low, high):

    if low > high: # Dado que se trata de una función recursiva,
        # Si esta condición se cumple sin que se haya encontrado el número,
        # es por que ya no se puede dividir más la lista y por ende no 
        # se encontró el número. Este es el primer caso base para la función recursiva
        return False

    # Creación de punto medio que parte la lista en dos.
    # Se asegura que la división de un número entero.
    mid = int((low + high) / 2 )
    
    # Caso en el que el número a buscar está en la mistad de la lista. Segundo caso base
    if numbers[mid] == number_to_find:
        return True
    # Caso en que el número a buscar es menor que el número que está en la mitad de la lista
    elif numbers[mid] > number_to_find:
        # repetir la búsqueda binaria pero desde la mitad inferior de la lista
        return binary_search(numbers, number_to_find, low, mid - 1)
    # Caso en el que el número a buscar es mayor que el número que se encuentra en la mitad de la lista     
    else:
        # repetir búsqueda binaria pero desde la mitad superior de la listsa 
        return binary_search(numbers, number_to_find, mid + 1, high)


#Inicio de ejecución de código de Python
if __name__ == '__main__':
    #Lista de números ordenados
    numbers = [1, 3, 4, 5, 6, 9, 10, 11, 25, 27, 28, 34, 36, 49, 51]

    number_to_find = int(input('Ingresa un número: '))

    result = binary_search(numbers, number_to_find, 0, len(numbers) - 1)

    if result is True:
        print('El número sí está en la lista.')
    else:
        print('El número NO está en la lista.')
