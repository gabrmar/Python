
"""
Aspectos por mejorar:

    -Un poco de teoría sobre el ciclo while
    -un poco de la teoría de los caracteres de escape prefriblemente español
    -Pulir los comentarios qie ya exísten en el código
    -Definir lo que hace este código 

"""
"""
Además del condicional if, otras de las formas de controlar cuáles instrucciones se ejecutan dentro de tu código. Una de ellas es indicando
que ciertos comandos se ejecuten cierto número de veces  hasta que se hayan repetido cierto número de veces o hasta que una condición
se haya cumplido. A este tipo de ejecución repetiva se le concen como ciclos (loops en inglés). Uno de los ciclos básicos en la programación
es el ciclo while (mientras que). 

Un Ciclo while ejecuta instrucciones dentro de su ciclo hasta que su condición deje de ser cierta. De ahí viene el nombre. es un ciclo
que funciona mientras que su condición sea cierta. El código a continuación muestra varios ciclos while.
"""

print("Uso del ciclo para (while).\nElige un númnero desde el cual iniciará un conteo descendente")
# El \n sirve para que el texto después de este se genere en una nueva línea. Este tipo de caracter ese le conoce como caracter de escape
# Al fnal del código hay un enlace con más información sobre los caracteres de escape.
conteo = int(input("Número de inicio: "))
while conteo > 0: #  While (condición):  
    # Es importante escribir los dos puntos al final de la condición. 
    print(conteo)
    conteo -=1 #forma corta de hacer la operación "conteo = conteo-1".
print("Fin del conteo")
respuesta = str(input("Este programa cuenta con la opción de ejecutiar un ciclo infinito. ¿Desea usarla? Y/N "))
if respuesta == "Y" or respuesta == "y":
    print("ciclo infinito iniciado. Use Control+C o cierre el programa para detenerlo")
    while True:  # Al reemplazar la condición por un True, entonces no hay forma de que el ciclo while se rompa porque  su "condición" siempre
    #  es verdad, lo cual nos dá como resultado un ciclo infinito. 
    # También se puede usar cualquier condición que siempre de como resultado true.
        print("While infinito")
elif respuesta == "N" or respuesta == "n":
   print("OK. no se ejecuta el ciclo infinito.")
   print("Ahora se probará el  uso de la delcaración break.\nSe iniciará un ciclo de 100 interaciones que tendrá una interrupción en el valor que definas")
    # Una forma de interrumpir ciclos sin que ninguna condición sea verdadera o falsa es por medio de la declaración break (romper).
    # Si hay un ciclo en ejecucióny llega a toparse con un break, entonces el ciclo se termina inmediatamente.
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
       print("fin de conteo por break")              
else:
    print("comando inválido")
    print("Ahora se probará el  uso de la delcaración continue.\nSe se contarán sólo los valores pares o impares")
    respuesta = input("¿Qué tipo de conteo se hará?.Par/Impar ")
    conteo = 0
    if respuesta == "Par" or respuesta == "par":
     while conteo < 100:
        conteo +=1
        if conteo%2 == 0:
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
        
       
    
