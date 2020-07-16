# -*- coding: utf-8 -*-

def foreign_exchange_calculator(ammount):
    mex_to_col_rate = 145.97

    return mex_to_col_rate * ammount

def run():
    print('C A L C U L A D O R A  D E  D I V I S A S')
    print('Convierte pesos mexicanos a pesos colombianos.')
    print('')

    ammount = input('Ingresa la cantidad de pesos mexicanos que quieres convertir: ')

    result = foreign_exchange_calculator(ammount)

    print('${} pesos mexicanos son ${} pesos colombianos'.format(ammount, result))
    #.format se usa colocando llaves en los espacios donde quieres inserar variables
    #Una forma diferente de utilizar el ,format es asignando variables  al texto de la
    # siguiente manera:
    """  print('${x} pesos mexicanos son ${y} pesos colombianos'.format(x=ammount,y=result))
    """
    print('')

if __name__ == '__main__': #el código empieza a ejecutarse aquí. Es punto de partida para empezara leer código de Python.
    run()
    print('Final {}')
