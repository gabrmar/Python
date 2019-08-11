def Dosxuno(*args):
    if len(args) == 0:
        print("One for you, one for me")
    else:
        print("one for {x}, one for you".format(x=args[0]))


Dosxuno()
Dosxuno("Galleta")
