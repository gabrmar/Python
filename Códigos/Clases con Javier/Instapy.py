import random

locations = [
    'Barranquilla, Colombia',
    'Bogotá, Colombia',
    'Miami, USA',
    'Disney World, Orlando',
    'Cabo Cañaveral, Orlando',
    'Ciudad de Panamá, Panamá',
    'Tokyo, Japón',
]
class FeedPost:
    image = None
    description = "hola"
    location = None
    likes = 0
    comments = []
    tags = None
    filters = None

    def get_location(self):
        location = random.sample(locations,1)
        print("llamado por {}".format(self))

        return location

    def show_comments(self):
        if self.comments: #Esto es lo mismo que if self.comments == True, es decir si hay contenido dentro de la lista comments
            return self.comments
        else:
            return "Esta publicación no tiene comentarios"

