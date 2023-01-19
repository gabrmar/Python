import random

rango = range(80,120)  #Como hacer esto en una sola línea?
pesos = []
for i in rango:
    pesos.append(i)

class carro:
    def __init__(self,marca,vel_max,aceleración,llantas):
        self.marca = marca
        self.vel_max = vel_max
        self.aceleración = aceleración
        self.llantas = llantas


class formula_1(carro):
    
    def __init__(self,marca,velo_max,acelera,tipo_llanta,kilometraje,nivel_gasolina=10,peso=None,**kwargs):
        super().__init__(marca,velo_max,acelera,tipo_llanta)
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

class grua:

    def __init__(self,kilometraje,nivel_gasolina=20,peso=None,peso_carga=20):
        self.kilometraje = kilometraje
        self.nivel_gasolina = nivel_gasolina
        self.peso = peso
        self.peso_carga = peso_carga

    def medir_gasolina(self):
        if self.nivel_gasolina < 2:
            print("Gasolina baja Llenar el tanque lo más pronto posible.")
        else:
            print("Gasolina: {}".format(self.nivel_gasolina))

    def remolcar_carro(self,peso_carro):
        if self.peso_carga >= peso_carro:
            print("remolcando carro")
        else:
            print("el carro pesa {}, demsaido pesado para ser remolcado por esta grúa".format(peso_carro))