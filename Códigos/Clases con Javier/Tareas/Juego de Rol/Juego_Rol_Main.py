from Juego_Rol import Mago,Ladron,Arquero

merlin = Mago("Merlin")
merlin.mana = 100
merlin.experiencia = 50
gaspar = Mago("Gaspar")
gaspar.sanacion = False
gaspar.experiencia = 150
ron = Mago("Ron")
gandalf = Mago("Gandalf",100,200,obra="Señor de los Anillos",comentarios="**kwargs es algo de otro mundo")
richard = Ladron("Richard")
robin = Arquero("Robin",10,"Arco Simple")

gaspar.recuperar_mana()

del gaspar

merlin.recuperar_mana()
Mago.recuperar_mana(merlin)
merlin.pared_magica()

ron.pared_magica()

merlin.experiencia = 60

merlin.rafaga_de_plasma(20)
ron.rafaga_de_plasma(20)
print(dir(gandalf))

print(richard.mana)
richard.robar()
print(richard.mana)

robin.apuntar()
robin.disparar()
