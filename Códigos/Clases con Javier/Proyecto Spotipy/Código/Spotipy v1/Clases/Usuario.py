from Bases_de_Datos.Base_Canciones import acceder_canciones

class usuario:
    def __init__(self,nombre,correo,celular,contraseña):
        self.nombre = nombre
        self.correo = correo
        self.celular = celular
        self.contraseña = contraseña

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
    
    def buscar_canciones(self,nombre_canción): #Toca hacer la prueba de conceptos
        acceso = acceder_canciones()
        resultado = False
        for objeto in acceso:
            if nombre_canción == objeto.nombre: # Tiene que ser una equivalencia exacta
                resultado = True
                return objeto
                break
        if resultado == False:
            return "Canción no encontrada. Intenta de nuevo"
            
