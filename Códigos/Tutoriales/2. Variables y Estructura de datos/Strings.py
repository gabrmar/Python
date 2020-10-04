
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
x = input("Primer número:") # El número que se guarde en la variable x es tomado como si fuera  un caracter, sólo texto
x = int(x) # De esta forma se le indica a Python que trate al contenido de la variable x como  un número entero en vez de texto 
x = x*2
print("El valor número multiplicado por 2  es " + str(x)) # La función print() sóolo trabaja con texto, así que  es necesario  formatear
# la variable x de nuevo a texto por medio de la función str()

# Usando la función format
y = input("Segundo número:")
y = float(y) # float() permite tratar el contenido de la variable como un número flotante, es decir un número  on punto decimal
z = y*3.14 # Gracias a ello, el resultado de esta multiplicación será un número con parte entera y dos cifras decimales 
print("{a} multilicado por 3.14 es {b}".format(a=y,b=z)) # Usar la función format() es una forma más cómoda de formatear lo que quieras
# colocar dentro de un mensaje de print ya que esta función se encarga de revisar el contenido de las variables que le coloques y las
# ajusta a texto. Lo importante con format() es dejar una llave con una variable por cada espacio donde quieras instertar variables del
# Código 

# Usando f""
print(f"Sumando los valores de {x} y {z}") # Ésta es la forma más rápida ya que el formateo sólo requiere la letra f antes del mensaje
# del print y las llaves con los nombres de las variables que deseas mostrar en el mensaje
suma = x + z
print(f"Suma total:{suma}")


"""
1) Enlace de formateo/casteo de variables  en Python
"""