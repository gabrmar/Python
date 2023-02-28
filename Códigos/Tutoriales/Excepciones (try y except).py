""""
Las excepciones son bloques de código utilizados para  tratar con errores durante la ejecución
del código. Errores comunes son el ingreso de datos que no corresponden con el tipo de variable,
división por cero u operaciones con el tipo equivocado  de variable.

Python maneja  un repertorio de operaciones predefinidas (built-in exceptions) que ya tienen
un bloque de código establecido de los cuales podemos modificar para establecer instrucciones
personlizadas. La lista de ecepciones peredefinidas está disponible en internet.
"""
 
for i in range(3):  #definiendo ciclo indefinodo
    num1 = float(input("Agrega un número: "))
    num2 = float(input("Agrega un número: "))
    nombre= input("nombre de la operación: ")
    try: #bloque de código que se ejecuta nromalmente y donde puede ocurrir un error
        print(i+1) 
        div = num1/num2 
        print (div)
        print("Done calculation")
        print("operación" + nombre + "da como resultado "  + div) #esta línea genera un error de tipo
    # por no haber convertido la variable  div a string
    except ZeroDivisionError: # especificación del tipo de excepción (built-in excepcion)
        print("error ocurrió por división por cero")
    except(ValueError,TypeError): #múltiples excepciones con un solo except
    #agrupando las excepciones entre paréntesis
        print("error por valor o tipo equivocado")
    finally: # Bloque de código que se ejecuta en todo momento (haya o no error)
        print("instrucción de finally")
        
for i in range(3):
    print("manejando una excepción para todo error")
    num1 = float(input("Agrega un número: "))
    num2 = float(input("Agrega un número: "))
    try:
        div = num1/num2
        print(div)
        print("Done calculation")
    except: #excepción para todo tipo de error
        print("Ha ocurrido un error. No preguntes cuál es porque este es una excepción general (para todo error)")

for i in range(3):
        print("manejando excepciones con declaración raise")
        num1 = float(input("Agrega un número: "))
        num2 = float(input("Agrega un número: "))
        if num2 == 0:
            #raise ValueError #declaración raise nos permite llamar a las excepciones predefinidas sin necesidad
            # de usar un try y un except
            raise ValueError("Colocaste un cero en el denominador.") #puedes colocar mensajes  en las excepciones
            #Persnalizadas de Ptython. quita el comentario del raise de arriba si no quieres un mensaje propio
        div = num1/num2
        print(div)
        print("Done calculation")

print("prueba de raise general")
try:
    num = 5 / "string" #cambia el valor del denominador para fomentar diferentes errores
    print("hola")
except:
    print("Un error ocurrió") # instrucción del bloque de error
    raise #al no colocar el tipo de error, raise busca el error que le corresponde


                   
    

