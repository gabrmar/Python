import string
import finpy

tasa = 1.5 #Interés efectivo mensual
cuota = 2e4 #Cuota mensual 
monto = 1e5 #Monto adeudado

analisis = finpy.icompuesto(tasa,cuota,monto) # La vairbale de salida es un objeto de tipo análisis si el préstamo se puede pagar
if type(analisis) == str:
    print("-------Error----------------")
    print(analisis)
else:
    print("Evolución del capital:",analisis.lista_capi)
    print("Evolución de los intereses generados",analisis.lista_inter)
    print("Capital pagado incluyendo intereses:",analisis.capitalTotal)
    print("Intereses generados durante el préstamo:",analisis.interesesTotales)
    print(f"Proporción de intereses: {analisis.proporcion}%")
    print(finpy.formato(analisis.interesesTotales))

#-------Exportar los datos en un archivo de texto-----------

#Redondeando listas a valores enteros

#Removiendo llaves de las listas
aux = str(analisis.lista_capi)
aux = aux[1:]
fila1 = aux[:len(aux)-2]
aux = str(analisis.lista_inter)
aux = aux[1:]
fila2 = aux[:len(aux)-2]

#------Versión sin formato 
lista1 = "Evolucion del capital: " + fila1
lista2 = "Evolucion de los intereses: " + fila2
#------Crear una lista de listas para cada cadena de mensajes

archivo = open("Resultados.txt","w")
archivo.write(lista1)
archivo.write("\n")
archivo.write(lista2)
archivo.close()