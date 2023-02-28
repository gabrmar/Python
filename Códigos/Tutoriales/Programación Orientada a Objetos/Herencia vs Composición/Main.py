from Clases.Comida import comida
from Clases.Macronutrientes import proteínas,carbohidratos,grasas

"""
-La clase comida  tiene a la clase protenínas, carbohidratos y grasas por medio
de la composición. Por otro lado, estas 3 clases son clases hijas de la clase
macronutrientes por medio de la herencia y gracias a esto la clase comida tiene
acceso a los métodos de la clase macronutirente sin recibir herencia por parte de ella.
"""


if __name__ == "__main__":

    avena = proteínas("vegetal",10)
    leche = grasas("Animal",15)
    cereal = carbohidratos("Ultraprocesado",5)
    desayuno = comida("avena con leche y cereal",30,avena,leche,cereal)
    print(desayuno)
    print(type(desayuno))

    print(desayuno.proteínas)
    print(desayuno.carbohidratos)
    print(desayuno.grasas)