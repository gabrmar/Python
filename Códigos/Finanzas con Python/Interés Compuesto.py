import string
import finpy

tasa = 1.5 #Interés efectivo mensual
cuota = 2e4 #Cuota mensual 
monto = 1e5 #Monto adeudado

analisis = finpy.icompuesto(tasa,cuota,monto) #La variable de entrada es un diccionario ----Verificar esto ----
if type(analisis) == str:
    print(analisis)
else:
    print(analisis.lista_capi)
    print(analisis.lista_inter)
    print(analisis.capitalTotal)
    print(analisis.interesesTotales)
    print(analisis.proporcion)
    print(type(finpy.formato(analisis.capitalTotal)))
    print(finpy.formato(analisis.interesesTotales))