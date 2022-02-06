import finpy

tasa = 1.5 #Interés efectivo mensual
cuota = 1e3 #Cuota mensual
monto = 1e5 #Monto adeudado

analisis = finpy.icompuesto(tasa,cuota,monto) #La variable deentrada es un diccionario
for k,v in analisis.items():
    print(f"{k}: {round(v,0)}")