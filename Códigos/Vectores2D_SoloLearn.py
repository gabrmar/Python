import math,time # Importing mathematics and time modules


def sumavec(f1,theta1,f2,theta2):
    try:
        #First vector components
        theta1 = math.radians(theta1)
        f1x = f1*math.cos(theta1)
        f1y = f1*math.sin(theta1)
        #print("Vector 1 components\nX:{x} Y:{y}".format(x = round(f1x,4),y = round(f1y,4)))
    
        #Second vector components
        theta2 = math.radians(theta2)
        f2x = f2*math.cos(theta2)
        f2y = f2*math.sin(theta2)
        #print("Vector 2 components\nX:{x} Y:{y}".format(x= round(f2x,4),y =round(f2y,4)))

        #Vector addition
        frx = f1x+f2x
        fry = f1y+f2y
        Fr = math.sqrt(math.pow(frx,2)+math.pow(fry,2))
        Fr = round(Fr,4) #Rounding the result to 4 figures 
        print('Resultant vector components\nX:{x}, Y:{y}'.format(x = round(frx,4), y = round(fry,4)))

        #Vector angle
        if frx != 0:
            angle = math.degrees(math.atan(abs(fry)/abs(frx)))  
            print('Resultant vector angle\nTeta:{x}'.format(x = round(angle,4)))
        if Fr != 0:     
            #When frx is greater than zero 
            if frx > 0:
                if fry < 0:
                    polar = 360 - angle #calculating angle using  absolute values of the components
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
            print('Vectors cancelled each other')
                
        
        if round(polar,4) == 360: #Rounding angles very close to  360 degrees and set it to zero degrees
            polar = 0
            
        print("Resulting vector\nMagnitude:{x} Polar Angle:{y}".format(x = round(Fr,4),y = round(polar,4)))
        
    except TypeError:
        print('Something goes wrong...')
        time.sleep(2) #Do nothhing for 2 seconds
        print('Variable type error')
    return

def ingresovalores():
    F1 = 'x'
    t1 = 'x'
    F2 = 'x'
    t2 = 'x'   
    #Inputting values
    print('Defining 2D vector number 1')
    while F1 == 'x' and t1 == 'x': 
        try:
            F1 =float(input('Magnitude:'))
            if F1 < 0:
                print('Something goes wrong...')
                time.sleep(2)
                raise ValueError #Rasing a Value Error when a negative number is input
            t1 =float(input('Angle:'))

        except ValueError: #Used for type errors (wrong type of variables)
            print('Something goes wrong...')
            time.sleep(2)
            print('Incorrect value for vector 1')
            F1 = 'x'
            t1 = 'x'
            print('Input the correct values for vector 1')

    print('Defining 2D vector number 2')
    while F2 == 'x' and t2 == 'x': 
        try:
            F2 =float(input('Magnitude:'))
            if F2 < 0:
                print('Something goes wrong...')
                time.sleep(2)
                raise ValueError #Rasing a Value Error when a negative number is input
            t2 =float(input('Angle:'))
            sumavec(F1,t1,F2,t2)
        except ValueError: #Used for type errors (wrong type of variables)
            print('Something goes wrong...')
            time.sleep(2)
            print('Incorrect value for vector 2')
            F2 = 'x'
            t2 = 'x'
            print('Input the correct values for vector 2')
    return



#Variables default values
    
ans = 's' #Default variable 'ans'  value
ingresovalores()
while 1:        
    ans = input('Would you like to sum other two vectors? Y/N ')
    ans = ans.lower() #Turning string to lower case
    if ans == 'n':
        print('Thanks for using the 2D vector adder')
        break
    elif ans == 'y':
        ingresovalores()
    else:
        print('Choose a valid option')

        



    
    

    
    
    

