# Propiedades en objetos de Python - Encapsulamiento

"""
Privacidad en Python

La mayoría de lenguajes de programación soportan variables públicas y privadas para definit que tipos de datos en las instancias de clases
pueden ser accedidos y modificados por los usuarios, sin embargo Python no es así, es decir que la privacidad tal cual como se conoce en
otro lenguajes no existe en Python, pero existen ciertas restricciones que se le pueden colocar a las variables para tener cierto nivel
de privacidad. Uno de los aspectos a tener en cuenta es la notación aceptada en Python para hacer saber a los programadores qué tipos de datos
deberían ser tratados con privacidad el cual consiste en el uso de guiones bajos sencillos y dobles. Esto combinado con técnicas de programación
para dar control de acceso se establece el nivel de privacidad que se necesite dependiendo de los requerimientos que el código debe cumplir. 
"""

class Pizza:
  def __init__(self, toppings):
    self.toppings = toppings
    self._pineapple_allowed = False # un guión bajo da un nivel de privacidad.
    # este tipo de valores aparentemente no son importados. 


# Se pueden decorar métodos como propiedades para poder definir el tipo de acceso a los atributos. 
  @property
  def pineapple_allowed(self):
    return False # regresa falso indicando que esta la piña no es un ingrediente permitido.


pizza = Pizza(["cheese", "tomato"])
print(pizza.pineapple_allowed)
#pizza.pineapple_allowed = True # si habilitas la  línea, se tendrá un error de atributo
#al tratar de modificar un atributo que ha sido decorado como propiedad. La razón es la siguiente:

"""
el  decorador @property hace referencia a la función property() que recibe como primer parámetro
una fucnión getter, es decir que cuando trato de moidificarla al volverla verdaera, se genera un erorr
de atributo porque esa función no está diseñada para cambiar valores (setter) sino sólo para mostrarlos.

Más información: https://www.geeksforgeeks.org/getter-and-setter-in-python/

"""

