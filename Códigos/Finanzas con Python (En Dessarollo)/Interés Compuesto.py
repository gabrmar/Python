import string
import finpy

tasa = 1.98 #Interés efectivo mensual
cuota = 181004 #Cuota mensual
monto = 5.5e6 #Monto adeudado
analisis = finpy.icompuesto(tasa,cuota,monto) # La vairbale de salida es un objeto de tipo análisis si el préstamo se puede pagar

print("Evolución del capital:",analisis.lista_capi)
print("Evolución de los intereses generados",analisis.lista_inter)
print("Capital pagado incluyendo intereses:",analisis.capitalTotal)
print("Intereses generados durante el préstamo:",analisis.interesesTotales)
print(f"Proporción de intereses: {analisis.proporcion}%")
print(finpy.formato(analisis.interesesTotales))
#print(finpy.formato(-10)) #Habilita esta función para probar el error de aserción
#print(finpy.formato(0.123456789)) #Habilita esta función para probar el formato con líneas decimales

#-------Exportar los datos en un archivo de texto -----------

finpy.exportar(analisis)