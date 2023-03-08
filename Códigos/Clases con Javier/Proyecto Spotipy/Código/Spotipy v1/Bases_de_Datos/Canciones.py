
class canción:
    def __init__(self,nombre,género,autor,letra):
        self.nombre = nombre
        self.género = género
        self.autor = autor
        self.letra = letra

    def __str__(self):

        nombre = "Nombre:{}\n".format(self.nombre)
        género = "Género:{}\n".format(self.género)
        autor = "Autor:{}\n".format(self.autor)

        return nombre+género+autor

c1 = canción("Yo soy de otra clase","Rap","Peminen","Lo siento, pero to no heredo de cualquier clase")
c2 = canción("POO","Pop","JD Sensei","POO es otra onda.")
c3 = canción("El polimorfo","Ranchera","Alejandro el Magic Dunder","No confíes en él, cambia de forma según convenga")
canciones = [c1,c2,c3]

def acceder_canciones():
    return canciones

