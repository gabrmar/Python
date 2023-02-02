
#Averiguar cómo es que se piden varios parámeros por medio de la fucnión input()

"""

Ask the user to enter two numbers separated by a comma or other character

value = input("Enter 2 numbers (separated by a comma): ")

Then, the string is split: n takes the first value and m the second one

n,m = value.split(',')

Finally, to use them as integers, it is necessary to convert them

n, m = int(n), int(m)

Source: https://stackoverflow.com/questions/961263/two-values-from-one-input-in-python
"""