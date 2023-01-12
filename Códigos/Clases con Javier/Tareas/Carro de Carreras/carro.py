class formula_1:
    kilometraje = 0
    nivel_gasolina = 10

    def medir_gasolina(self):
        if self.nivel_gasolina < 2:
            print("Gasolina baja Llenar el tanque lo más pronto posible.")
        else:
            print("Gasolina: {}".format(self.nivel_gasolina))
