lista = ["galleta","galletas","galletan"]
objetivo = "galleta"
for i in range(len(lista)):
    if objetivo in lista: #Este va a buscar todas las coincidencias considerando incluso partes de la cadena de caracteres de cada miembro de la lista
        print(lista[i])
for i in range(len(lista)):
    if objetivo == lista[i]: # Por otro lado, acá busca una coincidencia exacta, así que si una sub-cadena coincide con el objetivo, igualmente será descartada
        print(lista[i])



