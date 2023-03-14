from Clases.Canciones import canción

class lista_reproducción:
    def __init__(self,nombre):
        self.nombre = nombre
        self.fila = []
        
    def añadir_a_lista(self,canción,nombre_lista):
        self.fila.append(canción)
        print("Canción {nombre_canción} añadida a la lista {lista}".format(nombre_canción=canción.nombre,lista=nombre_lista))

