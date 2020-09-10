# Iniciar comentarios

import random 

def busqueda_lineal(lista, objetivo):
    match = False

    for i in lista:
        if i == objetivo:
            match = True
            break
    
    return match

if __name__ == "__main__":
    tamaño = int(input("Define el tamaño de la lista:"))
    objetivo = int(input("¿Qué número quieres encontrar?:"))

    Lista = [random.randint(0, 100) for i in range(tamaño)] # Definir 
    print(Lista)

    encontrado = busqueda_lineal(Lista, objetivo)

    print(f'El número {objetivo} {"está " if encontrado else "no está" } en la lista') # especificar comentarios
    


