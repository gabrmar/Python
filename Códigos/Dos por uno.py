def Dosxuno(name="you"):
        if isinstance(name, str):
            word = "one for " + str(name) +", one for me"
        else:
            raise TypeError("Invalid parameter supplied, this function accepts only string as a parameter.")
        return word

hola = Dosxuno()
print(hola)
hola2 = Dosxuno("Galleta")
print(hola2)
#-----quita los comentarios de abajo para generar excepciones de tipo-----#
#hola3 = Dosxuno(1)
#hola4 = Dosxuno(True)
