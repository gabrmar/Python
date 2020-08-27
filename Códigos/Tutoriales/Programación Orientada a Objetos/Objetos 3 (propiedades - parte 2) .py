# Continuación de propiedades

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
    self._pineapple_allowed = False # un guión bajo para un nivel de privacidad.

  @property # Definición de parámetros para la función propiedad
  def pineapple_allowed(self) #  Definición de función getter 
    return self._pineapple_allowed # Regresar la variable sobre la piña como ingrediente (verdadero o falso)

  @pineapple_allowed.setter # Deinfición de función setter para la función propiedad
  def pineapple_allowed(self, value): # Función setter
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
