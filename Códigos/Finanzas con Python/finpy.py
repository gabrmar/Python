#Interés Compuesto
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

    intereses = monto*(tasa_interes/100)
    if intereses >= cuota: #Si el pago no logra cubrir los intereses, entonces nunca se podrá pagar la deuda
        return "Por favor aumentar el valor de la cuota para poder pagar este crédito con la tasa de interés actual"
    else:
        resultado = analisis()
        capital = monto #Capital adeudado 
        resultado.capitalTotal = monto
        while capital > 0:
            intereses = capital*(tasa_interes/100)
            #print("Intereses:",round(intereses,0)) #Habilitar sólo para depurar
            resultado.lista_capi.append(capital)
            resultado.lista_inter.append(intereses)

            resultado.interesesTotales = resultado.interesesTotales + intereses
            capital = capital + intereses
            #print("Capital por pagar:",round(capital,0)) #Habilitar sólo para depurar
            capital = capital - cuota
            if capital < 0:
                break
        resultado.capitalTotal = resultado.capitalTotal + resultado.interesesTotales
        proporcionIntereses = (resultado.interesesTotales/monto)*100 #Porcentaje de los intereses con respecto al monto del préstamo
        resultado.proporcion = proporcionIntereses

        return resultado

def formato(numero, moneda="COP"):

    numero = int(numero)
    check = isinstance(numero,int)
    if check == True:
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
    else:
        print("Número flotante no detectado")
        salida = 0

    return salida
    