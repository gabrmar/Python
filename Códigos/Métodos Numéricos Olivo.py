# Función = x + 5 = 10
# Valor inicial Xa

Y = 10 # Valor a alcanzar
Xa = 0 # Valor inicial
Yc = 0 # Resultado de la iteración
while Yc != Y :
    Yc = Xa + 5
    if Yc > Y:
        Xa = Xa - 1
    if Yc < Y:
        Xa = Xa + 1
print(f"La solución a la ecuación x + 5 = 10 es {Xa}")




