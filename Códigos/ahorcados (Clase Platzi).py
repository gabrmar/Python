# -*- coding: utf-8 -*-
# La línea uno se utiliza para asegurar que el intérprete de Python
# reconozca el codificacdore utf-8 que incluye símbolos especiales
# como la tilde letras propias del español como la "ñ"
import random #importar módulo de funciones alaeatorias

#Lista de imágenes en ASCII Art  (averiguar por qué se agregan usando comillas triples) 
IMAGES = ['''

    +---+
    |   |
        |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
    |   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        =========''', '''
''']

#Lista de palabras para juego del ahorcado
WORDS = [
    'lavadora',
    'secadora',
    'sofa',
    'gobierno',
    'diputado',
    'democracia',
    'computadora',
    'teclado'
]

#Definición de función de seleccionador aleatorio de palabra
def random_word():
    idx = random.randint(0, len(WORDS) - 1) #Definiendo índice entre 0 y la última posición de la lista de palabras
    return WORDS[idx] #Regresa elemento de la lista en la posición aleatoria definida en la línea de arriba

#Definición de función para imprimir el ahorcado en ASCII Art
#Recibe de entrada la palabra oculta basada en la palabra seleccionada por la función anterior
# y el número que representa los intentos que le quedan al jugador
def display_board(hidden_word, tries): 
    print(IMAGES[tries]) #Imprimir imagen según el intento que corresponde
    print('') #Espacio
    print(hidden_word) #Palabra oculta
    print('--- * --- * --- * --- * --- * --- ') #Línea de separación entre intentos

#Definición de función principal
def run():
    word = random_word() #Selección de palabra aleatoria
    hidden_word = ['-'] * len(word) #La palabra oculta es una lista compuesta por guiones y cuya longitud es ocultar
    #La palabra que el jugador debe adivinar.
    tries = 0 #Número de intentos usados
    while True:
        display_board(hidden_word, tries) #imprimir ASCI Art
        current_letter = input('Escoge una letra: ')

        letter_indexes = [] #Lista vacía
        for idx in range(len(word)):
            if word[idx] == current_letter:
                letter_indexes.append(idx) #Guarda el índice donde se dió la coincidencia

        if len(letter_indexes) == 0:
            tries += 1 #Avanzar al intento siguiente dado que la letra no está en la palabra 

            if tries == 7: #El límte de intentos es 8 puesto que hay 8 dibujos (7 es el último índice).
                display_board(hidden_word, tries)
                print('')
                print('¡Perdiste! La palabra correcta era {}'.format(word))
                break
        else:
            for idx in letter_indexes:
                hidden_word[idx] = current_letter #Agregar la letra  en la posición donde hubo la coincidencia

            letter_indexes = [] #Vaciar la loista para el próximo intento

        try:
            hidden_word.index('-') #Busca que no faltan letras por buscar en la palabra
            #En el caso de que sea así, entonces la función index() genera un ValueError que debe ser manejado
            # por medio de una excepción.
        except ValueError:
            print('')
            print('¡Felicidades! Ganaste. La palabra es: {}'.format(word))
            break #Interrupción del ciclo generado por el ciclo While


if __name__ == '__main__': #Garantizando el inicio de la ejecución del código aquí
    print('B I E N V E N I D O S  A  A H O R C A D O S')
    run()
