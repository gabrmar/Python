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
        return "El crédito no se puede pagar con los valores establecidos. Es recomendable incrementar la cuota mensual."
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
            capital = capital + intereses - cuota 
            if capital <= 0:
                break
        #--- Guardando resultados del préstamo --- 
        resultado.capitalTotal = resultado.capitalTotal + resultado.interesesTotales
        proporcionIntereses = (resultado.interesesTotales/monto)*100 #Porcentaje de los intereses con respecto al monto del préstamo
        resultado.proporcion = proporcionIntereses

        return resultado
        
#--- Rutina de formateo de números a valor de una divisa ---
def formato(numero):

    numero = int(numero) #Elimiando crifras decimales
    numero = str(numero) #Transformando números en string para poder contatenar puntos y el símbolo de la moneda
    l = len(numero)
    aux = "" #Auxiliar de la variable de salida
    aux2 = -1 #Auxiliar del contador de recorrido de la string numero
    contador = 0
    if l > 3: # Si el número no tiene más de tres cifras, entonces no se necesita colocar ningún punto
        punto = True
        reversa = numero[::-1] #Inversión del número
        for i in reversa:
            aux = aux + i
            contador = contador + 1
            aux2 = aux2 + 1
            #--- Cóndición para dejar de colocar puntos ---
            if contador == 3 and punto == True and aux2 != len(reversa) - 1:
                #Explicación:
                #Se debe colocar un punto cada 3 cifras (contador == 3)
                #Esto debe continuar mientras la variable punto se mantenga verdadera (punto == True)
                #No se deben colocar más puntos si faltan menos de 3 cifras para finalizar el recorrido (aux2 != len(reversa) - 1)
                aux = aux + "."
                contador = 0
                if len(reversa[aux2:]) <= 3: #Comprobando si luego de agregar el último punto de mil quedan 3 crifas o menos
                    punto = False
        salida = "$ " + aux[::-1] #Nueva reversa del número para obtenerlo en el orden deseado
    else:
        salida = "$ " + numero

    return salida
    
#--- Rutina de Exportación de Datos ---
def exportar(analisis): #
    #Redondeando listas a valores enteros
    i = 0
    aux = 0
    auxl = []
    meses = len(analisis.lista_capi)
    while i < len(analisis.lista_capi):
        aux = int(analisis.lista_capi[i]) #******Optimizar esta subrutina por medio otras subrutinas. Peso actual del archivo es 4.89 KB******
        auxl.append(aux)
        i = i + 1
    #Removiendo llaves de las listas
    aux = str(auxl)
    aux = aux[1:]
    lista1 = aux[:len(aux)-1]
    #--
    i = 0
    aux = 0
    auxl = []
    while i < len(analisis.lista_inter):
        aux = int(analisis.lista_inter[i])
        auxl.append(aux)
        i = i + 1
    aux = str(auxl)
    aux = aux[1:]
    lista2 = aux[:len(aux)-1]
    auxl = []
    print(range(1,meses))
    for i in range(1,meses+1):
        auxl.append(i)
    aux = str(auxl)
    aux = aux[1:]
    lista3 = aux[:len(aux)-1]
    #------Crear una lista de listas para cada cadena de mensajes

    exportable = {"Capital":lista1,"Intereses":lista2,"Meses":lista3}

    archivo = open("csv.txt","w")  
    for valores in exportable.values():
        archivo.write(valores)
        archivo.write("\n")
    archivo.close()

    archivo = open("Leyendas.txt","w") 
    archivo.write("Estos son las variables que representan cada una de las filas del archivo csv.txt:") 
    archivo.write("\n")
    for llaves in exportable.keys():
        archivo.write(llaves)
        archivo.write("\n")
    archivo.close()       

