import string
import finpy

tasa = 1.5 #Interés efectivo mensual
cuota = 1e4 #Cuota mensual------ Probar con valores extremos como 1500 y menores -----
monto = 1e5 #Monto adeudado

analisis = finpy.icompuesto(tasa,cuota,monto) #La variable de entrada es un diccionario
print(analisis.lista_capi)
print(analisis.lista_inter)
print(analisis.capitalTotal)
print(analisis.interesesTotales)
print(analisis.proporcion)
print(type(finpy.formato(analisis.capitalTotal)))
print(finpy.formato(analisis.interesesTotales))