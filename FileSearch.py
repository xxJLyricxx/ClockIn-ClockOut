#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# PROGRAM NAME: FileSearch.py
# AUTHOR: GARY DAVIS
# DATE: 7/23/2023
# DESCRIPTION: THE PURPOSE OF THIS PROGRAM IS TO PROVIDE A SET OF FUNCTIONS TO BE CALLED IN OTHER FUNCTIONS THAT CAN BE UTILIZED TO SEARCH
# THE DIFFERENT FILES THAT ARE USED IN CLOCK IN CLOCK OUT. THIS PROGRAM WILL BE ABLE TO BE CALLED TO PROVE WHETHER OR NOT A STRING EXISTS IN
# PASSWORDS.TXT OR IN EMPLOYEES.TXT
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

#check if a name is in the employee database
def nameInEmployees(inputname):
    inputname = inputname.lower()
    #Open Employees.txt as readable file
    with open("Employees.txt", "r") as employeedatabase:
        #search the database
        lines = employeedatabase.readlines()
        foundItFlag = False;
        #Read a line
        for x in lines:
            if(x.__contains__(inputname)):
                #break out just the name
                foundname = x[0:10]
                #cut off all the spaces
                foundname = foundname.replace(" ","")
                #compare it to inputname
                if (foundname == inputname):
                    #found an exact match
                    #-=-=-=
                    #test
                    #-=-=-=
                    print("found the perfect match")
                    print(inputname, "<>", foundname)
                    foundItFlag = True;
                    break
                else:
                    continue
            else:
                continue
    employeedatabase.close()
    return foundItFlag;
#::TEST ME::
# exp = input("Please enter a name to test: ")
# if (nameInEmployees(exp)):
#     print("Found it")
# else:
#     print("Not found")
