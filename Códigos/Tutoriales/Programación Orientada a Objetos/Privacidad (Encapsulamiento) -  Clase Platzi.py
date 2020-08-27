"""
Privacidad en Python

La mayoría de lenguajes de programación soportan variables públicas y privadas para definit que tipos de datos en las instancias de clases
pueden ser accedidos y modificados por los usuarios, sin embargo Python no es así, es decir que la privacidad tal cual como se conoce en
otro lenguajes no existe en Python, pero existen ciertas restricciones que se le pueden colocar a las variables para tener cierto nivel
de privacidad. Uno de los aspectos a tener en cuenta es la notación aceptada en Python para hacer saber a los programadores qué tipos de datos
deberían ser tratados con privacidad el cual consiste en el uso de guiones bajos sencillos y dobles. Esto combinado con técnicas de programación
para dar control de acceso se establece el nivel de privacidad que se necesite dependiendo de los requerimientos que el código debe cumplir.

"""


class CasillaDeVotación: # Creación de clase Casilla de votación

   def __init__(self, identificador, pais): # Se define una variable para indentificador de la casilla y para definir el país (una lista) .
      self._identificador = identificador # Notación de un guión bajo para indicar privacidad
      self._pais = pais 
      self._region = None # El None en Python signinfica nada. Es una palabra para indicar que la variable no tiene ningún valor definido
      # por ahora.

   @property # Decorador de la función propiedad (Más información en los enlacess)
   def region(self): # Función getter región 
      return self._region # Regresar valor privado de la región

   @region.setter # Definción de la función setter de region para la función propiedad
   def region(self, region): # Función setter región
      if region in self._pais: # Sección de control para validar que el nuevo país que se quiere agregar hace parte de la lista de países 
         self._region = region # permitidos
      else:
         raise ValueError(f"la región {region} no está en la lista") # Activar excepxión  de error de valor

casilla = CasillaDeVotación(123, ["Colombia", "Argentina"])
print(casilla.region) # por medio de la función propiedad ahora se puede usar notación de punto (objeto.atributo) para obtener y modificar
# los valores de cada una de las propiedades del objeto.
casilla.region = "Colombia"  # Si se coloca un país diferente a los que están en la lista, entonces se genera un error de valor (ValueError)
print(casilla.region)  


"""
Para más información, aquí está este enlace: 

Privacidad: https://www.tutorialspoint.com/How-data-hiding-works-in-Python-Classes

Setters and Getters: https://www.geeksforgeeks.org/getter-and-setter-in-python/
"""