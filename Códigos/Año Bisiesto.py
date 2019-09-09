def Esbisiesto(año):
        ans = False
        # Resolver problema con el uso del condicional
        if isinstance(año,(int)):
                año = int(año)
                if año % 4 == 0:
                        if año % 100 == 0:
                                if año % 400 == 0:
                                        ans = True
                                        print("Hola")
                                else:
                                        ans = False
                                        print("hola2")
                else:
                        ans = False
                        print("Hola3")
        else:
                raise TypeError("Please add a valid year")
        return ans
        
                
X = Esbisiesto(2020)
print(X)
X = Esbisiesto(2024)
print(X)
X = Esbisiesto(2028)
print(X)
X = Esbisiesto(1956)
print(X)
X = Esbisiesto(1)
print(X)
X = Esbisiesto(501)
print(X)