import string
import stringprep
from tokenize import String
import finpy

tasa = 1.5 #Interés efectivo mensual
cuota = 2e4 #Cuota mensual
monto = 1e5 #Monto adeudado

analisis = finpy.icompuesto(tasa,cuota,monto) #La variable deentrada es un diccionario
if isinstance(analisis,str): #Evaluando el tipo de variable entregada por la función
    print(analisis)
else:
    print(type(analisis))
    print(analisis.lista_capi)
    print(analisis.lista_inter)
    print(analisis.capitalTotal)
    print(analisis.interesesTotales)
    print(analisis.proporcion)

