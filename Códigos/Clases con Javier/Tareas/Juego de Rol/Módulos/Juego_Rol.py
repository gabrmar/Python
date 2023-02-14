
class Personaje:
    def __init__(self,nombre,experiencia=5,**kwargs):
        self.nombre = nombre 
        self.experiencia = experiencia
        self.health_points = 100
        

        for atributo,valor in kwargs.items():
            setattr(self,atributo,valor)

"""class Mago(Personaje):

    def __init__(self,nombre,experiencia=0,mana=5,**kwargs):
        super().__init__(nombre,experiencia,**kwargs) #Usando función super para poder usar el __init__ de la superclase y la clase hija al mismo tiempo
        self.nombre = nombre
        self.experiencia = experiencia
        self.mana = mana
        self.sanacion = True
        self.inteligencia = True

        
    def recuperar_mana(self):
        if self.sanacion:
            valor = random.sample(niveles,1)[0] #[0] es necesario para poder obtener el elemento de la lista de random.sample
        else:
            valor = 0
        print("{} ha usado recuperación de Mana".format(self))
        print("+{}".format(str(valor))) 

    def pared_magica(self):
        if self.inteligencia and self.experiencia > 20:
            print("{} ha usado pared mágica:".format(self))
            print("01111100...Canalizando...|")
        else:
            print("{} no tiene los requisitos para usar pared mágica".format(self))

    def rafaga_de_plasma(self, mana):
        if self.mana >= mana and self.experiencia > 50:
            print("{} ha usado ráfaga de plasma".format(self))
            print()
            self.mana = self.mana - mana 
            print(".-*-._.-*-._.-.-*-._.-*-._.-\n")
        else:
            print("El mago no puede usar ráfaga de plasma todavía")
        """
class Ladron(Personaje):

    def __init__(self,nombre,experiencia=10,mana=0): # este __init__ será el constructor visible de cara al usuario, por ende el ladrón tendrá 10 de experiencia por defecto
        super().__init__(nombre,experiencia) #Usando función super para poder usar el __init__ de la superclase y la clase hija al mismo tiempo
        self.nombre = nombre
        self.experiencia = experiencia
        self.mana = mana

    def robar(self):
        print("Ladrón {} ha usado robar".format(self.nombre))
        self.mana = self.mana + 10
        print("Ha robado +10 de mana al oponente")

class Arquero(Personaje):

    def __init__(self,nombre,experiencia=20,flechas=50,arco="Arco simple",**kwargs):
        super().__init__(nombre,experiencia,**kwargs) #Usando función super para poder usar el __init__ de la superclase y la clase hija al mismo tiempo
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

    