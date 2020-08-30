import time 

# Teorías

def factorial_iterativo(x):
    if x == 1:
        return 1
    else:    
        fact = x
        while x > 1:
            fact = fact * x - 1
            x = x - 1
        return fact 

def factorial_recursivo(x):
  if x == 1: #Caso base de la recursividad.  Toda funnción
      #recursiva debe tener un caso base que de final a la función,
      # de lo contrario esta correrá hasta que aparezca un error de
      # tiempo de ejecución (Runtime error)
    return 1
  else: 
    return x * factorial(x-1)

# Prueba de complejidad temporal