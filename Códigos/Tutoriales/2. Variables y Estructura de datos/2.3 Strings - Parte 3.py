"""
- Organizar sección de Strings con IF. Agregar comentarios sobre últimos cambios.

Como se ha dicho antes, las variables strings son cadenas de símbolos llamados caracteres. Es posible acceder a los caracteres que
hacen parte de una string por medio de un número que representa la posición del caracter que queremos extraer dentro de unos corchetes.
Las posiciones de cada caracter  se cuentan desde el cero hasta el último valor, es decir que en el caso del string "hola", el conteo
empieza en 0 que se reifere a la letra h y termina en 3 con la letra a.

 """

x = "Mensjae"  # Variable string.
a = x[1] # Sacando la letra que se encuentra en la posición 1 del string. Reucerda que un string es lo mismo que una lista de caracteres.
# Gracias a ello es que se pueden aplicar muchas de las funciones de listas en una variable tipo string.
print(a) # Motrando el caracter extraído del string


"""
Unicode

Todos los símbolos que escribes en el teclado son representados internamente con números que fueron definido por medio de un estándar
que hoy conocemos como Unicode. Todos los computadores son capaces de interpretar el texto proveniente de otro equipo gracias a que todos
siguen las reglas Unicode para poder indentificar cada letra y símbolo. En Python podemos ver el número Unicode que representa cada uno
de los caracteres.
"""


b = ord(a) # Obtiene el códgo Unicode que representa el caracter
print(f"El número que representa el caracter {a} es {b}.")
code = 100 # Número entero cualquiera. La cantidad de números enteros que se usan dentro de la Tabla Unicode es de miles de números.
# Prueba con el número que quieras si queires conocer cuan grande es la tabla Unicode.
c = chr(code) # Obtiene el caracter que es representado por un número entero en la tabla Unicode
print(f"El número {code} representa el símbolo {c} en la tabla Unicode.")

"""
Condicionales IF usando variables string

Por extraño que pueda parecer a simple vista, en Python se pueden comparar variables strings usando los comparadores de mayor y menor que
como si se tratasen de númros. Esto se puede gracias a que lo que se hace es la comparación de los códigos Unicode que conforman cada 
caracter. Por ejemplo, si tienes dos strings y quoeres ver quien es mayor que a otra, entonces primero se compara el primer caracter de 
cada string. Si son iguales en valor Unicode, entonces se repite el proceso con los cracteres inmediatos. Si todos los caracteres
correspondientes tienen el mismo valor Unicode, es porque las strings son iguales.

NOTA: es importante resaltar que una letra en miníscula tiene un valor Unicode difernete al de su versión en mayúscula.

"""


print("-----------------------------------------")
print("")
print("Comparación de strings")
s1 = "hola"
s2 = "Hola"
print("")
print(f"String 1:{s1}")
print(f"String 2:{s2}")
print("")
print(f"Valores Unicode de los caracteres en el string {s1}")
for i in s1:
    x = ord(i)
    print(f"El valor Unicode de {i} es {x}")
print("******************************************")
print(f"Valores Unicode de los caracteres en el string {s2}")
for i in s2:
    x = ord(i)
    print(f"El valor Unicode de {i} es {x}")
if s1 > s2:
    print(f"{s1} es una string mayor que {s2}")
else:
    print(f"{s2} es una string mayor que {s1}")


"""
Refrencias:

1) Unicode: https://es.wikipedia.org/wiki/Unicode

"""
