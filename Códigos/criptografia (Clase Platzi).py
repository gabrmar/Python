# -*- coding: utf-8 -*-
# codificación de caracteres especiales del español y otros idiomas

# Creación de diccionarioque sirve de clave para codifiicar cada letra de un mensaje
KEYS = {
    'a': 'w', # la se cambia por una w
    'b': 'E', # la b se cambia por una E (mayúscula)
    'c': 'x', # la c se cambia por una x y así susecivamente  
    'd': '1',
    'e': 'a',
    'f': 't',
    'g': '0',
    'h': 'C',
    'i': 'b',
    'j': '!',
    'k': 'z',
    'l': '8',
    'm': 'M',
    'n': 'I',
    'o': 'd',
    'p': '.',
    'q': 'U',
    'r': 'Y',
    's': 'i',
    't': '3',
    'u': ',',
    'v': 'J',
    'w': 'N',
    'x': 'f',
    'y': 'm',
    'z': 'W',
    'A': 'G',
    'B': 'S',
    'C': 'j',
    'D': 'n',
    'E': 's',
    'F': 'Q',
    'G': 'o',
    'H': 'e',
    'I': 'u',
    'J': 'g',
    'K': '2',
    'L': '9',
    'M': 'A',
    'N': '5',
    'O': '4',
    'P': '?',
    'Q': 'c',
    'R': 'r',
    'S': 'O',
    'T': 'P',
    'U': 'h',
    'V': '6',
    'W': 'q',
    'X': 'H',
    'Y': 'R',
    'Z': 'l',
    '0': 'k',
    '1': '7',
    '2': 'X',
    '3': 'L',
    '4': 'p',
    '5': 'v',
    '6': 'T',
    '7': 'V',
    '8': 'y',
    '9': 'K',
    '.': 'Z',
    ',': 'D',
    '?': 'F',
    '!': 'B',
}

# Definición de función para cifrar el mensaje
def cypher(message):
    words = message.split('') # Speración de mensaje string en lista usando
    # como separador el espacio en blanco (este es el separador por defecto así que no es necesario colocarlo)
    print(words) #Visualizar la lista por motivos de aprnedizaje. Comentar cuando se quiera
    cypher_message = [] #Lista vacía donde estará el mensaje cifrado
    
    for word in words:
        cypher_word = '' # string vacío donde estará el mensaje cifrado
        for letter in word:
            cypher_word += KEYS[letter] # Mensaje cifrado se forma de ir añadiando cada una de las letras
            # convertidas usando el diccionario KEYS y usando de llave las letras de la variable words

        cypher_message.append(cypher_word) # Adjunta resultado del cifrado letra por letra 

    return ' '.join(cypher_message) # Convirtiendo lista cifrada en String

# Definición de la función para decifrar el mensaje
def decipher(message):
    words = message.split(' ') # Separación de los elementos del string y conversión de ellos en una lista
    decipher_message = [] # Lista vacía donde estará el mensaje dcifrado

    for word in words:
        decipher_word = '' # String vacía donde estará el mensaje decifrado

        for letter in word:
            for key, value in KEYS.items():
                if value == letter: # Comparar que los elementos del mensaje cifrado coinciden con letras
                    # cifradas dentro del diccionario
                    decipher_word += key # Si es así, entonces el mensaje decifrado se va formando de las llaves
                    # del diccionario en donde se den las coincidencias 

        decipher_message.append(decipher_word) # Añadiendo caracteres decifrados uno por uno a la lista

    return ' '.join(decipher_message) # Convirtiendo lista decifrada a string

# Definición de función principal
def run():

    # Cilco indefinido
    while True:

        command = str(input('''--- * --- * --- * --- * --- * --- * --- * ---

            Bienvenido a criptografía. ¿Qué deseas hacer?

            [c]ifrar mensaje
            [d]ecifrar mensaje
            [s]alir
        '''))

        if command == 'c':
            message = str(input('Escribe tu mensaje: '))
            cypher_message = cypher(message)
            print(cypher_message)

        elif command == 'd':
            message = str(input('Escribe tu mensaje tu cifrado: '))
            decypher_message = decipher(message)
            print(decypher_message)
        elif command == 's':
            print('salir')
            break #Rompiendo ciclo infinito (Aporte personal al código)
        else:
            print('¡Comando no encontrado!')


if __name__ == '__main__':
    print('M E N S A J E S  C I F R A D O S')
    run()
