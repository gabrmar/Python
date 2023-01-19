class Personaje:
    def __init__(self,nombre,experiencia=5,**kwargs):
        self.nombre = nombre 
        self.experiencia = experiencia
        self.hp = 100
        

        for atributo,valor in kwargs.items():
            setattr(self,atributo,valor)

    def presentar(self):
        print("Hola, mi nombre es {}".format(self.nombre))

class Arquero:

    def __init__(self,nombre,experiencia=20,flechas=50,arco="Arco simple"):
        self.nombre = nombre
        self.experiencia = experiencia
        self.flechas = flechas
        self.arco = arco

    def disparar(self):
        print("flecha lanzada")
        self.flechas = self.flechas -1
        print("Quedan {} flechas disponibles".format(self.flechas))

    def apuntar(self):
        print("La precisón del arquero {} ha aumentado".format(self.nombre))

class Arquero_2(Personaje):

    def __init__(self,nombre,experiencia=20,flechas=50,arco="Arco simple"):
        self.nombre = nombre
        self.experiencia = experiencia
        self.flechas = flechas
        self.arco = arco

    def disparar(self):
        print("flecha lanzada")
        self.flechas = self.flechas -1
        print("Quedan {} flechas disponibles".format(self.flechas))

    def apuntar(self):
        print("La precisón del arquero {} ha aumentado".format(self.nombre))

class Arquero_3(Personaje):

    def __init__(self,nombre,experiencia=20,flechas=50,arco="Arco simple",**kwargs):
        super().__init__(nombre,experiencia,**kwargs)
        self.nombre = nombre
        self.experiencia = experiencia
        self.flechas = flechas
        self.arco = arco

        for atributo,valor in kwargs.items():
            setattr(self,atributo,valor)

    def disparar(self):
        print("flecha lanzada")
        self.flechas = self.flechas -1
        print("Quedan {} flechas disponibles".format(self.flechas))

    def apuntar(self):
        print("La precisón del arquero {} ha aumentado".format(self.nombre))


#------------------Main------------------------------

personaje = Personaje("Pablo",rol="test")
print(dir(personaje))
print(personaje.hp)
personaje.presentar()

robin = Arquero("Robin")
robin.disparar()
robin.apuntar()
print(dir(robin))

hipolita = Arquero_2("Hipolita")
hipolita.disparar()
hipolita.apuntar()
hipolita.presentar()
print(dir(hipolita))
#print(hipolita.hp) # el __init___ de la clase Arquero_2 sobreescribe el __init__ de la clase padre, por eso no hay un atributo de salud (hp)

hawkeye = Arquero_3("Hawakeye",200,100,"Arco de carbono reforzado",eslogan="Justo en el blanco")
hawkeye.disparar()
hawkeye.apuntar()
hawkeye.presentar()
print(hawkeye.hp)
print(hawkeye.eslogan)
