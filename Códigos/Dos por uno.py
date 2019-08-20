def Dosxuno(name = "you"):
    if isinstance(name, str) == True:
        if len(name) == "you":
            print("One for you, one for me")
        else:
            print("one for {x}, one for you".format(x=name))
    else:
        print("Wrong variable. This methods work with string variables only")

Dosxuno()
Dosxuno("Galleta")
Dosxuno(1)
Dosxuno(True)