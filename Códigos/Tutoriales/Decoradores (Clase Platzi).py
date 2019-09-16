# Definición de función de protección de contraseña
def protected(func):
    
    # Definición de función que mensaje de respuesta si la contraseña es acertada o no
    def wrapper(password):

        if password == 'platzi':
            # Regresar una función si se cumple la contraseña platzi
            return func()
        else:
            print('La contraseña es incorrecta')
    # Regresar objeto wrapper. Nota: no regresar la función wrapper()
    # porque genera un error. 
    return wrapper


@protected
def protected_func():
    print('Tu contraseña es correcta.')


if __name__ == '__main__': #Función principal
    password = input('Ingresa tu contraseña: ') #Ingreso de contraseña
    protected_func(password) # Función de contraseña con decorador
