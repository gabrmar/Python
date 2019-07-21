print("this is a a code to ilustrate an example of the contitional i and some logical operators")

name = input("What is you name? ")
lastName = input("what about your last name? ")
age = int(input("How old are you? "))
occupation = input("What is your occupation? ")

if age < 18:
    print("you are uunderage. There is no way you have an occupartion yet. You should go to school")
else:
    print("Your name is "+ name + " " + lastName )
    if age > 18+5:
        print("It seems you have certain time since your graduation. \n I suppose you have been working hard")
        ans = input("Have been working as an " + occupation + " this years? Y/N ")
        if ans == "Y" or ans == "y":
            print("Quite interesting, gotta say")
            if age >18+10 and occupation == "Engineer" or occupation == "engineer":
                print("Well " + name + "," + " I see you have  all the requierements we need to get this job. \nWelcome to Super Company Inc.")
        elif ans == "N" or ans == "n":
            print("Well. If you would really like to work on what you studied, I hope you can do it soon")
            
            
        
    
