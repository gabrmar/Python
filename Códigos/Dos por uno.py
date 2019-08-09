def Dosxuno(*args):
    if len(args) == 0:
        print("One for you, one for me")
    else:
        #Convertir las tuplas en Strings
        print("One for {x}, one for me".format(x=args))

Dosxuno()
Dosxuno("Pablo")

        
        
