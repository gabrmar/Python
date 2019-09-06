def Esbisiesto(año):
        if año % 4 == 0:
           if año % 100 == 0:
                if año % 400 == 0:
                       ans = True
                else:
                        ans = False
        else:
                ans = False
        return ans
        
                
ans = Esbisiesto(2000)
print(ans)
