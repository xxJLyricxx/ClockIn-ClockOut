print("Which would you like to change? ")
print("1 Username")
print("2 Password")
print("3 Position")
print("4 Admin rights")
print("5 Hours")
d = input("Input: ")
inputflag = 0
foundit = 0
while (inputflag == 0):
    if (d == "1") or (d =="2") or (d =="3") or (d=="4") or (d=="5"):
        inputflag = 1
        #do the thing
        if (d == "1"):
            dd = input("Which would you like to change? ")
            with open("C:/Users/davisgj/Desktop/Python Files/Employee Time Project/EmployeeProject/test2.txt", "r") as f:
                lines = f.readlines()
                for line in lines:
                    if(line.__contains__(dd)):
                        print("username found")
                        foundit = 1
                        ddd = input("What woud you like to change it to?")
                        lengthflag = 0
                        while (lengthflag == 0):
                            if (len(ddd) > 10):
                                print("That name is too long. Enter a name shorter than 10 characters.")
                                ddd = input("Try Again: ")
                            else:
                                lengthflag = 1
                        newnamelen = len(ddd)
                        spacecounter = 10 - newnamelen
                        #-------------
                        f.close()
                        with open("C:/Users/davisgj/Desktop/Python Files/Employee Time Project/EmployeeProject/test2.txt", "r") as f:
                            lines = f.readlines()
                        with open("C:/Users/davisgj/Desktop/Python Files/Employee Time Project/EmployeeProject/test2.txt", "w") as f:
                            for line in lines:
                                #print(line)
                                if (line.__contains__(dd)):
                                    holdline = line
                                    f.write("")
                                else:
                                    f.write(line)
                        #-------------
                        f.close()
                        with  open("C:/Users/davisgj/Desktop/Python Files/Employee Time Project/EmployeeProject/test2.txt", "a") as f:
                            f.write("\n")
                            f.write(ddd)
                            for x in range(spacecounter):
                                f.write(" ")
                            f.write(holdline[10:])
                            f.close()
                if (foundit == 0):
                    print("Does not exist in the database.")
    else:
        print("Input not accepted. Try again")
        print("-------------------------------------------------------")
        d = input("Input: ")
        
'''
with open("C:/Users/davisgj/Desktop/Python Files/Employee Time Project/EmployeeProject/test2.txt", "r") as f:
    lines = f.readlines()
with open("C:/Users/davisgj/Desktop/Python Files/Employee Time Project/EmployeeProject/test2.txt", "w") as f:
    for line in lines:
        print(line)
        if (line.__contains__(d)):
            f.write("")
        else:
            f.write(line)
            '''