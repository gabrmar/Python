import random

rango = range(80,120)  #Como hacer esto en una sola línea?
pesos = []
for i in rango:
    pesos.append(i)

class formula_1:
    
    def __init__(self,kilometraje,nivel_gasolina=10,peso=None,**kwargs):
        self.kilometraje = kilometraje
        self.nivel_gasolina = nivel_gasolina
        self.peso = peso

        for atributo,valor in kwargs.items():
            setattr(self,atributo,valor)

    def medir_gasolina(self):
        if self.nivel_gasolina < 2:
            print("Gasolina baja Llenar el tanque lo más pronto posible.")
        else:
            print("Gasolina: {}".format(self.nivel_gasolina))

    def pesar(self):
        self.peso = random.sample(pesos,1)[0]
