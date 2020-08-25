"""
Privacidad en Python

La mayoría de lenguajes de programación soportan variables públicas y privadas para definit que tipos de datos en las instancias de clases
pueden ser accedidos y modificados por los usuarios, sin embargo Python no es así, es decir que la privacidad tal cual como se conoce en
otro lenguajes no existe en Python, pero existen ciertas restricciones que se le pueden colocar a las variables para tener cierto nivel
de privacidad. Uno de los aspectos a tener en cuenta es la notación aceptada en Python para hacer saber a los programadores qué tipos de datos
deberían ser tratados con privacidad el cual consiste en el uso de guiones bajos sencillos y dobles. Esto combinado con técnicas de programación
para dar control de acceso se establece el nivel de privacidad que se necesite dependiendo de los requerimientos que el código debe cumplir.

"""
"""
Continuar con los comentarios.
"""


class year_graduated: # Clase año graduado 
   def __init__(self, year=32):
      self._year = year

   # make the getter method
   def get_year(self):
      return self.__year

# make the setter method
def set_year(self, a):
    self.__year = a

grad_obj = year_graduated()
print(grad_obj._year)

# Before using setter
print(grad_obj.get_year())
#
# # After using setter
grad_obj.set_year(2019)
print(grad_obj._year)

"""
Para más información, aquí están los siguientes enlaces 

1) https://www.tutorialspoint.com/getter-and-setter-in-python

2) https://www.tutorialspoint.com/How-data-hiding-works-in-Python-Classes


"""