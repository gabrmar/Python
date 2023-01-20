import math


class figura_2D:
    def __init__(self,a,b):
        figura_2D.a = a
        figura_2D.b = b

class circulo():

    def __init__(self,radio=1):
        self.radio = radio

    def area(self):
        area = math.pi*math.pow(self.radio,2)
        print("el area del circulo es {}".format(area))

class triangulo(figura_2D):

    def __init__(self,base=1,altura=1):
        super().__init__(base,altura)
        self.base = base
        self.altura = altura

    def area(self):
        area = self.base*self.altura/2
        print("el area del triángulo es {}".format(area))
        

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