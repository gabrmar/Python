class except_mánager:

    def revisar_registro(self,lista_datos):
        #El objetivo es reivsar los datos presentes en la lista de dato y dar excepciones para los siguoentes casos:
        #   -Cuando el correo no tiene el símbolo arroba (@).
        #   -Cuando el número de celular no tiene la longitud propia de un número para celulares.
        #   -Cuando el númerop de celular tiene caracteres que no son numéricos.
        if lista_datos[0] == "prueba": #condición de prueba
            raise ValueError("Esta es una excepción de prueba.")
        """
        No estoy seguro si podré usar varias veces la misma excepción, pero creo que sí podré hacerlo con el uso
        del raise.
        """