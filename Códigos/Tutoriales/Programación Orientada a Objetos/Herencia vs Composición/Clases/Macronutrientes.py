
#Esta parte está para probar una herencia típica
#Revisar archivo de tutoriales sobre Herencia.py 
class macronutriente:

    def __init__(self,origen,peso): 
    
        self.origen = origen
        self.peso = peso 

    def __str__(self):
        origen = "Orígen:{}\n".format(self.origen)
        peso = "Peso:{}\n".format(self.peso)

        return origen+peso


class proteínas(macronutriente):

    def __init__(self,origen,peso):
        #El orígen puede ser vegetal o animal
        self.origen = origen
        self.peso = peso

class carbohidratos(macronutriente):

    def __init__(self,tipo,peso):
        #El tipo puede ser simple o complejo
        super().__init__(tipo,peso)
        self.tipo = tipo
        self.peso = peso

class grasas(macronutriente):

    def __init__(self,tipo,peso):
        super().__init__(tipo,peso)
        #El tipo de grasa puede ser saturada o insaturada
        self.tipo = tipo
        self.peso = peso

if __name__ == "__main__":

    grasa = grasas("vegetal",10)
    print(grasa)
    print(type(grasa))
    carbo = carbohidratos("simple",23)
    print(type(carbo))
    print(carbo)
    prote = proteínas("animal",10)
    print(type(prote))
    print(prote)
