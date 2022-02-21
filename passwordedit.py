#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#PROGRAM NAME: passwordedit.py
#AUTHOR: GARY DAVIS
#DATE: 1/21/2022
#DESCRIPTION: THIS PROGRAM IS A PASSWORD VALIDATOR. IT STARTS UP AND PRINTS A WELOME MESSAGE ON ./RUN
# - AFTER GREETING THE USER, IT ASKS FOR AN INPUT [QQ] (NAMING CONVENTIONS TO BE UPDATE LATER)
# - THE INPUT IS THEN SAVED IN TEMPORARY MEMORY WHILE SORTING THROUGH THE DATABASE
# - THE 'DATABASE' IN THIS CASE IS A TEXT FILE [PASSWORDS.TXT]. IT IS SAVED IN THE SAME FOLDER AS THE PROGRAM.
# - THE PROGRAM SEARCHES DOWN THE PAGE OF THE DATABASE FOR A STRING CONTAINING THE SAME STRING AS THE INPUT.
# - - *AS OF NOW, IF THERE ARE ANY DUPLICATES, THE PROGRAM WILL LOOP UNTIL ALL DUPLICATES HAVE THEIR PASSWORDS RESET. UPDATE NEEDED
# - IF THE USER'S NAME IS FOUND IT WILL PRINT A CONFIRMATION, AND ASK FOR THE MATCHING PASSWORD
# - IF NOT, THE USER WILL BE NOTIFIED THAT IT'S NOT CORRECT AND THE PROGRAM WILL TERMINATE.
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=


f = open("Passwords.txt", "r")
q = 0                                                       #This is just a flag                                                                                      
i = 0

#------
#test--
#------
#ff = remove(f.readline(10))
#print("The string is: ", ff)
#print(len(ff))
#print("The type is: ", type(ff))
#qq = input("PLEASE ENTER YOUR USERNAME: ")
#print(qq)
#qq = qq.lower()
#print(qq)
loopflag = 0
while (loopflag == 0):
   # if (ff.__contains__(qq)):
        #print("yes")
        #loopflag = 1
        #ff = remove(f.readline())
        #qq = input("Please enter the password: ")
        #qq = qq.lower()
        #if (ff.__contains__(qq)):
        #    print("Password matches!")
        #else:
        #    print("Password does not match!")

    #else:
        #print("no")
        #print("Reading more...")
        #ff = f.readline()
       # print("_______________")
        #print(ff)
        #print("------there goes the password---------")
        #ff = remove(f.readline(10))
        #if (ff == ""):
        #    print("Not in the list")
        #    loopflag = 1
    f.close()
print("fin password.py")