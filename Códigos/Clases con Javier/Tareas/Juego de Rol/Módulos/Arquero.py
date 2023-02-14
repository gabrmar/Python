from .Personaje import Personaje

class Arquero(Personaje):

    def __init__(self,nombre,experiencia=20,flechas=50,arco="Arco simple",**kwargs):
        super().__init__(nombre,experiencia,**kwargs) #Usando función super para poder usar el __init__ de la superclase y la clase hija al mismo tiempo
        self.nombre = nombre
        self.experiencia = experiencia
        self.flechas = flechas
        self.arco = arco

    def disparar(self):
        print("flecha lanzada")
        self.flechas = self.flechas -1
        print("Quedan {} flechas disponibles".format(self.flechas))

    def apuntar(self):
        print("La precisón del arquero {} ha aumentado".format(self.nombre))
