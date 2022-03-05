import string
import finpy

tasa = 1.5 #Interés efectivo mensual
cuota = 2e4 #Cuota mensual 
monto = 1e5 #Monto adeudado

analisis = finpy.icompuesto(tasa,cuota,monto) #La variable de entrada es un diccionario ----Verificar esto ----
if type(analisis) == str:
    print(analisis)
else:
    print("Evolución del capital:",analisis.lista_capi)
    print("Evolución de los intereses generados",analisis.lista_inter)
    print("Capital pagado incluyendo intereses:",analisis.capitalTotal)
    print("Intereses generados durante el préstamo:",analisis.interesesTotales)
    print(f"Proporción de intereses: {analisis.proporcion}%")
    print(type(finpy.formato(analisis.capitalTotal))) #Revisarla importancia de esta línea más tarde
    print(finpy.formato(analisis.interesesTotales))