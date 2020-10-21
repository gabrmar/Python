"""
- Organizar sección de Strings con IF

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

 #----------------------------------------------If con Strings--------------------------




s1 = "hola"
s2 = "Hola"
if s1 > s2:
    print("Hola")
else:
    print("Hola 2")
# La compración entre cadenas de caracteres (strings) se hace la siguiente manera:
"""
Se hace comparación el primer caracter de cada  string. Si son iguales en valor ASCII,
entonces se repite el proceso con los cracteres inmediatos. Si todos los caracteres
correspondientes tienen el mismo valor ASCII, es porque las strings son iguales.

NOTA: es importante resaltar que una letra en miníscula tiene un valor ASCII difernete
al de su versión en mayúscula.
"""

"""
Refrencias:

1) Unicode: https://es.wikipedia.org/wiki/Unicode

"""
