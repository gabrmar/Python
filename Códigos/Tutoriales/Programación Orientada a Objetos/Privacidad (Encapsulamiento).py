"""
Privacidad en Python

La mayoría de lenguajes de programación soportan variables públicas y privadas para definit que tipos de datos en las instancias de clases
pueden ser accedidos y modificados por los usuarios, sin embargo Python no es así, es decir que la privacidad tal cual como se conoce en
otro lenguajes no existe en Python, pero existen ciertas restricciones que se le pueden colocar a las variables para tener cierto nivel
de privacidad. Uno de los aspectos a tener en cuenta es la notación aceptada en Python para hacer saber a los programadores qué tipos de datos
deberían ser tratados con privacidad el cual consiste en el uso de guiones bajos sencillos y dobles. Esto combinado con técnicas de programación
para dar control de acceso se establece el nivel de privacidad que se necesite dependiendo de los requerimientos que el código debe cumplir.

"""
   


class year_graduated: # Clase año graduado 
   def __init__(self, year=32): # Se define un año por defecto de valor 32
      self._year = year # Definiendo un atributo con un guión bajo para indicar la privacidad de este valor

   # Función getter
   def get_year(self):
      return self.__year # Al retornar una variable que no existe (Nunca se ha definido una variable con doble guión bajo hasta ahora) se va a
      # generar un error de atributo porque tal valor no existe.

   # Función setter
   def set_year(self, a):
      self.__year = a # Cambiar el valor de la variable oculta de año

grad_obj = year_graduated() # Definiendo una instancia de la clase año graduado
print(grad_obj._year) # Imprimiendo la variable de año 

# Si quitas el comentario de la línea de abajo, se va a generar un error de atributo porque no existe la variable __year hasta ahora. El uso
# de los guiones simples y dobles como notación de privacidad es algo que sólo se usa en Python.
#print(grad_obj.get_year()) # Invoncando función getter para pedir el año

# ***After using setter***
grad_obj.set_year(2019) # Invocando función setter para cambiar el valor del año
print(grad_obj._year) # Imprimmir el valor del año. Seguirá imprimiendo el valor incial del año porque el setter guarda su valor en otra 
# Variable diferente de _year (un guión), es decir __year (doble guión).

"""
Para más información, aquí están los siguientes enlaces 

1) https://www.tutorialspoint.com/getter-and-setter-in-python

2) https://www.tutorialspoint.com/How-data-hiding-works-in-Python-Classes


"""