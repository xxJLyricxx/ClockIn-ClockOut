#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# PROGRAM NAME: AddToRecords(edit).py
# AUTHOR: GARY DAVIS
# DATE: 1/21/2022
# DESCRIPTION: THIS PROGRAMS PURPOSE IS TO ADD ENTRIES TO THE 'DATABASE' IN THIS CASE, THE DATABASE IS A TEXT FILE THAT IS SAVED IN THE SAME FOLDER
# AS THE PROGRAM ITSELF. THE TEXT FILE INCLUDES NAMES, JOBS, ADMIN RIGHTS (WRITTEN AS EITHER 'TEAM' OR 'ADMIN') AND THEIR COUNT OF HOURS. THERE ARE A LOT OR
# VALIDATOR LOOPS IN THIS PROGRAM. MOSTLY JUST TO MAKE SURE THAT THE CONVENTIONS FOR INPUTTING DATA REMAINS CONSISTANT WITH THE REST OF THE ENTRIES IN THE DATABASE.
# FIRST THE USER IS ASKED IF THEY WOULD LIKE TO ENTER A NEW USER. THE INPUT MUST BE 'Y' OR 'YES'. EITHER WILL WORK. THE INPUT IS [LOWER.()]'D JUST IN CASE. IF THERE IS
# *ANY* OTHER INPUT, THE PROGRAM WILL TERMINATE.
# IF THE INPUT IS ACCEPTED THEN THE USER WILL BE PROMPTED TO ADD A NAME. WHEN ADDING A NAME, IT CAN NOT BE MORE THAN 10 CHARACTERS. THE USER WILL BE PROMPED TO CHANGE THE NAME
# TO SOMETHING THAT IS LESS THAN 10 CHARACTERS 3 TIMES. IF THE USERS INPUT IS STILL LONGER THAN 10 CHARACTERS, THEIR INPUT WILL BE CUT OFF. [0:9].
# the process continues for inputting the position [11:21] admin rights [22:31] and their hours [32:]
# ONCE ALL THE DATA IS COLLECTED FROM THE USER, THE PROGRAM WILL APPEND A LINE TO THE DATABASE WITH THE NEW DATA.
#
#
# Rewritten a as a function
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

#import EmployeeClassv2
#import Password
#from EmployeeClassv2 import Employee
#from EmployeeClassv2 import remove
#---------------
def check_input(input):
    try:
        val = int(input)
        print("Input accepted")
        return True
    except ValueError:
        print("Input Not accepted. Not a number.")
        return False
#--------------
def AddToRecords(inputname):
    f = open("test.txt", "a")
    logdoc = open("test2.txt", "a")
    employeerecords = open("Employees.txt", "a")
    passwordrecords = open("Passwords.txt", "a")
    #f.write("0123456789012345678901234567890")
    #f.write("\n")
    answer = input("Would you like to add a new user? ")
    answer = answer.lower()
    if ((answer == "y") or (answer == "yes")):
        print("The name entered will be: '", inputname,"'")
        position = input("Please enter their position ")
        if (len(position) > 11):
            position = input("That name is too long. You only get 10 characters. Try again. ")
            if (len(position) > 11):
                position = input("That name is still too long. One more try. Make sure it's shorter than 10 characters or it will be cut short.")
                if (len(position) > 11):
                    position = position[0:10]
                    print("The position entered will be:", position)

        adminrights = input("Are they an admin?: ")
        adminflag = 0
        while (adminflag == 0):
            str(adminrights)
            print(type(adminrights))
            adminrights = adminrights.lower()
            if (adminrights == "y") or (adminrights == "yes"):
                adminrights = "Admin"
                adminflag = 1
            elif(adminrights == "no") or (adminrights == "n"):
                adminrights = "Team"
                adminflag = 1
            else:
                adminrights = input("Please enter yes or no.")
                adminflag = 0
            
        totalhours = input("Have they worked any hours yet? ")
        
        hoursflag = 0
        while (hoursflag == 0):
            if(check_input(totalhours)):
                totalhours = totalhours
                hoursflag = 1
            else:
                totalhours = input("Please enter a number: ")
                hoursflag = 0
        pswrd = input("Please enter a 4 character password for this new user: ")
        pswrd = pswrd[0:4]
        
        

        spacecounter = 11 - len(inputname)
        #print(spacecounter)
        employeerecords.write("\n")
        employeerecords.write(inputname)
        passwordrecords.write("\n")
        passwordrecords.write(inputname)
        for x in range(spacecounter):
            #print(x)
            employeerecords.write(" ")
            passwordrecords.write(" ")
        employeerecords.write(position)
        spacecounter = 11 - len(position)
        for x in range(spacecounter):
            employeerecords.write(" ")
        employeerecords.write(adminrights)
        spacecounter = 10 - len(adminrights)
        for x in range(spacecounter):
            employeerecords.write(" ")
        employeerecords.write(totalhours)
        passwordrecords.write(pswrd)

        print("input added to the database")

    else:
        print()
        print("==========")
        print("RETURNING")
        print("==========")
        print()
    f.close()
    logdoc.close()
    employeerecords.close()
    passwordrecords.close()
    return