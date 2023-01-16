import random

rango = range(1,11)  #Como hacer esto en una sola línea?
niveles = []
for i in rango:
    niveles.append(i)

class Mago:
    sanacion = True
    inteligencia = True
    experiencia = 20
    mana = 70

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

    def rafaga_de_plasma(self, mana):
        if self.mana >= mana and self.experiencia > 50:
            print("{} ha usado ráfaga de plasma".format(self))
            print()
            self.mana = self.mana - mana 
            print(".-*-._.-*-._.-.-*-._.-*-._.-\n")
        else:
            print("El mago no puede usar ráfaga de plasma todavía")
        
