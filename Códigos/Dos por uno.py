def Dosxuno(name = "you"):
    if isinstance(name, str) == True:
        if len(name) == "you":
            print("One for you, one for me")
        else:
            print("one for {x}, one for you".format(x=name))
    else:
        print("Wrong variable. This method work with string variables only")

Dosxuno()
Dosxuno("Galleta")
Dosxuno(1)
Dosxuno(True)
>>>>>>> 9cb394938cc688e6f69e8eaa608416283a9d546f
