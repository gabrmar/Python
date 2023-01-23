from Módulos.carro import formula_1,grua,carro_pruebas,safety_car

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

carro_academia = carro_pruebas("Nissan","60 km/h","10 km/h^2","Llantas convecionales","Centro de Enseñanza Los Carros son Objetos")
print(dir(carro_academia))
print(carro_academia.academia)

carro_apoyo = safety_car("Renault","100 km/h","50 km/h^2","Llantas caras","Monaco")
print(dir(carro_apoyo))
print(carro_apoyo.pista)