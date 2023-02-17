from .carro import carro

class safety_car(carro):
    def __init__(self, marca, vel_max, aceleración, llantas,pista):
        super().__init__(marca, vel_max, aceleración, llantas)
        self.pista = pista