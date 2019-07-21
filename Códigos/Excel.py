from openpyxl import Workbook #W mayúscula
wb = Workbook() #W mayúscula
ws = wb.active
ws1 = wb.create_sheet("My sheet hello") #Se coloca al final de las hojas de Excel
ws2 = wb.create_sheet("My sheet 0", 0) #Al definir la posición, puedo colocar la hoja donde quiera
print(wb.sheetnames) #imprimir los nombres de las hojas 