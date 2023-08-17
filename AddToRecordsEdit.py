#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# PROGRAM NAME: AddToRecords(edit).py
# AUTHOR: GARY DAVIS
# DATE: 1/21/2022
# DESCRIPTION: THIS PROGRAMS PURPOSE IS TO ADD ENTRIES TO THE 'DATABASE' 
# IN THIS CASE, THE DATABASE IS A TEXT FILE THAT IS SAVED 
# IN THE SAME FOLDER AS THE PROGRAM ITSELF. THE TEXT FILE INCLUDES NAMES, 
# JOBS, ADMIN RIGHTS (WRITTEN AS EITHER 'TEAM' OR 'ADMIN') 
# AND THEIR COUNT OF HOURS. THERE ARE A LOT OR
# VALIDATOR LOOPS IN THIS PROGRAM. MOSTLY JUST TO MAKE SURE THAT THE CONVENTIONS FOR 
# INPUTTING DATA REMAINS CONSISTANT WITH THE REST OF THE ENTRIES IN THE DATABASE.
# FIRST THE USER IS ASKED IF THEY WOULD LIKE TO ENTER A NEW USER. THE INPUT MUST BE 
# 'Y' OR 'YES'. EITHER WILL WORK. THE INPUT IS [LOWER.()]'D JUST IN CASE. IF THERE IS *ANY* OTHER 
# INPUT, THE PROGRAM WILL TERMINATE. IF THE INPUT IS ACCEPTED THEN THE USER WILL BE PROMPTED TO 
# ADD A NAME. WHEN ADDING A NAME, IT CAN NOT BE MORE THAN 10 CHARACTERS. THE USER WILL BE PROMPED 
# TO CHANGE THE NAME TO SOMETHING THAT IS LESS THAN 10 CHARACTERS 3 TIMES. IF THE USERS INPUT 
# IS STILL LONGER THAN 10 CHARACTERS, THEIR INPUT WILL BE CUT OFF. [0:9]. THE PROCESS CONTINUES 
# FOR INPUTTING THE POSITION [11:21] ADMIN RIGHTS [22:31] AND THEIR HOURS [32:] ONCE ALL THE DATA 
# IS COLLECTED FROM THE USER, THE PROGRAM WILL APPEND A LINE TO THE DATABASE WITH THE NEW DATA.
#
#
# REWRITTEN AS A FUNCTION: REMOVED SEVERAL PRINT STATEMENTS AND ADDED REQURIEMENT FOR ONE ARGUEMENT
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#import Filesearch Function
#DEFINE
from FileSearch import nameInEmployees
from logMe import logMe
logMe(str("<Addto> BEGIN."))
def check_input(input):
    #ERROR CATCHING 
    try:
        val = int(input)
        print("Input accepted")
        return True
    except ValueError:
        print("Input Not accepted. Not a number.")
        return False

#--------------

#begin 'add to records' function
def AddToRecords(inputname):
    logMe(str("<Addto> BEGIN."))
    #before you do anything, is this name in the database already?
    if (nameInEmployees(inputname)):
        print("Can not add due to <DUPLICATE ERROR>")
        logMe(str("<Addto> <DUPLICATE ERROR>"))
        return
    else:

        #open the text files
        employeerecords = open("Employees.txt", "a")
        passwordrecords = open("Passwords.txt", "a")
        #ask for input
        #answer = input("Would you like to add a new user? ")
        #make sure that the input is lower case for matching purposes
        #answer = answer.lower()

        #The following section of code is to make sure that the user's input 
        #Fits the criteria of the database.
        # Is the answer yes or y?
        answer = "yes";
        if ((answer == "y") or (answer == "yes")):
            #[inputname] is the name of the arguement included in the function call
            inputname = inputname.lower();
            print("The name entered will be: '", inputname,"'")
            #Accept in put for the position
            position = input("Please enter their position ")
            position = position.lower();
            #Check to make sure that the inpout is less thn 11 characters long.
            if (len(position) > 11):
                #if the input is too long, warn the user
                position = input("That name is too long. You only get 10 characters. Try again. ")
                #If the input is too long again then the user gets one more warning
                if (len(position) > 11):
                    #if the input is STILL too long then the user's input will be included in the database
                    #But only the first 11 characters
                    position = input("That name is still too long. One more try. Make sure it's shorter than 10 characters or it will be cut short.")
                    if (len(position) > 11):
                        #this sets the [position] variable to the first 10 characters of the user's input
                        #then prints the input
                        position = position[0:10]
                        print("The position entered will be:", position)
            #Is the input user going to need admin rights
            adminrights = input("Are they an admin?: ")
            #Flag used to break the [while] loop below
            adminflag = 0
            while (adminflag == 0):
                #makes sure that [adminrights] is a string
                str(adminrights)
                #lower case the input for input varification purposes
                adminrights = adminrights.lower()
                #If 'y'or 'yes' make them an admin and break the loop
                if (adminrights == "y") or (adminrights == "yes"):
                    adminrights = "Admin"
                    adminflag = 1
                #If 'n' or 'no' make them a team member and break the loop
                elif(adminrights == "no") or (adminrights == "n"):
                    adminrights = "Team"
                    adminflag = 1
                else:
                    #if the input is invalid, notify the user and loop
                    adminrights = input("Please enter yes or no.")
                    adminflag = 0
            #Accept input from the user for the number of hours that they have worked    
            totalhours = input("Have they worked any hours yet? ")
            #flag used to break the loop 
            hoursflag = 0

            while (hoursflag == 0):
                #checks to  make sure that the user's input is a number
                #If it is then it breaks the loop
                #if not then loop continuously
                if(check_input(totalhours)):
                    totalhours = totalhours
                    hoursflag = 1
                else:
                    totalhours = input("Please enter a number: ")
                    hoursflag = 0
            #select a 4 character password for the new user
            #anything created that is longer than 5 characters will be cut off.
            pswrd = input("Please enter a 4 character password for this new user: ")
            pswrd = pswrd[0:4]
            # print("::",pswrd,"::")
            # print("::",pswrd[0],"::")
            # print("::",pswrd[1],"::")
            # print("::",pswrd[2],"::")
            # print("::",pswrd[3],"::")
            
            #Take the fractured pieces of the user's input and write them to the database in pieces
            #add check the length of the name for the space counter
            spacecounter = 11 - len(inputname)
            #Write the name to the employee records database
            employeerecords.write("\n")
            employeerecords.write(inputname)
            #write the name to the Passwords database
            passwordrecords.write("\n")
            passwordrecords.write(inputname)
            #input the correct number of spaces to fill out the database
            for x in range(spacecounter):
                employeerecords.write(" ")
                passwordrecords.write(" ")
            #Write the employee's position to the passwords database and the Employee Database
            employeerecords.write(position)
            #count and write the number of spaces necessary for the position
            spacecounter = 11 - len(position)
            for x in range(spacecounter):
                employeerecords.write(" ")
            #write out admin rights then write out the spaces to fill the block for admin rights
            employeerecords.write(adminrights)
            spacecounter = 10 - len(adminrights)
            for x in range(spacecounter):
                employeerecords.write(" ")
            employeerecords.write(totalhours)
            passwordrecords.write(pswrd)

            #Confirm that the process has completed
            print("input added to the database")
            logMe(str("<Addto> New user added to the Database."))
            logMe(str("<Addto> " + inputname))
        #print if user types 'no' when asked if they would like to add a user.
        else:
            print()
            # print("==========")
            # print("RETURNING")
            # print("==========")
            # print()
        #closes all the opened text files
        employeerecords.close()
        passwordrecords.close()
        #return
        logMe(str("<Addto> END."))
        return;