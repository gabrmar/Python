
def ejemplo():
    # Las funciones en Python se escriben así: def nombre_de_función():
    # dentro de los paréntesis puedes colocar las variables que la función necesite para trabajar, pero también puedes hacer funciones
    # que no necesiten variables de entrada para funcionar.
    pass # esta palara se utiliza para indicar que de momento no se colocará nada en el código pero que de pretende en otro momento cambiar
    # el pass por el código que se quiere crear.

def suma(n1,n2): # Definiendo función suma de dos númeoros cualquiera que llamaremos n1 y n2
    total = n1 + n2
    return total # la palabra return se usa para indicar que el valor de una variable dentro de la función  se usará en otra parte del programa 

def saludo(nombre): # Definiendo función saludo usando un nombre cualquiera como entrada
    print(f"bienvenido al código de funciones, {nombre}")

#Código principal (main).

x = suma(1,2) # Mira como el resultado de la función suma se guara en la variable x gracias al uso del return
print(x) # Mostrando el valor de x
print(suma(3,5)) # También puedes imprir el resultado de la función suma sin la necesidad de guardarlo en una variable antes
saludo("Max")  #Este tipo de funciones no se asignan a ninguna variable porque  no tienen return dentro de ellas, es decir que las operaciones
# que hacen estas funciones sin return no son usadas en otra parte del código principal (también conocido como main)
saludo("María")
