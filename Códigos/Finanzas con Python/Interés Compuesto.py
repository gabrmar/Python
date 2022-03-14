import string
import finpy

tasa = 1.5 #Interés efectivo mensual
cuota = 2e4 #Cuota mensual 
monto = 1e5 #Monto adeudado  -----Probar con un monto mayor------

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

#-------Exportar los datos en un archivo de texto *****Volver esto una función*********-----------

#Redondeando listas a valores enteros
i = 0
aux = 0
auxl = []
while i < len(analisis.lista_capi) - 1:
    aux = int(analisis.lista_capi[i])
    auxl.append(aux)
    i = i + 1
#Removiendo llaves de las listas
aux = str(auxl)
aux = aux[1:]
fila1 = aux[:len(aux)-2]
#--
i = 0
aux = 0
auxl = []
while i < len(analisis.lista_inter) - 1:
    aux = int(analisis.lista_inter[i])
    auxl.append(aux)
    i = i + 1
aux = str(auxl)
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