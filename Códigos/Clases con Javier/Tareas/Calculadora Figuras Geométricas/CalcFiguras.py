import math

class circulo:
    radio = 0

    def area(self):
        area = math.pi*math.pow(self.radio,2)
        print("el area del circulo es {}".format(area))

class triangulo:
    base = 0
    altura = 0

    def area(self):
        area = self.base*self.altura/2
        print("el area del triángulo es {}".format(area))
        

class rectangulo:
    lado1 = 0
    lado2 = 0

    def area(self):
        figura = "rectángulo"
        area = self.lado1*self.lado2
        if self.lado1 == self.lado2:
            figura = "cuadrado"

        print("el area del {fig} es {a}".format(fig=figura,a=area))