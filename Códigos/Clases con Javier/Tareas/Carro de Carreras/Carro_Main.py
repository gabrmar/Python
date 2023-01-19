from carro import formula_1,grua

caterpillar = grua(0)
ferrari = formula_1("Ferrari","200 Km/h","80 km/h^2","Llantas caras",0,modelo=2009,motor="gasolina",cilindros=12)
ferrari.medir_gasolina()
ferrari.nivel_gasolina = 1
ferrari.medir_gasolina()
print(ferrari.peso)
ferrari.pesar()
print(ferrari.peso)
print(dir(ferrari))
print(ferrari.aceleración)
caterpillar.medir_gasolina()
print(ferrari.peso)
caterpillar.remolcar_carro(ferrari.peso)
caterpillar.peso_carga = 100
caterpillar.remolcar_carro(ferrari.peso)



