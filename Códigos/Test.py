lista = [1,2,34,4,1212]
l = len(lista)
print(l)
iterable = range(l-1)
print(iterable)
for i in range(len(lista)-1):
    if lista[i] == 1 or lista[i] == 34:
        del lista[i]
        print("Eliminando elemento")
    print("Index:",i,"Element",lista[i])
print(iterable)
print(lista)

