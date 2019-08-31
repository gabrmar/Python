def Dosxuno(name="you"):
        if isinstance(name, str):
            print("one for {}, one for you".format(name))
        else:
            raise TypeError("Invalid parameter supplied, this function accepts only string as a parameter.")

Dosxuno()
Dosxuno("Galleta")
Dosxuno(1)
Dosxuno(True)
