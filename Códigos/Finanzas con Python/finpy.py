#Interés Compuesto
import math

class analisis:

    def __init__(self,capitalTotal = -1,interesesTotales = -1,proporcion = -1,lista_capi = [],lista_inter = []):
        self.capitalTotal = capitalTotal
        self.interesesTotales = interesesTotales
        self.proporcion = proporcion
        self.lista_capi = lista_capi
        self.lista_inter = lista_inter



#--- Rutina de análisis de interés compuesto ----
def icompuesto(tasa_interes,cuota,monto):
    proporcionIntereses = -1

    intereses = monto*(tasa_interes/100) #Intereses generados en un periodo de pago
    if intereses >= cuota: #Si el pago no logra cubrir los intereses, entonces nunca se podrá pagar la deuda
        return "Por favor aumentar el valor de la cuota para poder pagar este crédito con la tasa de interés actual"
    else:
        resultado = analisis() #Creación de instancia  de tipo análisis
        capital = monto #Este cambio de variables es sólo para reafirmar que la variable monto tiene el capital que se debe
        resultado.capitalTotal = capital
        while capital > 0:
            intereses = capital*(tasa_interes/100) #Cálculo de intereses generados
            #---- Guardando resultados en listas ---
            resultado.lista_capi.append(capital)
            resultado.lista_inter.append(intereses)
            resultado.interesesTotales = resultado.interesesTotales + intereses
            capital = capital + intereses
            capital = capital - cuota
            if capital <= 0:
                break
        #--- Guardando resultados del préstamo --- 
        resultado.capitalTotal = resultado.capitalTotal + resultado.interesesTotales
        proporcionIntereses = (resultado.interesesTotales/monto)*100 #Porcentaje de los intereses con respecto al monto del préstamo
        resultado.proporcion = proporcionIntereses

        return resultado
        
#--- Rutina de formateo de números a valor de una divisa ---
def formato(numero, moneda="COP"):

    numero = int(numero) #Elimiando crifras decimales
    numero = str(numero)
    l = len(numero)
    aux = ""
    aux2 = -1
    contador = 0
    if l > 3:
        punto = True
        reversa = numero[::-1]
        for i in reversa:
            aux = aux + i
            contador = contador + 1
            aux2 = aux2 + 1
            if contador == 3 and punto == True and aux2 != len(reversa) - 1:
                aux = aux + "."
                contador = 0
                if len(reversa[aux2:]) <= 3: 
                    punto = False
        salida = "$ " + aux[::-1]
    else:
        salida = "$ " + numero

    return salida
    