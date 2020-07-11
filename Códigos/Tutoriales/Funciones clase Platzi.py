
import turtle # Módulo pra hacer gráficos 

def main():
    window = turtle.Screen()
    dave = turtle.Turtle()

    make_square(dave)

    turtle.mainloop()

def make_square(dave):
    length = input('Tamaño de cuadrado: ')
    length = int(length) 

    for i in range(4):
        make_line_and_turn(dave, length)

def make_line_and_turn(dave, length):
    dave.forward(length)
    dave.left(90)

if __name__ == '__main__':
    main()
"""Esto es bastante interesante. Normalmente los códigos de Python se ejecutan desde arriba hacia abajo,
Es decir que es necesario siempre colocar las definiciones d elas funciones antes de la parte del código
en donde se terminan ejecutando. Una forma de hacer que la ejecución del código no se dé desde la parte
más arriba es usando la sentencia _name_ y comparándola con el nobre de la que será la función principal,
es decir la función main. Basta con comparar el _name_ con el nombre que uno le de a la función principal."""