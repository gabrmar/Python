
class canción:
    def __init__(self,nombre,género,autor,letra):
        self.nombre = nombre
        self.género = género
        self.autor = autor
        self.letra = letra

c1 = canción("Yo soy de otra clase","Rap","Peminen","Lo siento, pero to no heredo de cualquier clase")
canciones = [c1]

def acceder_canciones():
    return canciones

