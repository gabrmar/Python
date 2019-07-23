from openpyxl import Workbook #W mayúscula
wb = Workbook() #W mayúscula
ws = wb.active #No se está claro que es lo que hace
ws1 = wb.create_sheet("My sheet hello") #Se coloca al final de las hojas de Excel
ws2 = wb.create_sheet("My sheet 0", 0) #Al definir la posición, puedo colocar la hoja donde quiera
ws2.title = "My edited name sheet" #cambiar el nombre de las hojas de cálculo.
print(wb.sheetnames) #imprimir los nombres de las hojas 
ws.sheet_properties.tabColor = "1072BA" #Color de la pestaña
ws3 = wb["My sheet hello"] #esta variable aparentemente está asignando el contenido de la hoja que
#se llama como he descrito. Puedes hacer búsquedas en libro de cálculo de Excel usando
# el nombre de sus pestañas como índice.
print(ws3)
for sheet in wb: #los libros de cálculo son interables
    print(sheet.title) # imprimiendo título de hoja uno a la vez
source = wb.active #...
target = wb.copy_worksheet(source) #Copiando un libro de cálculo.