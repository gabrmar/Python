import random 

locations = [ 
    "Barranquilla, Colombia",
    "Bogotá, Colombia",
    "Miami, USA",
    "Disney World, Orlando",
    "Cabo Cañaberal, Orlando",
    "Ciudad de Panamá, Panamá",
    "Tokyo, Japón"
]

class FeedPost:
    description = "Cool"
    comments = []

    def get_location(self):
        print("el self permite que esta función pueda acceder a los atributos del objeto")
        print(self.description)
        print(self) #Imprime el objeto como tal, es decirt
        return random.sample(locations,1)

    def show_comments(self):
        if self.comments: #Es decir, if self.comments == True. Sólo dará verdadero si la lista no está vacía
            return self.show_comments
        else:
            return "there are no comments"