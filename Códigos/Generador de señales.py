import math, os
A = 1
w = 1
ph = 0
csv = ""
n = 360
archivo = open("señal.txt","w")
for i in range(n):
    sin = A*math.sin(math.radians(w*i + ph))
    sin = round(sin,3)
    csv = csv + str(sin)
    if i < n-1:
        csv = csv + ","
print(csv)
archivo.write(csv)
archivo.close()
