from .CalcFiguras import figura_2D

class triangulo(figura_2D):

    def __init__(self,base=1,altura=1):
        super().__init__(base,altura)
        self.base = base
        self.altura = altura

    def area(self):
        area = self.base*self.altura/2
        print("el area del triángulo es {}".format(area))