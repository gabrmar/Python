from openpyxl import Workbook  # W mayúscula
wb = Workbook()  # W mayúscula
ws0 = wb.active  # No se está claro que es lo que hace
# Se coloca al final de las hojas de Excel
ws1 = wb.create_sheet("My sheet hello")
# Al definir la posición, puedo colocar la hoja donde quiera
ws2 = wb.create_sheet("My sheet 0", 0)
# cambiar el nombre de las hojas de cálculo.
ws2.title = "My edited name sheet"
print(wb.sheetnames)  # imprimir los nombres de las hojas
ws0.sheet_properties.tabColor = "1072BA"  # Color de la pestaña
# esta variable aparentemente está asignando el contenido de la hoja que
ws3 = wb["My sheet hello"]
# se llama como he descrito. Puedes hacer búsquedas en libro de cálculo de Excel usando
# el nombre de sus pestañas como índice.
print(ws3)  # imprime la hoja de cálculo
for sheet in wb:  # los libros de cálculo son interables
    print(sheet.title)  # imprimiendo título de hoja uno a la vez
source = wb.active  # ...
target = wb.copy_worksheet(source)  # Copiando un libro de cálculo.
# Jugando con datos
c = ws0["A4"]  # Asignando contenido de celda A4 de la hoja ws0 a variable c
print(c)  # imprimiendo celda
ws0["A4"] = 4  # asignando un nuevo valor a la celda A4 de la hoja ws0
c = ws0["A4"]  # Reasignando el valor de c
print(c)  # imprime la celda
# También se puede acceder a las celdas por este medio
d = ws0.cell(row=1, column=1, value=2)
print(d)  # imprimiendo la celda
e = ws0.cell(5, 6, 10)  # fila 5, columna 6 y valor 10
print(e)  # imprimiendo la celda
cell_range = ws0["A1":"C2"]  # Aisgnar un rango de Excel a una variable
# Nota: Rangos en diagonal como el descrito arriba representan todas las filas y columnas
# contenidas entre los extremos colocados.
print(cell_range)  # Imprimiendo rangos.
