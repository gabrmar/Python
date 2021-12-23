binario = [1 ,0, 0, 1, 0, 0, 0, 1]
decimal = 0
bit = 7

for i in binario:
    if i == 1:
        decimal = decimal + pow(2,bit)
    bit = bit - 1
print(decimal)