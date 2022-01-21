import EmployeeClassv2
#import Password
from EmployeeClassv2 import Employee
from EmployeeClassv2 import remove
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

f = open("C:/Users/davisgj/Desktop/Python Files/Employee Time Project/EmployeeProject/test.txt", "a")
logdoc = open("C:/Users/davisgj/Desktop/Python Files/Employee Time Project/EmployeeProject/test2.txt", "a")
employeerecords = open("C:/Users/davisgj/Desktop/Python Files/Employee Time Project/EmployeeProject/Employees.txt", "a")
passwordrecords = open("C:/Users/davisgj/Desktop/Python Files/Employee Time Project/EmployeeProject/Passwords.txt", "a")
#f.write("0123456789012345678901234567890")
#f.write("\n")
answer = input("Would you like to add a new user? ")
answer = answer.lower()
if ((answer == "y") or (answer == "yes")):
    name = input("Please enter their name: ")
    if (len(name) > 10):
        name = input("That name is too long. You only get 10 characters. Try again. ")
        if (len(name) > 10):
            name = input("That name is still too long. One more try. Make sure it's shorter than 10 characters or it will be cut short.")
            if (len(name) > 10):
                name = name[0:9]
                print("The name entered will be: ", name)
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
        adminrights = adminrights.lower()
        if (adminrights == "y") or (adminrights == "yes"):
            adminrights = "Admin"
            adminflag = 1
        elif(adminrights == "no") or (adminrights == "n"):
            adminrights = "Team"
            adminrights = 1
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
    pswrd = pswrd[0:3]
    
    

    spacecounter = 11 - len(name)
    #print(spacecounter)
    employeerecords.write("\n")
    employeerecords.write(name)
    passwordrecords.write(name)
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
    print("okay then")
f.close()
logdoc.close()
employeerecords.close()
passwordrecords.close()