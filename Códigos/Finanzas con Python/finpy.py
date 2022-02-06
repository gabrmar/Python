#Interés Compuesto
import math

def icompuesto(tasa_interes,cuota,monto):
    interesTotales = -1
    capitalTotal = -1
    proporcionIntereses = -1
     

    
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
            #print("Intereses:",round(intereses,0))
            interesTotales = interesTotales + intereses
            capital = capital + intereses
            #print("Capital a pagar:",round(capital,0))
            capital = capital - cuota
            if capital < 0:
                break
        capitalTotal = capitalTotal + interesTotales
        proporcionIntereses = (interesTotales/monto)*100 #Porcentaje de los intereses con respecto al monto del préstamo

    #print(f"Intereses Pagados:{round(interesTotales,0)} pesos")
    #print(f"Capital Pagado:{round(capitalTotal,0)} pesos")
    #print(f"Porcentaje de intereses:{round(proporcionIntereses,2)}%")

    return {"Intereses Pagados":interesTotales, "Capital Pagado":capitalTotal, "Porcentaje de intereses":proporcionIntereses}