#Afirmaciones (excepciones) en Python
"""
Las afirmaciones son condiciones  cuyo incumplimineto cierra el programa
por defecto. Se usan mucho para validar los datos de entrada suministrdos
por el usuario y las salida de las funciones realizadas por el programa
"""
np = float(input("agrega un número entero positivo positivo menor que 100:"))
assert (np>=0),"Colocaste un número negativo. Error" #el mensaje es opcional
assert(np<100)#se activará el error de aserción sin un mnensaje




        
