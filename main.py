import string
import random


# Gettin' passwd lenght
lenght = int(input("Enter password lenght: "))

print('''Choose character set for password from these:
         1. Digits
         2. Letters
         3. Special characters
         4. Exit''')

characterList = ""

#char set for rand passwd
while(True):
    charChoice = int(input("Pick an option: "))
    if(charChoice <= 4):
        match charChoice:
            case 1:
                characterList += string.ascii_letters
                #ascii letters to possible characters

            case 2:
                characterList += string.digits
                #digits to possible char

            case 3:
                characterList += string.punctuation
                #spec char to possible char

            case 4:
                break
    else:
        print("Please pick a valid option!")

password = []

for i in range (lenght):
    #rand char
    randomchar = random.choice(characterList)

    #append passwd with rand
    password.append(randomchar)

print('''Random generated password is: 
      ''' + "".join(password))

