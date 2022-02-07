from wsgiref.validate import validator
import finpy

tasa = 1.5 #Interés efectivo mensual
cuota = 2e4 #Cuota mensual
monto = 1e5 #Monto adeudado

analisis = finpy.icompuesto(tasa,cuota,monto) #La variable deentrada es un diccionario
for k,v in analisis.items():
    print(f"{k}: {v}")