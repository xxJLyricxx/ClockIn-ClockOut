#this is a program that will create random word and name combinations.
#It will write this combination in two different files in two different files
#Text File 1 will have the name and 'password' combination in plain text format
#The second text file will have the username nad password combination in hashes
import hashlib
import random
import Words_List
import Names_List
from Names_List import maleFirstNames
from Names_List import femaleFirstNames
from Words_List import words
temphold = ""
storedDatabase = open("NameAndHashCombo.txt", 'w')
with open("NameAndWordCombo.txt", 'w') as f:
    print("NameAndWordCombo.txt Opened")
    counter = 1
    for x in range(10):
        gender = random.randint(0,1)
        a = random.randint(0,99)
        wordnum = random.randint(0,2643)
        if (gender == 0):
            firstname = maleFirstNames[a]
        else:
            firstname = femaleFirstNames[a]
        wordname = words[wordnum]
        temphold = firstname
#-=-=-=-=-=-=-=-=-=
#                    Print everything out

        print("")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print("The Random combination is: ")
        print("Name: ", firstname)
        print("Word: ", wordname)
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print("")
#-=-=-=-=-=-=-=-=-=-
#                    write everything to 'NameAndWordCombo.txt'
        f.write("\n")
        f.write("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        f.write("\nThe Random combination is: ")
        f.write("\nName: ")
        f.write(firstname)
        f.write("\nWord: ")
        f.write(wordname)
        f.write("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
#-=-=-=-=-=-=-=-=-=-=-=-=
#                    write everything to 'NameAndHashCombo.txt'
        renamed = hashlib.sha512(firstname.encode())
        wordpassed = hashlib.sha512(wordname.encode())
        storedDatabase.write(renamed.hexdigest())
        storedDatabase.write(wordpassed.hexdigest())
        storedDatabase.write("\n")
        storedDatabase.write("-=-=-=-=-=-=-=-=-=")
        storedDatabase.write("\n")
        
        
f.close()
storedDatabase.close()

'''
temphold = "Wrong"
temphold = hashlib.sha512(temphold.encode())
temphold = temphold.hexdigest()
foundit = 0
print(temphold)
print("Searching the database now.")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-==")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-==")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-==")
with open("NameAndHashCombo.txt", 'r') as f:
        lines = f.readlines()
        for line in lines:
            if (line.__contains__(temphold)):
                print(line)
                foundit = 1
        if (foundit==1):
            print("found it!")
            print(line)
        else:
            print("Does not exist in the database")
'''