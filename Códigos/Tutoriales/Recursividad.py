# Recursividad en Pýthon

def factorial(x):
  if x == 1: #Caso base de la recursividad.  Toda funnción
      #recursiva debe tener un caso base que de final a la función,
      # de lo contrario esta correrá hasta que aparezca un error de
      # tiempo de ejecución (Runtime error)
    return 1
  else: 
    return x * factorial(x-1)

#También se puede hacer recursividad  indirecta, es decir una función llamando a otra
# llama a la primera hasta termiar la operación por medio del caso base

def es_par(x):
  if x == 0:
    return True
  else:
    return es_impar(x-1)

def es_impar(x):
  return not es_par(x)


print(factorial(5)) # factorial 5 = 5*4*3*2*1
print(es_impar(17))
print(es_par(23))
