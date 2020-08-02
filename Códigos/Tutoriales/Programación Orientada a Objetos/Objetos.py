#Clases en  python
# OOP (programación orientada a objetos)

class gato: #creando el objeto/clase gato
    especie = "gato quillero" #este espacio es para los atributos de clase
    #se pueden ver como variables globales dentro de la clase
    def __init__(self,color,piernas,nombre,dieta = "Atún"): #la función/método __init__ es  
        # el connstructor de clase. Es el encargado de definir
        # los atributos de la clase (las variables que estarán
        # (asociadas a este objeto).
        # es necesario colocar como primer argumento la declaración self
        # para el caso de la dieta, se está definiendo un valor por defecto en caso de que el usuario no lo especifique.
        self.color = color #self asocia las variables a la clase
        self.piernas = piernas
        self.nombre = nombre
        self.dieta = dieta
        self._raza = "Gato persa" # Indicando por convención por medio del guión bajo que la raza es una variable privada la cual el usuario
        # no conoce ni va a interactuar con ella.
        self._edad = None # El None es el indicador de que la varialble no tiene un valor definido. es como el Null en Java. En este caso
        # se está efiniendo una variable privdad que se usará para el manejo de la edad del gato.


    def maullar(self):
        print("{x} usó maullar: miau!".format(x= self.nombre))

class gatico(gato): #la clase entre paréntesis se vuelve la superclase
    # de la clase gatico y hereda sus atributos y funciones a la clase
    # que se está creando. La clase gatico se vuelve una subclase de
    # la clase gato

    def esconder(self): # No olvides colocar el self
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
    
class métodos: #Se pueden crear clases sin atributos. Sólo con métodos
    def saludo(self):
        print("hola")
    def halago(self):
        print("un gusto conocerlo")
    def despedida(self):
        print("hasta pronto")



felix = gato("rojo",4, "Felix")
felix_jr = gatico("rojo",4,"felix JR.")
print(felix.color)  
print(felix.piernas)
felix.maullar() 
print("La especie de {g} es {e}".format(g = felix.nombre,e = felix.especie))
#print(felix.edad)# este atributo no ha sido definido, por eso habilitarlo
# genera un error de atributo
felix_jr.esconder()
felix_jr.maullar()

persona = métodos() #Variable persona recibe los métodos de la clase métodos
persona.saludo()
persona.halago()
persona.despedida()
Prueba = isinstance(felix,gato) # función que sirve para probar si un objeto pertenence a una clase en específico
print(Prueba)

