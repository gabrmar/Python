def Esbisiesto(año):
        if isinstance(año,(int,float)) == True:
                año = int(año)
                if año % 4 == 0:
                        if año % 100 == 0:
                                if año % 400 == 0:
                                        ans = True
                                else:
                                        ans = False
                        else:
                                ans = True
                else:
                        ans = False
        else:
                raise TypeError("Please add a valid year")
        return ans
        
                
X = Esbisiesto(1996)
print(X)
X = Esbisiesto(1997)
print(X)
X = Esbisiesto(1900)
print(X)
X = Esbisiesto(2000)
print(X)