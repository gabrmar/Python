#Welcome message
print("welcome to CheckMonth2")
#prompting  day and month
day = int(input("Please, add a day: "))
month = int(input("please, add a month: "))
#Defining max number of days per each month
monthly_days = [31,29,31,30,31,30,31,31,30,31,30,31]
#Validating day and month were added properly
if month > 12 or month < 1:
    print("invalid date for the month")
elif day > monthly_days[month-1] or day < 1:
     #Printing error message
    print("invalid date for the month")
else:
    #printing correct message
    print ("{}/{} is a valid birthday".format(day,month))

 
