import random  #Librería para funciones generadores de números aleatorios 

def ordenamiento_por_mezcla(lista): # Definiendo función de ordenamiento por mezcla 
    if len(lista) > 1:
        medio = len(lista) // 2 # El punto medio se calcula por medio de una  división entera (//), es decir una devisión que no da valores
        # decimales
        izquierda = lista[:medio] # Se genera una sub-lista desde el inicio hasta el punto medio -1
        derecha = lista[medio:] # Se genera una sub-lusta desde el punto medio hasta el final  
        print(izquierda, '*' * 5, derecha) # Se imprime el contenido de las dos listas sepatados por 5 asterístos (*)

        # llamada recursiva en cada mitad
        ordenamiento_por_mezcla(izquierda)
        ordenamiento_por_mezcla(derecha)

        # Iteradores para recorrer las dos sublistas
        i = 0
        j = 0
        # Iterador para la lista principal
        k = 0

        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1

            k += 1

        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k +=1

        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1
        
        print(f'izquierda {izquierda}, derecha {derecha}')
        print(lista)
        print('-' * 50)

    return lista


if __name__ == '__main__':
    tamano_de_lista = int(input('De que tamano sera la lista? '))

    lista = [random.randint(0, 100) for i in range(tamano_de_lista)]
    print(lista)
    print('-' * 20)

    lista_ordenada = ordenamiento_por_mezcla(lista)
    print(lista_ordenada)


"""
Referencias
1) Ordenamiento por mezcla: http://www.pythondiario.com/2018/08/ordenamiento-por-mezcla-merge-sort.html
2) Recursividad en Python: https://entrenamiento-python-basico.readthedocs.io/es/latest/leccion5/funciones_recursivas.html
3) Cadena de caracteres en Python: https://thepythonguru.com/python-strings/


"""