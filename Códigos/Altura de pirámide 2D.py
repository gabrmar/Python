blocks = int(input("Enter the number of blocks: "))

height=0
cost=1
if blocks!=0:
    while blocks>0:
        if blocks>=cost:
            height +=1
            blocks -=height
            cost +=1
        else:
            break

print("The height of the pyramid:", height)