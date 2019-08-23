def Esbisiesto(año):
        if año % 4 == 0:
           if año % 100 == 0:
                if año % 400 == 0:
                        print("Es bisiesto")
                else:
                        print("No es bisiesto 1")
        else:
                print("No es bisiesto 2")
        
                
Esbisiesto(2000)
