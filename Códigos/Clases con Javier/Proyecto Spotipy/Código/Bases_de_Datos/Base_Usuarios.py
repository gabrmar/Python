from Clases.Usuario import usuario

admin = usuario("admin","admin@gmail.com","3006983847","admin")
gabo = usuario("Gabriel","gmll920628@gmail.com","3006983847","gabo")

lista_usuarios = [admin,gabo]

def consultar_usarios():
    return lista_usuarios