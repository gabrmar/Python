"""
Los métodos mágicos son funciones que permiten realizar proceosos que que están fuera
de alcance por medio de los métodos regulares. Son conocidos por tener su nombre entre
guiones bajos dobles (underscores o dunders). El método mágino __init__ es el usado para la definicón
de los atributos de la clase.
"""
import random

#Método mágico __add__ #suma atrbitos numérricos equivalentes entre dos objetos de la misma clase 
class Vector2D:
  def __init__(self, x, y):  #definición de atributos
    self.x = x # componente x
    self.y = y # componente y
  def __add__(self, other): #el argumento other inidica que se usarán atributos pertenencientes
      #a un objeto diferente al que estamos definiendo (diferente al objeto self)
    return Vector2D(self.x + other.x, self.y + other.y)
    #se enrtrega un objeto Vector2D que tiene por componentes la suma de los componentes correspondientes
    #A cada tipo
"""
Muchos de los métodos mágicos tienen la función de definir cómo usar operadores matemáticos con los objetos
creados por el programador. __Add__ define cómo será la suma para objetos de la clase Vector2D, pero si se necesita
otro tipo de relación entre los atributos a sumar, se puede alcanzar sólo modificando el código. esto aplica
para todos los operadores matemáticos que tenga un método mágico asociado. Darle nuevas funciones a los operadores
matemáticos se le conoce como sobrecarga de operadores.
"""

class SpecialString:
  def __init__(self, cont):
    self.cont = cont

  def __truediv__(self, other): # Definiendo cómo será la división de 2 strings
    line = "=" * len(other.cont) # multiplicando el caracter según el tamaño del caracter del otro obejto
    return "\n".join([self.cont, line, other.cont]) # uniendo los Strings por medio de inicios de línea

  def __gt__(self, other): # defniendo la relación entre objetos ante el símbolo mayor que
    for index in range(len(other.cont)+1):
      result = other.cont[:index] + ">" + self.cont
      result += ">" + other.cont[index:] 
      print(result)

"""
Se puede definir por medio de la sobrecarga de operadores si los objetos pueden se indexables, iterables
y hasta suceptubles a funciones de variables string, teniendo la libertad de redefinir las operaciones
de estas funciones predefinidas según la necesidad.
"""

class VagueList:
  def __init__(self, cont):
    self.cont = cont

  def __getitem__(self, index):
    return self.cont[index + random.randint(-1, 1)] #alterando indexación por medio de número al azar

  def __len__(self):
    return random.randint(0, len(self.cont)*2) #Alterando el cálculo del tamaño de la lista por mediio
    # de un número al azar

"""
Además de los métodos como instancias(funciones), es posible usarlos como una clase dentro de la clase, lo cual
se conoce como método de clase. Éste método es capaz de crear una clase especial dentro de la clase la cual
automáticamente hereda todos atributos y métodos de la clase principal. Es bastante similar a realizar herencias
de una súperclase a una subclase, pero de una forma más práctica al no tener que  programar la creación de una nueva clase;
basta con definir el método de clase como si fuera un método más y cómo este genera un objeto del mismo tipo de clase
que la clase orginial.

Los métodos de clase se identifican porque se les marca con decoradores (se puede decir que los métodos de clases son
decordores).
"""

class rectángulo:
    def __init__(self,largo,ancho):
        self.largo = largo
        self.ancho = ancho

    def área(self):
        return self.largo * self.ancho

    @classmethod #decorador de métdodo de clase 
    def cuadrado(cls,lado): #creando la clase cuadrado de un sólo atributo: lado
        #Nótese que no se usa la declaración self sino cls
        return cls(lado,lado) #se regresa el objeto de la clase cuadrado y cómo sus parámeteros
        #encanjan con los atributos de la clase rectángulo

class Pizza:
  def __init__(self, toppings):
    self.toppings = toppings

  @staticmethod #Decorador de métodos estáticos
  def validate_topping(topping): #los métodos estáticos son métodos de clases que trabajan con los mismos argumentos que su clase padre
    if topping == "pineapple":
      raise ValueError("No pineapples!")
    else:
      return True

 

vector1 = Vector2D(5, 7)
vector2 = Vector2D(3, 9)
resultante = vector1 + vector2
print(resultante.x)
print(resultante.y)

spam = SpecialString("spam")
hello = SpecialString("Hello world!")
print(spam / hello)
eggs = SpecialString("eggs")
spam > eggs

vague_list = VagueList(["A", "B", "C", "D", "E"])
print(len(vague_list))
print(len(vague_list))
print(vague_list[2])
print(vague_list[2])

figura = rectángulo.cuadrado(10)
print(figura.área())


ingredients = ["cheese", "onions", "spam"]
if all(Pizza.validate_topping(i) for i in ingredients):
    pizza = Pizza(ingredients)





