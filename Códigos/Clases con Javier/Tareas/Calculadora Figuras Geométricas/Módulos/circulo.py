from .CalcFiguras import figura_2D
import math

class circulo():

    def __init__(self,radio=1):
        self.radio = radio

    def area(self):
        area = math.pi*math.pow(self.radio,2)
        print("el area del circulo es {}".format(area))
