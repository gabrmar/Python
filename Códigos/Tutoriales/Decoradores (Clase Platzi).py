
#-----Clase de Python en Platzi sobre decoradores-------#

# Definición de función de protección de contraseña
# Cuando se trabaja con decoradores, lo usual es trabajar con fucniones anidadas.
# protected será la función principal de un nido de funciones la cual se le conoce
# como función de cierre ya que define (cierra, delimita)  el inicio y cierre del
# nido de funciones.
def protected(func):
    
    # Definición de función que mensaje de respuesta si la contraseña es acertada o no
    # Ésta función se le conoce como wrapper cuando se habla de decoradores.
    # Un wrapper es la función que se encuentra anidada dentro de la función principal
    # func es la función de entrada de la función protected.
    def wrapper(password):
        
        if password == 'platzi':
            # Regresar una función si se cumple la contraseña platzi
            return func() #regresar la funcion con paréntesis hace que la función se
            # ejecute cuando sea regresada.
        else:
            print('La contraseña es incorrecta')
    # Regresar objeto wrapper. Nota: no regresar la función wrapper()
    # porque genera un error al indicar que le falta un argumento a la función wrapper.
    return wrapper


@protected
def protected_func():
    print('Tu contraseña es correcta.')


if __name__ == '__main__': #Función principal
    password = input('Ingresa tu contraseña: ') #Ingreso de contraseña
    protected_func(password) # Función de contraseña con decorador
