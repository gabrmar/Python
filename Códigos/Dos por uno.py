def Dosxuno(name="you"):
    if isinstance(name, str):
        print("one for {x}, one for you".format(x=name))
    else:
        print("Wrong variable. This method work with string variables only")

Dosxuno()
Dosxuno("Galleta")
Dosxuno(1)
Dosxuno(True)
>>>>>>> 9cb394938cc688e6f69e8eaa608416283a9d546f
