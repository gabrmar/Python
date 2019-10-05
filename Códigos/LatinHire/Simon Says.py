from random import randint
RGBY = "RGBY"
SimonPattern = ""
print("Welcome to Simon Says")
while len(SimonPattern) != 10:
    index = randint(0, 3)
    SimonPattern = SimonPattern + RGBY[index]
print("Simon Says: {}".format(SimonPattern))
UserPattern = input("Now is your turn. Repeat Simon's pattern:")
score = 0
for  i  in range(0,10):
    if SimonPattern[i] == UserPattern[i]:
        score = score + 1
        i = i + 1
    else:
        break
if i == 9:
    score = score + 1    
print("Total Score: {}".format(score))
