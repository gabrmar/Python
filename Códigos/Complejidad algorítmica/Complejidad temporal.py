import time,sys 

# time para el manejo de funciones que miden el tiempo y sys para manejo de variables relacionadas con el intérprete      

# Teorías


def factorial_iterativo(x):
    if x == 1:
        return 1
    else:    
        fact = x
        while x > 1:
            fact = fact * (x - 1)
            x = x - 1
        return fact 

def factorial_recursivo(x):
  if x == 1: #Caso base de la recursividad.  Toda funnción
      #recursiva debe tener un caso base que de final a la función,
      # de lo contrario esta correrá hasta que aparezca un error de
      # tiempo de ejecución (Runtime error)
    return 1
  else: 
    return x * factorial_recursivo(x-1)

# Prueba de complejidad temporal

print(sys.getrecursionlimit()) # Imprime el valor por defecto del límite para recursividad. Valor por defecto de 1000
sys.setrecursionlimit(10000) # Cambiando el límite de recursión para soportar mayores recursiones 
print(sys.getrecursionlimit())

"""
Pendiente agregar comentarios
"""

t0 = time.time()
a = factorial_iterativo(500)  
t1 = time.time()
delta_it = t1 - t0
t1 = time.time()
b = factorial_recursivo(500) # límite de recursividad por defecto: 998
t1 = time.time()
delta_rec = t1 - t0
print(f"{a,b}")
print(f"{delta_it,delta_rec}")

