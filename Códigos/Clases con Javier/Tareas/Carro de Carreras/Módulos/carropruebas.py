from .carro import carro

class carro_pruebas(carro):
    def __init__(self, marca, vel_max, aceleración, llantas,academia):
        super().__init__(marca, vel_max, aceleración, llantas)
        self.academia = academia