from openpyxl import Workbook #W mayúscula
wb = Workbook() #W mayúscula
ws = wb.active #No se está claro que es lo que hace
ws1 = wb.create_sheet("My sheet hello") #Se coloca al final de las hojas de Excel
ws2 = wb.create_sheet("My sheet 0", 0) #Al definir la posición, puedo colocar la hoja donde quiera
ws2.title = "My edited name sheet" #cambiar el nombre de las hojas de cálculo.
print(wb.sheetnames) #imprimir los nombres de las hojas 
ws.sheet_properties.tabColor = "1072BA" #Color de la pestaña
ws3 = wb["My sheet hello"] #esta variable aparentemente está asignando el contenido de la hoja que
#se llama como he descrito. Puedes hacer búsquedas en una hoja de cálculo de excel usando
# el nombre de sus pestañas como índice.
print(ws3)