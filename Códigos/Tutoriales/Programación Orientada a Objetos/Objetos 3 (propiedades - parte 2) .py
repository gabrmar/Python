# Continuación de propiedades

"""
Se pueden decorar métodos como propiedades para poder definir el tipo de acceso a los atributos. +++Modificar+++

  @property
  def pineapple_allowed(self):
    return False

"""
     
class Pizza:
  def __init__(self, toppings):
    self.toppings = toppings
    self._pineapple_allowed = False

  @property
  def pineapple_allowed(self):
    return self._pineapple_allowed

  @pineapple_allowed.setter
  def pineapple_allowed(self, value):
    if value:
      password = input("Enter the password: ")
      if password == "Sw0rdf1sh!":
        self._pineapple_allowed = value
      else:
        raise ValueError("Alert! Intruder!")

"""
+++Modificar++++

pizza = Pizza(["cheese", "tomato"])
print(pizza.pineapple_allowed)
#pizza.pineapple_allowed = True # si habilitas la  línea, se tendrá un error de atributo
#al tratar de modificar un atributo que ha sido decorado como propiedad
"""



pizza = Pizza(["cheese", "tomato"])
print(pizza.pineapple_allowed)
pizza.pineapple_allowed = True
print(pizza.pineapple_allowed)
