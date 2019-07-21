print("Uso del ciclo para (while).\nElige un númnero desde el cual iniciará un conteo descendente")
conteo = int(input("Número de inicio: "))
while conteo > 0: #importante escribir los dos puntos al final de la condición
    print(conteo)
    conteo -=1 #forma corta de hacer la operación "conteo = conteo-1"
print("Fin del conteo")
respuesta = str(input("Este programa cuenta con la opción de ejecutiar un ciclo infinito. ¿Desea usarla? Y/N "))
if respuesta == "Y" or respuesta == "y":
    print("ciclo infinito iniciado. Use Control+C o cierre el programa para detenerlo")
    while True: # también aplica cualquier  operación lógica que  de como resultado True
        print("While infinito")
elif respuesta == "N" or respuesta == "n":
   print("OK. no se ejecuta el ciclo infinito.")
   print("Ahora se probará el  uso de la delcaración break.\nSe iniciará un ciclo de 100 interaciones que tendrá una interrupción en el valor que definas")
   ruptura = int(input("Define el valor donde se ejecutará la declaración break: "))
   if ruptura > 100 or ruptura < 0:
       print("No se puede hacer el conteo. El valor debe estar entre 0 y 100")
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
        
       
    
