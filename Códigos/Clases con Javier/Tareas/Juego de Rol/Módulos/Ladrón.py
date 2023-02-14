from .Personaje import Personaje

class Ladron(Personaje):

    def __init__(self,nombre,experiencia=10,mana=0): # este __init__ será el constructor visible de cara al usuario, por ende el ladrón tendrá 10 de experiencia por defecto
        super().__init__(nombre,experiencia) #Usando función super para poder usar el __init__ de la superclase y la clase hija al mismo tiempo
        self.nombre = nombre
        self.experiencia = experiencia
        self.mana = mana

    def robar(self):
        print("Ladrón {} ha usado robar".format(self.nombre))
        self.mana = self.mana + 10
        print("Ha robado +10 de mana al oponente")