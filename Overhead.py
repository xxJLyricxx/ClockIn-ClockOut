#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# PROGRAM NAME: overhead.py
# AUTHOR: GARY DAVIS
# DATE: 1/28/2022
# DESCRIPTION: This is an overhead program that will utilize functions that perform the same actions that the earlier written programs
# do. The purpose of this program is to be the front of the program that users actually interact with instead of the individual pieces.
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#
#
#Start defining programs
from re import U
from AddToRecordsEdit import AddToRecords 
def remove(string):
    return string.replace(" ","")

currentusername = input("Please enter your username:")
print("--------")
print("Processing")
print("--------")
with open("C:/Users/davisgj/Desktop/Python Files/Employee Time Project/EmployeeProject/Passwords.txt", "r") as passdatabase:
    lines = passdatabase.readlines()
    founditflag = 0
    #iterate through each line of the list searching for the name that you want to change
    for line in lines:
        #found it!
        if(line.__contains__(currentusername)):
            print("username found")
            passlinewhole = line
            passline = line[11:15]
            founditflag = 1
            passdatabase.close()
    if (founditflag == 0):
        print("Username not found in database")
        AddToRecords(currentusername)
    if (founditflag == 1):
        passwordinput = input("Please enter your password: ")
        print(passline)
        if (passline == passwordinput):
            #correct input
            #begin processing the rest of the functions
            print("Password match")
            #open the employee database to find user name, position and hours worked.
            with open("C:/Users/davisgj/Desktop/Python Files/Employee Time Project/EmployeeProject/Employees.txt", "r") as employeedatabase:
                #do the thing
                print("-----begin new section------")
                print()
                lines = employeedatabase.readlines()
                for line in lines:
                    print(line)
                    if(line.__contains__(currentusername)):
                        currentdataline = line
                print("the employee's name is: ", currentdataline[0:10])
                print("The Employees position is: ", currentdataline[11:20])
                print("The Employees Rights are: ", currentdataline[21:30])
                print("the employees hours are: ", currentdataline[31:])
                print()
                employeename = currentdataline[0:10]
                employeeposition = currentdataline[11:20]
                employeerights = currentdataline[22:30]
                employeehours = currentdataline[32:]
                print(":::",employeename,":::")
                remove(employeename)
                x = 0
                while (x < len(employeename)):
                    print("----", employeename, "----")
                    if (employeename[x] == " "):
                        employeename[x].replace(" ","",1)
                        print(x)
                        print(employeename[x])
                    x += 1
                print("::::", employeename,":::")
                print(":::",employeeposition,":::")
                print(":::",employeerights,":::")
                print(":::",employeehours,":::")
                print("-----end new section-----")
            print(currentusername)

        else:
            print("Password doesn't match")

print("FIN")