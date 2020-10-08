from bokeh.plotting import figure, output_file, show  # Importando elementos necesarios de Bokeh para el código
 
if __name__ == '__main__': 
    output_file('graficado_simple.html') # Creando archivo html que se usará para mostrar la gráfica
    fig = figure() # Creando objeto tipo gráfica (figure en inglés)
    
    total_vals = int(input('¿Cuántos valores quieres graficar?:')) # Pidiendo la cantidad de valores a graficar
    x_vals = list(range(total_vals)) # Creando lista que representa las posiciones en X 
    y_vals = [] # Creando lista vacía donde se colocarán los valores en Y

    for x in x_vals: # Ciclo for para pedir los valores en Y
        val = int(input(f'Valor y para {x}:')) 
        y_vals.append(val) # Agregando los valores a la lista por medio del  método append

    fig.line(x_vals, y_vals, line_width=5) # Graficando con la lista de valores en X,Y y definiedo  el ancho de la lista. Este último
    # valor es opcional
    show(fig) # Mostrar figura
    
