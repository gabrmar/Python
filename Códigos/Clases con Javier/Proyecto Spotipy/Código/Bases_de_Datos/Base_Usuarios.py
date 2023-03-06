from Clases import Usuario

admin = Usuario("admin","admin@gmail.com","3006983847","admin")
gabo = Usuario("Gabriel","gmll920628@gmail.com","3006983847","gabo")

lista_usuarios = [admin,gabo]

def consultar_usarios():
    return lista_usuarios