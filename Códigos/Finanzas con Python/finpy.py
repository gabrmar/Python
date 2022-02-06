#Interés Compuesto
import math

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
        print("Por favor aumentar el valor de la cuota para poder pagar este crédito con la tasa de interés actual")
    else:
        capital = monto #Capital adeudado 
        capitalTotal = monto
        while capital > 0:
            intereses = capital*(tasa_interes/100)
            #print("Intereses:",round(intereses,0)) #Habilitar sólo para depurar
            capt.append(capital)
            inter.append(intereses)
            interesTotales = interesTotales + intereses
            capital = capital + intereses
            #print("Capital por pagar:",round(capital,0)) #Habilitar sólo para depurar
            capital = capital - cuota
            if capital < 0:
                break
        capitalTotal = capitalTotal + interesTotales
        proporcionIntereses = (interesTotales/monto)*100 #Porcentaje de los intereses con respecto al monto del préstamo

        out = {"Intereses Pagados":interesTotales, "Capital Pagado":capitalTotal, "Porcentaje de intereses":proporcionIntereses}


    return out