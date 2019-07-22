"""
Los set son estructuras de datos similares a los direccionarios, de hecho
también son formados por medio de llaves {}, pero también pueden ser formados
por el uso de listas (agrupadas en corchetes) y la función set(lista)
"""
lista = ["hola",3,"PI"]
set1 = set(lista)
set2 = {1,2,3,4}
print(set1)
print(set2)

if "hola" in set1: #se puede usar la declaración in para buscar elementos
    print("coincidencia de palabra encontrada")
if 4 in set2:
    print("Coincidencia de número encontrada")
# puedes utilizar alguna delcraciones que se usaban con las listas para trbajar
# con sets (por ejemplo el uso de len()
# set() genera un set vacío

#Características de los Sets
#1: no son indexados
#2: No eliminan de manera automática elemetos repetidos
#3: son variables  de las cuales se pueden obtener datos de forma más rápida
# que las estructuras de datos indexados
nums = {1, 2, 1, 3, 1, 4, 5, 6}
print(nums)
nums.add(-7) # añade el -7 a la lista
nums.remove(3) # remueve el 3 de la lista
print(nums)
nums.pop() # elimina un elemento de forma arbitraria
print(nums)
print(len(nums)) # longiutd del set

#Sets con operaciones matemáticas
#Unión de sets, intersección de sets, diferencia de sets y diferencia simétrica
primer = {1, 2, 3, 4, 5, 6}
segundo = {4, 5, 6, 7, 8, 9}
print(primer)
print(segundo)
print(primer | segundo) # operación de unión (eliminando repetidos)
print(primer & segundo) # elementos en común (interesección)
print(primer - segundo) # muuestra los elementos que están en el primer set
# que no hacen parte del segundo (diferencia)
print(segundo - primer) # muestra los elementos que están en el segundo set
# que no hacen parte del primero
print(primer ^ segundo) #Muestra los elementos únicos en cada set en un sólio
# set (diferencia simétrica)
