def Dosxuno(name="you"):
    if isinstance(name, str):
        print("one for {x}, one for you".format(x=name))
    else:
        print("Wrong variable. This method work with string variables only")

Dosxuno()
Dosxuno("Galleta")
Dosxuno(1)
Dosxuno(True)