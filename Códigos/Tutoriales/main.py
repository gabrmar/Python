# uso del main en python

"""
los main son arhivos que pueden funciionar como módulos para
ser importados por otros programas como códigos independientes
"""

def function():
   print("This is a module function")

if __name__=="__main__": #asegura que el archivo se comporatá como módulo
    #si es importado
   # todo lo que va dentro del main es lo que s eejecuta cuando
   # es tratado como arhico principal en vez de módulo importado
   # es decir que print("this is a script") no será impreso
   # cuando es importado, sino cuando es tratado como archivo principal
   print("This is a script")

## se puede colocar un else para definr el resto del código que será ejecutado
   #cuando es importado
else:
   print("hello") #esto aparecerá por defecto cuando el módulo es importado

