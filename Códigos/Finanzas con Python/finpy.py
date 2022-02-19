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

    intereses = monto*(tasa_interes/100)
    if intereses > cuota:
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
    """Objetivo. Formatear números y listas a formato de moneda.
    
    Tareas:

    1. Definir si el parámetro recibdido es un valor único o una lista
    2. Proceder con el debido formateo según el tipo de variable
    
    """
    check = isinstance(numero,float)
    if check == True:
        numero = round(numero,0)
        numero = str(numero)
        l = len(numero)
        aux = ""
        if l > 3:
            #Creo que lo mejor es generar una nueva variable que recibe un elemento a la vez y cada 3 unidades
            #agregue un punto a la cadena ya que agregar los puntos dentro de la variable número puede ser complicado de
            #indexar dichos puntos debido a que el valor de la longitud de la variable cambiaría en cada iteración lo cual
            #puede haer más difdícil tener una idea clara de en qué posición colocar los puntos
            pass

        salida = "$ " + aux
    else:
        print("Número flotante no detectado")
        salida = 0

    return salida
    