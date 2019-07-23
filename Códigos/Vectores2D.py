import math,time # Importando librerias de  matematicas y de tiempo.


def sumavec(f1,theta1,f2,theta2):
    
    try:
        #componetes primer vector
        theta1 = math.radians(theta1)
        f1x = f1*math.cos(theta1)
        f1y = f1*math.sin(theta1)
        #print("Componentes de vector 1\nX:{x} Y:{y}".format(x = round(f1x,4),y = round(f1y,4)))
    
        #componentes segundo vector
        theta2 = math.radians(theta2)
        f2x = f2*math.cos(theta2)
        f2y = f2*math.sin(theta2)
        #print("Componentes de vector 2\nX:{x} Y:{y}".format(x= round(f2x,4),y =round(f2y,4)))

        #Suma de vectores
        frx = f1x+f2x
        fry = f1y+f2y
        Fr = math.sqrt(math.pow(frx,2)+math.pow(fry,2))
        Fr = round(Fr,4) #Redondeo de resultado a 4 cifras
        print('Componentes de vector resultante\nX:{x}, Y:{y}'.format(x = round(frx,4), y = round(fry,4)))

        #Ángulo del vector
        if frx != 0:
            angle = math.degrees(math.atan(abs(fry)/abs(frx)))  
            print('Ángulo de de vector resultante\nTeta:{x}'.format(x = round(angle,4)))
        if Fr != 0:     
            #Cuando frx es mayor que cero 
            if frx > 0:
                if fry < 0:
                    polar = 360 - angle #Calculando los ángulos con los valores absolutos de los componentes
                else:
                    polar = angle
            elif frx < 0:
                if fry < 0:
                    polar = 180 + angle
                else:
                    polar = 180 - angle
            else:
                if fry > 0:
                    polar = 90
                else:
                    polar = 270
        else:
            polar = 0.0
            print('Los vectores se cancelaron entre si')
                
        
        if round(polar,4) == 360: #Redondear ángulos cercanos a 360 y transformarlos a ángulos de 0 grados
            polar = 0
            
        print("vector resultante\nMagnitud:{x} Ángulo polar:{y}".format(x = round(Fr,4),y = round(polar,4)))
        
    except TypeError:
        print('Algo va mal...')
        time.sleep(2) #Tiemp sin hacer nada por 2 segundos
        print('Error de tipo de variable')
    return

def ingresovalores():
    F1 = 'x'
    t1 = 'x'
    F2 = 'x'
    t2 = 'x'   
    #Ingresando valores
    print('Definiendo vector 2D número 1')
    while F1 == 'x' and t1 == 'x': 
        try:
            F1 =float(input('Magnitud:'))
            if F1 < 0:
                print('Algo va mal...')
                time.sleep(2)
                raise ValueError #llamando excepción de errorel error de valor  en caso de toparse con números negativos
            t1 =float(input('Ángulo:'))

        except ValueError: #Usado para errores de tipo( tipo de variable equivocado)
            print('Algo va mal...')
            time.sleep(2)
            print('Valor incorrecto en vector 1')
            F1 = 'x'
            t1 = 'x'
            print('Ingrese los valores correctos en el vector 1')

    print('Definiendo vector 2D número 2')
    while F2 == 'x' and t2 == 'x': 
        try:
            F2 =float(input('Magnitud:'))
            if F2 < 0:
                print('Algo va mal...')
                time.sleep(2)
                raise ValueError #llamando excepción  el error de valor  en caso de toparse con números negativos
            t2 =float(input('Ángulo:'))
            sumavec(F1,t1,F2,t2)
        except ValueError: #Usado para errores de tipo( tipo de variable equivocado)
            print('Algo va mal...')
            time.sleep(2)
            print('Valor incorrecto en vector 2')
            F2 = 'x'
            t2 = 'x'
            print('Ingrese los valores correctos en el vector 2')
    return



#Valores por defecto de las variables
    
ans = 's' #Valor de respuesta por defecto
ingresovalores()
while 1:        
    ans = input('¿Desea realizar otra suma? S/N ')
    ans = ans.lower() #Convirtiendo string a minúscula
    if ans == 'n':
        print('Gracias por usar el sumador de vecrtores 2D')
        break
    elif ans == 's':
        ingresovalores()
    else:
        print('Elija una opción válida')
#Agregar un intervalo de espera cuando elijan una opcion incorrecta
        



    
    

    
    
    

