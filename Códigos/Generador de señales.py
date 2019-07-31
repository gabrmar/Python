import math
import os
A = [1, 1]
f = [2, 2]
ph = [0, 0]
archivo = open("señal.txt", "w")


def señal_seno(A, f, ph, n):
    csv = ""
    w = 2*math.pi*f
    for i in range(n):
        sin = A*math.sin(math.radians(w*i + ph))
        sin = round(sin, 3)
        csv = csv + str(sin)
        if i < n-1:
            csv = csv + ","
    print(csv)
    archivo.write(csv)
    archivo.close()


def señal_seno_doble(A1, f1, ph1, A2, f2, ph2, n):
    csv = ""
    w1 = 2*math.pi*f1
    w2 = 2*math.pi*f2
    for i in range(n):
        sin = A1*math.sin(math.radians(w1*i + ph1)) + A2 * \
            math.sin(math.radians(w2*i + ph2))
        sin = round(sin, 3)
        csv = csv + str(sin)
        if i < n-1:
            csv = csv + ","
    print(csv)
    archivo.write(csv)
    archivo.close()


def generador_senoides(A, f, ph, n):
        if len(A) == len(f) and len(f) == len(ph):
                print("Parámetros validados")
                #wave = [0]
                for i in range(n):

        else:
                print("Parámetros incorrectos. Verificar número")


señal_seno(1,4,0,256)
#señal_seno_doble(3,3,0,-3,2,45,256)
