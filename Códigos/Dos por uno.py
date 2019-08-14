def Dosxuno(name = "you"):
    if len(name) == "you":
        print("One for you, one for me")
    else:
        print("one for {x}, one for you".format(x=name))


Dosxuno()
Dosxuno("Galleta")
