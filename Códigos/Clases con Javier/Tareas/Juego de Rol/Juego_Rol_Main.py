from Juego_Rol import Mago

merlin = Mago()
merlin.mana = 100
merlin.experiencia = 50
gaspar = Mago()
gaspar.sanacion = False
gaspar.experiencia = 150
ron = Mago()

gaspar.recuperar_mana()

del gaspar

merlin.recuperar_mana()
Mago.recuperar_mana(merlin)
merlin.pared_magica()

ron.pared_magica()

merlin.experiencia = 60

merlin.rafaga_de_plasma(20)
ron.rafaga_de_plasma(20)