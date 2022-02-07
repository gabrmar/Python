#Interés Compuesto
from logging import captureWarnings
import math

class analisis:

    def __init__(self,capitalTotal = -1,interesesTotales = -1,proporcion = -1,lista_capi = [],lista_inter = []):
        self.capitalTotal = capitalTotal
        self.interesesTotales = interesesTotales
        self.proporcion = proporcion
        self.lista_capi = lista_capi
        self.lista_inter = lista_inter




def icompuesto(tasa_interes,cuota,monto):
    interesTotales = -1
    capitalTotal = -1
    proporcionIntereses = -1

    capt = []
    inter = []
   

    
    #Se necesita hacer una evaluación de los valores de cuota vs montos e intereses para que sean viables para el resto del
    #código

    intereses = monto*(tasa_interes/100)
    if intereses > cuota:
        return "Por favor aumentar el valor de la cuota para poder pagar este crédito con la tasa de interés actual"
    else:
        resultado = analisis()
        capital = monto #Capital adeudado 
        capitalTotal = monto
        while capital > 0:
            intereses = capital*(tasa_interes/100)
            #print("Intereses:",round(intereses,0)) #Habilitar sólo para depurar
            resultado.lista_capi.append(capital)
            resultado.lista_inter.append(intereses)

            interesTotales = interesTotales + intereses
            capital = capital + intereses
            #print("Capital por pagar:",round(capital,0)) #Habilitar sólo para depurar
            capital = capital - cuota
            if capital < 0:
                break
        capitalTotal = capitalTotal + interesTotales
        proporcionIntereses = (interesTotales/monto)*100 #Porcentaje de los intereses con respecto al monto del préstamo
        resultado.capitalTotal = capitalTotal
        resultado.interesesTotales = interesTotales
        resultado.proporcion = proporcionIntereses

        return resultado


    