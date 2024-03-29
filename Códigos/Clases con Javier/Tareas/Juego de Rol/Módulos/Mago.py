from .Personaje import Personaje
import random

rango = range(1,11)  #Como hacer esto en una sola línea?
niveles = []
for i in rango:
    niveles.append(i)


class Mago(Personaje):

    def __init__(self,nombre,experiencia=0,mana=5,**kwargs):
        super().__init__(nombre,experiencia,**kwargs) #Usando función super para poder usar el __init__ de la superclase y la clase hija al mismo tiempo
        self.nombre = nombre
        self.experiencia = experiencia
        self.mana = mana
        self.sanacion = True
        self.inteligencia = True

        
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
