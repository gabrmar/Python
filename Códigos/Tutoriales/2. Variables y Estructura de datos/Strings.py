
"""
- Introducción a las strings de Python
- Formateo con valores numéricos  
- Formateo con format()
- Formateo con f""
- Funciones báscias en strings en Python (Esto puede ir en otra función)
- Compraciones con un IF en una string 
- Slicing (Una tercera parte)
- Iterables de strings en Python (Cuarta parte)
"""

# Formateando variables
x = input("Primer número:")
x = int(x)
x = x*2
print("El valor número multiplicado por 2  es " + str(x))

# Usando la función format
y = input("Segundo número:")
y = float(y)
z = y*3.14
print("{a} multilicado por 3.14 es {b}".format(a=y,b=z))

# Usando f""
print(f"Sumando los valores de {x} y {z}")
suma = x + z
print(f"Suma total:{suma}")


"""
1) Enlace de formateo/casteo de variables  en Python
"""