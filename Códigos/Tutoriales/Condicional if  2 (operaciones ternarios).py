# Operadores ternarios
# escribir operadores ternarios ayuda reducir las líneas de código
# al definir el valor de una variable en fucnión de una condición if
# en una sola línea de código
a = 4
b = 1 if a >= 5 else 42 #condición ternaria
print(b)

status  = 2
msg = "Logout" if status == 1 else "Login" #operación ternaria
print(msg)


"""
Los else se pueden colocar fuera de ciclos(para y mientras) como manera
de ejecutar una inistrucción en caso de que el ciclo termine en condiciones
normales, es decir sin niguna salida forzada por un break.

Honestamente, me parece que no es necesario usarlos, ya que el uso del else
no es indispensable, pero se acepta que ayuda a la lectura del código
"""

for i in range(10):
   print(i)
   if i == 999:
      break
else:
    print("Unbroken 1")

for i in range(10):
   print(i)
   if i == 5:
      print("rotura de ciclo")
      break
else: 
   print("Unbroken 2")
print("-------------------------")

"""
Los else también pueden usarse como parte del código que se ejecuta
en conjunto con los try
"""
try:
   print(1)
except ZeroDivisionError:
   print(2)
else:
   print(3)

try:
   print(1/0)
except ZeroDivisionError:
   print(4)
else:
   print(5)
