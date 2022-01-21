import EmployeeClassv2
from EmployeeClassv2 import Employee
from EmployeeClassv2 import remove
print()
print("-------")
print("Password.py Start")
print("-------")
f = open("C:/Users/davisgj/Desktop/Python Files/Employee Time Project/EmployeeProject/Passwords.txt", "r")
q = 0                                                       #This is just a flag                                                                                      
i = 0

#------
#test--
#------
ff = remove(f.readline(10))
#print("The string is: ", ff)
#print(len(ff))
#print("The type is: ", type(ff))
qq = input("PLEASE ENTER YOUR USERNAME: ")
#print(qq)
qq = qq.lower()
#print(qq)
loopflag = 0
while (loopflag == 0):
    if (ff.__contains__(qq)):
        #print("yes")
        loopflag = 1
        ff = remove(f.readline())
        qq = input("Please enter the password: ")
        qq = qq.lower()
        if (ff.__contains__(qq)):
            print("Password matches!")
        else:
            print("Password does not match!")

    else:
        #print("no")
        #print("Reading more...")
        ff = f.readline()
       # print("_______________")
        #print(ff)
        #print("------there goes the password---------")
        ff = remove(f.readline(10))
        if (ff == ""):
            print("Not in the list")
            loopflag = 1
f.close()
print("fin password.py")