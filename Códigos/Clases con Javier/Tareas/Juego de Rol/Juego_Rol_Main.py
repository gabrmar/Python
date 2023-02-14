from Módulos.Juego_Rol import Ladron,Arquero
from Módulos.Mago import Mago

merlin = Mago("Merlin")
merlin.mana = 100
merlin.experiencia = 50
gaspar = Mago("Gaspar")
gaspar.sanacion = False
gaspar.experiencia = 150
ron = Mago("Ron")
gandalf = Mago("Gandalf",100,200,obra="Señor de los Anillos",comentarios="**kwargs es algo de otro mundo")
richard = Ladron("Richard")
robin = Arquero("Robin",20,50,"Arco desgastado",obra="Robin Hood")

gaspar.recuperar_mana()

del gaspar

merlin.recuperar_mana()
Mago.recuperar_mana(merlin)
merlin.pared_magica()

ron.pared_magica()

merlin.experiencia = 60

merlin.rafaga_de_plasma(20)
ron.rafaga_de_plasma(20)
print(gandalf.health_points)
print(gandalf.comentarios)
print(gandalf.mana)
print(dir(gandalf))

print(richard.mana)
richard.robar()
print("Experiencia del ladrón {a} es {b}".format(a=richard.nombre,b=richard.experiencia))
print("Mana del ladrón {a} es {b}".format(a=richard.nombre,b=richard.mana))


robin.apuntar()
robin.disparar()
print("salud del arquero {a} es {b}".format(a=robin.nombre,b=robin.health_points))
print(robin.obra)
print(robin.arco)
print(robin.experiencia)