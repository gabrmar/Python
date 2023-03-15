from Bases_de_Datos.Base_Canciones import acceder_canciones
from Clases.Lista_repro import lista_reproducción
from Clases.Listas import listas_reproducción
class usuario:
    def __init__(self,nombre,correo,celular,contraseña):
        self.nombre = nombre
        self.correo = correo
        self.celular = celular
        self.contraseña = contraseña
        self.listas_usuario = listas_reproducción() #propuesta: usar clase listas 

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
                #break
        if resultado == False:
            return "Canción no encontrada. Intenta de nuevo"
        
    def buscar_listas(self,nombre_lista):
        if nombre_lista in self.listas:
            print("Lista encontrada")
            return self.listas[nombre_lista]
        else:
            print("Lista no encontrada. La lista será creada")
            return False
        
    def añadir_a_listas(self,nombre_lista,lista_reproducción):
        self.listas_usuario.listas[nombre_lista] = lista_reproducción
        print("Lista de reproducción {lista} añadadida para el usuario {usuario}".format(lista=nombre_lista,usuario=self.nombre))
        
    def añadir_a_lista(self,canción,nombre_lista):
        lista = self.buscar_listas(nombre_lista)
        if type(lista) == list: #Puede que usar lista_reproducción en vez de list sea mejor
            pass
        else:
            lista = lista_reproducción(nombre_lista)
            lista.añadir_a_lista(canción,lista.nombre) #Añadir canción a la lista de reproducción
            self.añadir_a_listas(lista.nombre,lista) #Añadir la lista de reproducción a la colección de listas de reproducción de un usuario


            
