
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
        return"Clase tipo {a}\nNombre:{b}\nCorreo:{c}\nCelular:{d}\nContraseña:{e}".format(a=type(self),b=self.nombre,c=self.correo,d=self.celular,
                                                                                           e=self.contraseña)