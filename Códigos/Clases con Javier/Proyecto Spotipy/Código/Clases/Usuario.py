
class usuario:
    def __init__(self,nombre,correo,celular,contraseña):
        self.nombre = nombre
        self.correo = correo
        self.celular = celular
        self.contraseña = contraseña

    def proteger_contraseña(self):
        #self.contraseña será usado para entregar una contraseña protegida
        pass

    def __str__(self):

        clase ="Clase tipo:{}\n".format(type(self))
        nombre ="Nombre:{}\n".format(self.nombre)
        correo ="Correo:{}\n".format(self.correo)
        celular ="Celular:{}\n".format(self.celular)
        l = len(self.contraseña)
        asteriscos = "*"*l #multiplicador de asteristcos según el largo de la
        #contraseña
        contra_protegida = self.contraseña.replace(self.contraseña,asteriscos)
        contraseña_asteriscos ="Contraseña:{}\n".format(contra_protegida) 
        return clase+nombre+correo+celular+contraseña_asteriscos