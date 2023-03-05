
class canción:
    def __init__(self,nombre,género,autor,letra):
        self.nombre = nombre
        self.género = género
        self.autor = autor
        self.letra = letra

    def __str__(self):

        a = "Nombre:{}\n".format(self.nombre)
        b = "Género:{}\n".format(self.género)
        c = "Autor:{}\n".format(self.autor)

        return a+b+c

c1 = canción("Yo soy de otra clase","Rap","Peminen","Lo siento, pero to no heredo de cualquier clase")
canciones = [c1]

def acceder_canciones():
    return canciones

