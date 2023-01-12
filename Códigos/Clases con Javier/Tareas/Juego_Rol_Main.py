from Juego_Rol import Mago

merlin = Mago()
merlin.mana = 100
merlin.experiencia = 50
gaspar = Mago()
gaspar.sanacion = False
gaspar.sanacion = 150
del gaspar

merlin.recuperar_mana()
