from Clases.Canciones import canción

class listas_reproducción:
    def __init__(self):
        self.listas = {}

    def __str__(self):
        for lista in self.listas:
            #Acá hay que imprimir cada una de las listas de reproducción
            for lista in self.listas.keys():
                pass 

    def __len__(self):
        return len(self.listas)