# Continuación de propiedades

"""
Recodar en todos los códigos de propiedades que no existen los valores privados como tal en Python de la misma manera que existen en otros
lenguajes de programación como Java.
"""
class Pizza:
  def __init__(self, toppings):
    self.toppings = toppings
    self._pineapple_allowed = False # un guión bajo para un nivel de privacidad.

  @property
  def pineapple_allowed(self):
    return self._pineapple_allowed

  @pineapple_allowed.setter
  def pineapple_allowed(self, value):
    if value: #  una forma corta de  if value == True
      password = input("Enter the password: ") # Contraseña para validación de estar ante un usuario con privilegios para cambiar esta valor
      if password == "cisco":
        self._pineapple_allowed = value
      else:
        raise ValueError("Alert! Intruder!")




pizza = Pizza(["cheese", "tomato"])
print(pizza.pineapple_allowed)
pizza.pineapple_allowed = True
print(pizza.pineapple_allowed)
