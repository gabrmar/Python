import random

rango = range(1,11)
niveles = []
for i in rango:
    niveles.append(i)

class Mago:
    sanacion = True
    inteligencia = True
    experiencia = 20
    Mana = 70

    def recuperar_mana(self):
        if self.sanacion:
            valor = random.sample(niveles,1)[0] #[0] es necesario para poder obtener el elemento de la lista de random.sample
        else:
            valor = 0
        print("{} ha usado recuperación de Mana".format(self))
        print("+{}".format(str(valor))) 

    def pared_magica(self):
        if self.inteligencia and self.experiencia > 20:
            print("{} ha usado pared mágica:".format(self))
            print("01111100...Canalizando...|")
        else:
            print("{} no tiene los requisitos para usar pared mágica".format(self))
