# Propiedades en objetos de Python - Encapsulamiento

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
el  decorador @property hace referencia a la función property() que recibe como priemer parámetro
una fucnión getter, es decir que cuando trato de moidificarla al volverla verdaera, se genera un erorr
de atributo porque esa función no está diseñada para cambiar valores (setter) sino sólo para mostrarlos.

Más información: https://www.geeksforgeeks.org/getter-and-setter-in-python/

"""

