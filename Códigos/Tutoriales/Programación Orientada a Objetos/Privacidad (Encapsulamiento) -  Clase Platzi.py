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
Empezar comentarios por acá

"""
class CasillaDeVotación:

   def __int__(self, identificador, pais):
      self._identificador = identificador
      self._pais = pais
      self._region = None

   @property
   def region(self):
      return self._region

   @property.setter
   def set_region(self, region):
      if region in self._pais:
         self._region = region
      else:
         raise ValueError(f"la región {region} no está en la lista")

casilla = CasillaDeVotación(123, ["Colombia", "Argentina"])
print(casilla.region)
casilla.region = "Cundinimarca"
print(casilla.region)  


"""
Para más información, aquí está este enlace: 

Privacidad: https://www.tutorialspoint.com/How-data-hiding-works-in-Python-Classes

Setters and Getters: https://www.geeksforgeeks.org/getter-and-setter-in-python/
"""