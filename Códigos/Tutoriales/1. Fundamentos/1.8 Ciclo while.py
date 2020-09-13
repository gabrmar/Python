
"""
Uno de los ciclos básicos en la programaciónes el ciclo while (mientras que). Este ejecuta instrucciones dentro de su ciclo hasta que
una condición especificada deja de ser cierta. De ahí viene el nombre; es un ciclo que funciona mientras que su condición sea cierta. El código
a continuación muestra varios ciclos while.
"""

print("Uso del ciclo para (while).\nElige un númnero desde el cual iniciará un conteo descendente")
# El \n sirve para que el texto después de este se genere en una nueva línea. Este tipo de caracter ese le conoce como caracter de escape
# Al fnal del código hay un enlace con más información sobre ellos.
conteo = int(input("Número de inicio: "))
while conteo > 0: #  While (condición):  
    # Es importante escribir los dos puntos al final de la condición. 
    print(conteo)
    conteo -=1 #forma corta de hacer la operación "conteo = conteo-1".
print("Fin del conteo")
respuesta = input("Este programa cuenta con la opción de ejecutiar un ciclo infinito. ¿Desea usarla? Y/N ") # Datos tratados como string 
# por defecto.
if respuesta == "Y" or respuesta == "y":
    print("ciclo infinito iniciado. Use Control + C o cierre el programa para detenerlo")
    while True:  # Al reemplazar la condición por un True, entonces no hay forma de que el ciclo while se rompa porque  su "condición" siempre
    #  es verdad, lo cual nos dá como resultado un ciclo infinito. 
    # También se puede usar cualquier condición que siempre de como resultado True para que un ciclo sea infinito.
        print("While infinito. Use Control + C para detenerlo.")
elif respuesta == "N" or respuesta == "n":
   print("OK. No se ejecuta el ciclo infinito.")
   print("Ahora se probará el  uso de la delcaración break.\nSe iniciará un ciclo de 100 interaciones que tendrá una interrupción en el valor que definas")
    # Una forma de interrumpir ciclos sin que ninguna condición sea verdadera o falsa es por medio de la declaración break (romper).
    # Si hay un ciclo en ejecución y llega a toparse con un break, entonces el ciclo se termina inmediatamente.
   ruptura = int(input("Define el valor donde se ejecutará la declaración break: "))
   if ruptura > 100 or ruptura < 0:
       print("No se puede hacer el conteo. El valor debe estar entre 0 y 100. \nFin del programa. ")
   else:    
       conteo = 0
       while conteo <=100:
            print(conteo)
            conteo +=1
            if conteo == ruptura:
                break
       print("fin del conteo por break.")              
else: #En caso de que el usuario coloque una cualer letra o palabra  que no sea Y o N. También funciona si el usuario coloca números en vez de
    # vez de letras o incluso si no colocar ningun dato.
    print("comando inválido")
    print("Ahora se probará el  uso de la delcaración continue.\nSe se contarán sólo los valores pares o impares")
    # La declaración continue ingora una de las repeticiones del ciclo haciendo que este regrese al inicio del ciclo while sin importar si
    # habían instrucciones pendientes.
    respuesta = input("¿Qué tipo de conteo se hará?. Par/Impar ")
    conteo = 0
    if respuesta == "Par" or respuesta == "par":
     while conteo < 100:
        conteo +=1
        if conteo%2 == 0: #El uso de la operación módulo nos permite definir si el número es par o impar. Más información abajo del código.
            print(conteo)
        else:
            continue
    elif respuesta == "Impar" or respuesta == "impar":
     while conteo < 100:
        conteo +=1
        if not conteo%2 == 0:
            print(conteo)
        else:
            continue
        
"""
Referencias

1) \n y demás secuencias de escape en Python: https://tutz.tv/python/secuencias-de-escape/
2) Control de ciclos con break y continue: https://www.pythonmania.net/es/2013/04/05/control-de-bucles-break-continue-y-pass/
3) Operación módulo: https://yosoy.dev/operador-aritmetico-modulo/

"""       
    
