#Clases en  python
# OOP (programación orientada a objetos)

class gato: #creando el objeto/clase gato
    especie = "gato quillero" #este espacio es para los atributos de clase
    #se pueden ver como variables globales dentro de la clase
    def __init__(self,color,piernas,nombre): #la función/método __init__ es 
        # el connstructor de clase. Es el encargado de definir
        # los atributos de la clase (las variables que estarán
        # (asociadas a este objeto).
        # es necesario colocar como primer argumento la declaración self
        self.color = color #self asocia las variables a la clase
        self.piernas = piernas
        self.nombre = nombre

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
#print(felix.edad)# este atributo noha sido definido, por eso habilitarlo
# genera un error de atributo
felix_jr.esconder()
felix_jr.maullar()

persona = métodos()
persona.saludo()
persona.halago()
persona.despedida()

