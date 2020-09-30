"""
operadores booleanos

En python se pueden manejar muchos tipos de datos, desde enteros, fraciones, letras, palabras y mensajes completos. Adicionalmente, Python 
también maneja un tipo de dato conocido como booleano. Sólo existen  dos tipos de valires booleanos: verdaero (True) y falso (False). La
fucnión de los booleanos es ser usados para evaluar si alguna instrucción en Python es verdadera o falsa. Esto tiene aplicaciones más claras
en códigos que veremos más adelante. Por ahora, es importante saber que los booleanos existen en Python y cómo se escriben en este lenguaje. 

Éste código muestra cómo se escriben los booleanos en Python y algunas de sus operaciones básicas. Para más información sobre los operadores
en Python, pudes consultar este enlace:

Operadores booleanos en Python: https://www.mclibre.org/consultar/python/lecciones/python-booleanos.html

"""
 
v1 = True # Los booleanos se escriben con la letra en mayúscula inicial
v2 = False # De esta manera, hemos asignado los valores de verdadero y falso a las variables v1 y v2
print(str(v1) + " and " + str(v2)) # Imprimiendo los valores booleanos guardados en las vriables
print (v1 == v2) # Esto es una prueba booleana o prueba lógica. v1 == v2 compara las dos variables y verifica si son iguales. como True no es
# igual a False, entonces el resultado es falso (False en Python).
v2 = True # Como con cualquier otro tipo de dato, la variable puede ser modificada después para tener un valor booleano diferente.
print(v1 == v2) # Como ahora v2 también es verdadero (True), es cierto que v1 y v2 son iguales, por lo tanto esta compración da como resultado
# verdadero (True)
print (v1 != v2) # signo de admiación en Python significa "no". Es decir que en esta comparación se evalua si v1 y v2 no eran iguales. El
# resultado de esta compración es falso porque en este momento del código tanto v1 como v2 tienen como valor booleano como verdadero(True).


