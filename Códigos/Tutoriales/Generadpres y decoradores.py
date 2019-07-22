"""
Los generadores son otro tipo de iterables como las listas y tuplas.
Se diferencia en que este no puede ser iterado por índices arbitrarios,
sino por ciclos para. Todo generador opera con la delcaación yield
como remplazo de la edclración return
"""

def conteo(): #definiendo generador
  i=5
  while i > 0:
    yield i #reemplazo del return que genera los elementos del iterable
    # Las variables locales dentro de una función con yield no son borradas
    i -= 1


for i in conteo(): #usando ciclo for para accerder al generador
  print(i)
print(list(conteo())) #formatear generador a lista

def numbers(x): # definiendo generador con argumento x
  for i in range(x):
    if i % 2 == 0: #Evaluando si el número es par o no
      yield i # generando sólo números divisibles entre 2
      
"""
Python ofrece el uso de recursos para modificar las funciones predefinidas
y las creadas por el ususario sin necesidad de hacer los cambios directamente.
En vez de eso se realiza un "código de decoración" que es una función de orden
superior la cual toma de argumento la función de la cual se quiere hacer
cambios. Este tipo  de códigos de decoración  se les conoce como decoradores.
"""

def decoración(f): # donde f es una función
    def resultado(): # código de decoración
        print("Estás viendo")
        f() #acá se coloca la fucnión base
        print("el resultado de una función decorada")
    return resultado #se entrega el resultado decorado

def print_text():
    print("Hello world!")

def decoración2(f): # donde f es una función
    def resultado(): # código de decoración
        print("Estás viendo")
        f() #acá se coloca la fucnión base
        print("decoraciones")
    return resultado #se entrega el resultado decorado

@decoración2 #puedes decorar la función con ayuda del arroba y el nombre
# de la decoración
def print_text2():
    print("Hello decorators!")


print(list(numbers(11))) #formatear generador a lista
decorado = decoración(print_text) #se asigna resultado una objeto
decorado() #se presenta aquí el resultado en pantalla
print_text = decoración(print_text) #también puede renombar la función
# sin decorar para que ahora trabaje con el código decorado
print_text() #la salida ya estará decorada
print_text2() #la salida ya estará decorada




  
