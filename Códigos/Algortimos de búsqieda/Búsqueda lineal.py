import random  # Módulo para generación de números aleatorios en Python

def busqueda_lineal(lista, objetivo): # Definiendo función  de búsqueda lineal
    match = False # por defecto se considera que el valor buscado no se encuentra, por ende es falso 
 
    for i in lista: # Incio de la búsqueda elemento por elemento 
        if i == objetivo: # Si el elemento en la lista es igual al número objetivo, entonces se detiende la búsqueda
            match = True 
            break # Fin de la búsqueda
    
    return match # regresa el resultado de ls búsqueda

if __name__ == "__main__": # Dunder init
    tamaño = int(input("Define el tamaño de la lista:"))
    objetivo = int(input("¿Qué número quieres encontrar?:"))

    Lista = [random.randint(0, 100) for i in range(tamaño)] # Definir 
    # random.randint(0, 100) genera un número aleatorio entre 0 y 99. Por otro lado, la función range() nos premite crear en un objeto
    # iterable para ser reocrrido por medio del ciclo for. Combinar estos dos en una lista nos permite generar una lista de números
    # aleatorios 
    
    print(Lista)
    encontrado = busqueda_lineal(Lista, objetivo)

    print(f'El número {objetivo} {"está " if encontrado == True else "no está" } en la lista')
    # El == True es opcional y puede ser eliminado  de la línea anterior que que se entiende en la sintaxis que se quiere evaluar
    # Si la variable encontrado es igual a verdadero  
    


