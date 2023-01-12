import random

rango = range(1,11)
niveles = []
for i in rango:
    niveles.append(i)

class Mago:
    sanacion = True
    inteligencia = True
    experiencia = 20
    Mana = 70

    def recuperar_mana(self):
        valor = random.sample(niveles,1)[0] #[0] es necesario para poder obtener el elemento de la lista de random.sample
        print("+{}".format(str(valor))) 
