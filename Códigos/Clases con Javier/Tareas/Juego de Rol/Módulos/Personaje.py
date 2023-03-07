
class Personaje:
    def __init__(self,nombre,experiencia=5,**kwargs):
        self.nombre = nombre 
        self.experiencia = experiencia
        self.health_points = 100
        

        for atributo,valor in kwargs.items():
            setattr(self,atributo,valor)
            #Objeto: self
            #Nombre del atributo: el que esté definodo por el nombre del kwarg
            #Valor del atributo: el que esté definifo como el valor asociado al kwarg
