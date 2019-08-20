def Dosxuno(name = "you"):
    if isinstance(name, str) == True:
        if len(name) == "you":
            print("One for you, one for me")
        else:
            print("one for {x}, one for you".format(x=name))
    else:
<<<<<<< HEAD
        print("one for {x}, one for you".format(x=args[0]))

=======
        print("Wrong variable")

Dosxuno()
Dosxuno("Galleta")
>>>>>>> 60846d6640035449fba96ea288f4b87bf46e575d
