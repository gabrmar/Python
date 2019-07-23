

def comprobarCaracter(texto,caracter):
    ans = False
    for i in texto:
        if i == caracter:
            ans = True
    return ans


def is_pangram(sentence):
    alphabet = "abcdefghijklmopqrstuvwxyz" 
    pangram = len(alphabet)
    c = 0

    for i in alphabet:
        char = i
        ans = comprobarCaracter(sentence,char)
        if ans == True:
            c = c + 1
        else:
            print ("Character " + char +" not found")    
    if c == pangram:
        print("It is a pangram")
    else:
        print("It is not a pangram")
    pass

    
#is_pangram("the quick brown fox jumped over the lazy FX")
"""alphabet = "abcdefghijklmopqrstuvwxyz" 
pangram = len(alphabet)
c = 0
texto = input('Add input text here :')
texto = texto.lower()
print('Use the input text and check if you can decompose it into its characters')
for i in alphabet:
    char = i
    ans = comprobarCaracter(texto,char)
    if ans == True:
        c = c + 1
    else:
        print ("Character " + char +" not found")    
if c == pangram:
    print("It is a pangram")
else:
    print("It is not a pangram")"""


    #June the 6th: I can use FOR cycles to look for matches
    #I need to read in detail the code "Analizador de texto.py"
    #June the 10th: Started the coding of the test code.
    #June the 11th: Function to check characters in progress.
    #June the 12th: Function to check characters complete
    #June the 13th: First attempt to make the pangram code was done.
    # Finding pangrams based string length does not work. I have to find other way 
    #June the 14th: Finding pangrams based on string length does worked. I only neeed to deal with upper cases.
    #June the 17th: Finish using all the strings on pangram_test.py 
    #June the18th: Pangram test complete. Now it is time delete test lines.
    #June the 19th: Test lines deleted. It would be cool to paste all trhe code into the function defined by Excersism.
    #June the 20th: Test adapted to fit pangram_test.py. Just one error to deal with.
    #June the 25th: Test submitted.

    

        


