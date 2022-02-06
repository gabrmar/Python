import finpy

tasa = 1.5 #Interés efectivo mensual
cuota = 50e3
monto = 5e6

analisis = finpy.icompuesto(tasa,cuota,monto)
print(analisis)