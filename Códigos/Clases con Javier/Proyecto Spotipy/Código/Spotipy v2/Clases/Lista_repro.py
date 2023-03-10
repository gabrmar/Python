from Clases.Canciones import canción

class lista_reproducción:
    def __init__(self,nombre):
        self.nombre = nombre
        self.fila = []
        
    def añadir_a_lista(self,canción,nombre_lista):
        self.fila.append(canción)
        print("Canción añadida a la lista {}".format(self.nombre))

