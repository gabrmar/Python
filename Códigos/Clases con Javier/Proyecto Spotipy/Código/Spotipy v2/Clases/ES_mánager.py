import time
from Clases.Usuario import usuario
from Bases_de_Datos.Base_Usuarios import consultar_usarios
from Clases.Excepciones import except_mánager
from Clases.Lista_repro import lista_reproducción

class IO_mánager:

    def iniciar(self):

        print("Bienvenidos a Spotipy")
        time.sleep(1)
        teclado = input("1. Iniciar Sesión.\n2. Registrarse.\n3. Salir\n")

        return teclado
        

    
    def registrar(self):

        excepciones = except_mánager()
        datos = []
        datos.append(input("Nombre:"))
        datos.append(input("Correo:"))  
        datos.append(input("Celular:"))
        datos.append(input("Contraseña:"))
        datos.append(input("confirmar contraseña:"))
        #---Validación del registro----
        excepciones.revisar_registro(datos)
        if datos[-2] == datos[-1]:
            u = usuario(datos[0],datos[1],datos[2],datos[3])
        else:
            verificación = False
            while(verificación== False):
                print("La contraseña no fue confirmada. Por favor revisar.")
                time.sleep(1)
                teclado4 = input("Contraseña:")
                teclado5 = input("confirmar contraseña:")
                if teclado4 == teclado5:
                    verificación = True
            u = usuario(datos[0],datos[1],datos[2],datos[3])
            
        del datos
        return u 

    def validar_registro(self):

        confirmación = False
        while confirmación == False:
            confirmación = input("¿Son estos datos correctos?S/N:")
            if confirmación == "S" or confirmación == "s":
                print("Registro exitoso")
                time.sleep(1)
                print("Bienvenido")
                #Toca generar un registro del usuario en algún lado.
                #Quizás la creación de la instancia sea suficeinte para ello, pero no creo
            elif confirmación == "N" or confirmación == "n":
                u = self.registrar()
                print(u)
                self.validar_registro() #Interesante, recursivdad en acción
            else:
                raise ValueError("Opción no válida. Sólo S o N")
        
    def iniciar_sesión(self,nombre,contraseña):
        usuarios = consultar_usarios()
        filtro = False
        filtro2 = False
        for usuario in usuarios:
            if usuario.nombre == nombre:
                filtro = True
                break
        for usuario in usuarios:
            if usuario.contraseña == contraseña:
                filtro2 = True
                #Propuesta para retornar el objeto tipo usuario
                break
        if filtro and filtro2:
            print("Usuario autenticado\n")
            return usuario
        else:
            print("Credenciales incorrectas\n")
            return False
         
    def pos_inicio(self,usuario): #Tal vez se pueden incluir como parte de la clase ES_Mánager
        teclado = input("1. Buscar cacnción\n2. Seleccionar lista\n3. Ajustes.\n")
        if teclado == "1":
            teclado = input("Coloca el nombre de la canción a buscar:")
            canción = usuario.buscar_canciones(teclado)
            print(canción) #Probar esta variante para casos exitosos y fracasos
            if type(canción) != str:
                return canción
            else:
                while type(canción) == str:
                    print("Intenta de nuevo o escribe x para salir")
                    time.sleep(1)
                    teclado = input("Coloca el nombre de la canción a buscar:")
                    if teclado == "x" or teclado == "X":
                        break
                    canción = usuario.buscar_canciones(teclado)
                    print(canción)
                    time.sleep(1)
                    return canción
        #----Acá se podría hacer una sfunción aparte de la clase ES_mánager que se llame canción_encontrada(cacnión)
        #canción_encontrada(canción) Estoy moviendo esta función hacia el código principal
        if teclado == "2":
            #Pasar listas de reproducción
            listas = usuario.listas_usuario
            time.sleep(1)
            print(listas)
            self.pos_inicio(usuario)
        if teclado == "3":
            print("Opción no disponible en esta versión de Spotipy")
            self.pos_inicio(usuario)

    def canción_encontrada(self,canción,usuario):
            print("¿Qué desea hacer?")
            teclado = input("1. Reproducir\n2. Agregar a lista de reproducción\n3. Buscar otra canción\n4. Cerrar Sesión\n")
            if teclado == "1":
                print(canción.letra)
                self.canción_encontrada(canción,usuario)
            if teclado == "2":
                if len(usuario.listas_usuario) == 0:
                    print("No hay listas de reproducción presentes en usuario {}. Se creará una lista nueva".format(usuario.nombre))
                    nombre_lista = input("Por favor añadir el nombre para la lista:")
                    lista_nueva = lista_reproducción(nombre_lista)
                    usuario.añadir_a_listas(nombre_lista,lista_nueva)
                    #usuario.añadir_a_lista(canción,lista_nueva)
                    opción = self.pos_inicio(usuario)
                    self.canción_encontrada(opción,usuario)
            if teclado == "3":
                teclado = input("Coloca el nombre de la canción a buscar:")
                canción = usuario.buscar_canciones(teclado)
                if type(canción) != str:
                    print(canción)
                    self.canción_encontrada(canción,usuario)
                else:
                    while type(canción) == str:
                        print(canción)
                        print("Intenta de nuevo o escribe x para salir")
                        time.sleep(1)
                        teclado = input("Coloca el nombre de la canción a buscar:")
                        if teclado == "x" or teclado == "X":
                            self.pos_inicio(usuario)
                            break
                        canción = usuario.buscar_canciones(teclado)
                        if type(canción) != str:
                            print(canción)
                            self.canción_encontrada(canción,usuario)
            if teclado == "4":
                print("Cerrando sesión...")
                time.sleep(1)
                #teclado = self.iniciar() esto require más revisión
