from Clases.Canciones import canción

class listas_reproducción:
    def __init__(self):
        self.listas = {}

    def __str__(self):
        nombres_listas = []
        if self.listas == {}:
            return("No hay listas disponibles")
        else:
            for lista in self.listas:
                #Acá hay que imprimir cada una de las listas de reproducción
                for lista in self.listas.keys():
                    nombres_listas.append(lista)
                return nombres_listas

    def __len__(self):
        return len(self.listas)