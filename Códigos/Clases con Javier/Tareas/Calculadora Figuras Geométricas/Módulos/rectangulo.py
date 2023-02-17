from .CalcFiguras import figura_2D

class rectangulo(figura_2D):

    def __init__(self,lado1,lado2):
        super().__init__(lado1,lado2)
        self.lado1 = lado1
        self.lado2 = lado2

    def area(self):
        figura = "rectángulo"
        area = self.lado1*self.lado2
        if self.lado1 == self.lado2:
            figura = "cuadrado"

        print("el area del {fig} es {a}".format(fig=figura,a=area))