import random  #Librería para funciones generadores de números aleatorios 

def ordenamiento_por_mezcla(lista): # Definiendo función de ordenamiento por mezcla 
    if len(lista) > 1:
        medio = len(lista) // 2 # El punto medio se calcula por medio de una  división entera (//), es decir una devisión que no da valores
        # decimales
        izquierda = lista[:medio] # Se genera una sub-lista desde el inicio hasta el punto medio -1
        derecha = lista[medio:] # Se genera una sub-lista desde el punto medio hasta el final  
        print(izquierda, '*' * 5, derecha) # Se imprime el contenido de las dos listas sepatados por 5 asterístos (*)

        # llamada recursiva en cada mitad
        ordenamiento_por_mezcla(izquierda) # Llamado recursivo con sólo la lista de la izquierda
        ordenamiento_por_mezcla(derecha) # Llamado recursivo con sólo la lista de la derecha

        # Iteradores para recorrer las dos sublistas
        i = 0
        j = 0
        # Iterador para la lista principal
        k = 0

        while i < len(izquierda) and j < len(derecha): # Mientras los iteradores sean menores a las longitudes de las sub-listas
            if izquierda[i] < derecha[j]: 
                lista[k] = izquierda[i] # si es elemento de la sub-lista izquierda es menor, entonces se asigna su valor en la lista principal
                i += 1 # i = i + 1
            else:
                lista[k] = derecha[j] # En su defecto, se colocará el elemento de la sub-lista derecha
                j += 1 # j = j + 1

            k += 1 # = k = k + 1

        while i < len(izquierda): # Mientras que el iterador i sea menor que la longitud de la sub-lista izquierda
            lista[k] = izquierda[i]  # Colocando los valores de la sub-lista en la lista principal
            i += 1
            k +=1

        while j < len(derecha): # Mientras que el iterador j sea menor que la longitud de la sub-lista derecha
            lista[k] = derecha[j] # Colocando los valores de la sub-lista en la lista principal
            j += 1
            k += 1
        
        print(f'izquierda {izquierda}, derecha {derecha}') # Imprimiendo sub-listas en cada llamado de la función
        print(lista) # Impresión de la lista ordenándose en cada una de las iteraciones. La lista se verá ordernada en esta línea en la 
        # última iteración de esta función de ordenamiento por mezcla
        print('-' * 50) # Imprimiendo una división formada por 50 guiones (-)

    return lista # Regresando lista  


if __name__ == '__main__': # Dunder init
    tamano_de_lista = int(input('De que tamano sera la lista? '))

    lista = [random.randint(0, 100) for i in range(tamano_de_lista)]
    print(lista)
    print('-' * 20) # Imprimiendo una división formada por 20 guiones (-)


    lista_ordenada = ordenamiento_por_mezcla(lista)
    print(lista_ordenada) # Imprimiendo lista ordenada 


"""
Referencias
1) Ordenamiento por mezcla: http://www.pythondiario.com/2018/08/ordenamiento-por-mezcla-merge-sort.html
2) Recursividad en Python: https://entrenamiento-python-basico.readthedocs.io/es/latest/leccion5/funciones_recursivas.html
3) Cadena de caracteres en Python: https://thepythonguru.com/python-strings/


"""