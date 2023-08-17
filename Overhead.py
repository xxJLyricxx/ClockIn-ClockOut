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
#
import time
#"from re import U" is short for "regular expressions"
from logMe import logMe
from re import U
from AddToRecordsEdit import AddToRecords
from RemoveFromRecordsEdit import DeleteRecord
from EditRecordsEdit import  EditRecords
def remove(string):
    return string.replace(" ","")

def updatehours(name, hours):
    hours = str()
    with open("Employees.txt", "r") as f:
        lines = f.readlines()
        #open the document as writable so that we can add the new input to it
        with open("Employees.txt", "w") as f:
            for line in lines:
                #if the line that we're about to print contains the value typed in,
                #don't write anything. If not, then write the line.
                if (line.__contains__(name)):
                    holdline = line
                    f.write("")
                else:
                    f.write(line)
        #-------------
        #Now that the old record is removed,
        #Write the new line at the bottom of the database
        #close the other open instances of the database for ram purposes
            f.close()
        #reopen as an appendable document
        with  open("Employees.txt", "a") as f:
            #new line
            f.write("\n")
            #new name
            f.write(holdline[0:32])
            f.write(hours)
            f.close()
            print("Database Updated!")
    return
            
            


currentusername = input("Please enter your username:")
print("--------")
print("Processing")
logMe(str("Login attempted: " + currentusername))
print("--------")
usernamecounter = 0;
currentusername = currentusername.lower()
with open("Passwords.txt", "r") as passdatabase:
    lines = passdatabase.readlines()
    founditflag = 0
    #iterate through each line of passwords.txt
    for line in lines:
        if(line.__contains__(currentusername)):
            usernamecounter += 1;
            time.sleep(1)
            foundname = line[0:10]
            foundname = foundname.replace(" ","")
            if (foundname == currentusername):
                #found an exact match
                passline = line[11:15]
                founditflag = 1
                passdatabase.close()
                break
            else:
                #did not find a match. keep going
                continue
    #Username not found in database
    #print(usernamecounter)        
    if (founditflag == 0):
        print("Username not found in database")
        continueyesno = input("Would you like to add that name to the database?: ")
        if (continueyesno == 'yes' or continueyesno =='y'):
            AddToRecords(currentusername);
        else:
            logMe(str("Username " + currentusername + "not added to database."))
            pass;
    if (founditflag == 1):
        passwordinput = input("Please enter your password: ")
        #print(passline)
        print("--------")
        print("Checking password match...")
        print("--------")
        time.sleep(1)
        if (passline == passwordinput):
            #correct input
            #begin processing the rest of the functions
            print("Password match")
            logMe(str("<OVHD> LOGIN SUCCESSFUL - " + currentusername))
            #open the employee database to find user name, position and hours worked.
            with open("Employees.txt", "r") as employeedatabase:
                #do the thing
                #print("-----begin new section------")
                #print(line)
                lines = employeedatabase.readlines()
                for line in lines:
                    #print(line)
                    if(line.__contains__(currentusername)):
                        currentdataline = line
                        #print("<",currentdataline,">")
                        employeename = currentdataline[0:10]
                        employeename = employeename.replace(" ","")
                        if (employeename == foundname):
                            break
                        else:
                            continue
                '''
                print("the employee's name is: ", currentdataline[0:10])
                print("The Employees position is: ", currentdataline[11:20])
                print("The Employees Rights are: ", currentdataline[21:30])
                print("the employees hours are: ", currentdataline[31:])
                print()
                '''
                employeename = currentdataline[0:10]
                employeeposition = currentdataline[11:20]
                employeerights = currentdataline[22:30]
                employeehours = currentdataline[32:]
                
                employeename = remove(employeename)
                employeeposition = remove(employeeposition)
                employeerights = remove(employeerights)
                employeehours = remove(employeehours)
                employeehours = employeehours.replace("\n", "")
                
                print("the employee's name is: ", employeename)
                print("The Employees position is: ", employeeposition)
                print("The Employees Rights are: ", employeerights)
                print("the employees hours are: ", employeehours)
                employeehours = int(employeehours)
                
                employeerights = employeerights.lower();

                if (employeerights == "admin"):
                    print("This employee is an admin")
                    print("What would you like to do?")
                    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
                    print("1) Add New Employee")
                    print("2) Fire an employee")
                    print("3) Edit employee records")
                    print("4) Add hours")
                    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
                    sel = input("Input: ")
                    selflag = False
                    while (selflag == False):
                        if (sel=="1") or (sel=="2") or (sel=="3") or (sel=="4"):
                            selflag = True
                        else:
                            print("That input is not one of the options above.")
                            print("Please enter '1', '2', '3', or '4'")
                            time.sleep(1)
                            sel = input("Try again:")                    
                    if (sel == "1"):
                        newemp = input("What name would you like to add?: ")
                        logMe(str(currentusername + " -> <ENTER <ADDTO>> ->" + newemp))
                        AddToRecords(newemp)
                    elif (sel == "2"):
                        logMe(str(currentusername + " -> <ENTER <DELETE>>"))
                        DeleteRecord()
                    elif (sel == "3"):
                        logMe(str(currentusername + " -> <ENTER <EDIT>>"))
                        EditRecords()
                    elif(sel == "4"):
                        numhours = int(input("how many hours would you like to add?: "))
                        employeehours = employeehours + numhours
                        print(employeename, "now has a total hour count of", employeehours)
                        updatehours(employeename, employeehours)
                    
                else:
                    print("This employee is a team member")
                
        else:
            print("Password doesn't match")

print("FIN")
logMe(str(currentusername + " logged out."))