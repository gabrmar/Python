# Herencia de clases

# Primer objeto 
class Rectangle: # Definiendo clase rectángulo
    def __init__(self, length, width): # la clase rectángulo necesita un largo y un ancho para ser definido
        self.length = length
        self.width = width

    def area(self): # Método para cálculo de área 
        return self.length * self.width

    def perimeter(self): # Método para cálculo de perímetro 
        return 2 * self.length + 2 * self.width

# Definiendo claae cuadrado que hereda de la clase rectángulo
class Square(Rectangle): # la sintaxis es class clase hija (super clase):
    def __init__(self, length): # la clase cuadrado sólo necesita definir un valor de longitud para ser usado
        super().__init__(length, length)  # Usando el método super() para definir cómo el parámetro de la longitud del cuadrado
        # encaja en la definción inicial del rectángulo. Eso es necesario para que los métodos de la clase rectángulo puedan ser
        # ser usados por la clase cuadrado.

# Ejemplo 2

class gato: #creando clase gato
    #raza = "gato quillero" # No recuerdo el porqué de esta línea
    def __init__(self,color,nombre,dieta = "Atún"): #la función/método __init__ es  
        raza = "gato quillero" 
        # el connstructor de clase. Es el encargado de definir
        # los atributos de la clase (las variables que estarán
        # (asociadas a este objeto).
        # es necesario colocar como primer argumento la declaración self
        # para el caso de la dieta, se está definiendo un valor por defecto en caso de que el usuario no lo especifique.
        self.color = color #self asocia las variables a la clase
        self.nombre = nombre
        self.dieta = dieta
        self._raza = raza # Indicando por convención por medio del guión bajo que la raza es una variable privada la cual el usuario
        # no conoce ni va a interactuar con ella.
        self._edad = None # El None es el indicador de que la varialble no tiene un valor definido. es como el Null en Java. En este caso
        # se está efiniendo una variable privdad que se usará para el manejo de la edad del gato.

    def maullar(self):
        print(f"{self.nombre} usó maullar: miau!")

class gatico(gato): #la clase entre paréntesis se vuelve la super clase
    # de la clase gatico y hereda sus atributos y funciones a la clase
    # que se está creando. La clase gatico se vuelve una subclase de
    # la clase gato

    def esconder(self): # No olvides colocar el self cada vez que definas una función dentro de una clase
        print("el gatico {a} se ha escondido".format(a = self.nombre))
        # se puede ver que pide el atributo nombre sin haberlo definido
        # en la clase gatico, sino que lo saca de la superclase gato
    def maullar(self):
        print("{x} usó maullar: miauuuuu!".format(x= self.nombre))
        #Definir un métodoya había sido definido en la herencia
        #hace que este sea sobrescrito
        super().maullar() # la función super permite llamar métodos
        # de la super clase(ahora este método realiza el maullar
        # con el mensaje de la subclase y luego con el mensaje
        # de la superclase)

Rec = Rectangle(5,2) # Definiendo objeto tipo rectángulo con largo 5 y ancho 2 
cuadra = Square(4) # Definiendo objeto tipo cuadrádo con arísta de valor 4
print(Rec.area()) # Mostrando el valor del área del rectángulo
print(Rec.perimeter()) # Mostrando el valor del perímetro del rectángulo
print(f"Area:{cuadra.area()} Perímetro:{cuadra.perimeter()}") # Mostrando tanto área como perímetro del cuadrado
felix_jr = gatico("rojo","felix JR.") # Creando objeto tipo gatico definiendo su color y nombre
felix_jr.esconder() # Acción de esconder
felix_jr.maullar()  # Acción de maullar 

"""
Link: https://realpython.com/python-super/

"""