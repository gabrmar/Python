
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

