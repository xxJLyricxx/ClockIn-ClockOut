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
currentusername = input("Please enter your username:")
print("--------")
print("Processing")
print("--------")
with open("C:/Users/davisgj/Desktop/Python Files/Employee Time Project/EmployeeProject/Passwords.txt", "r") as u:
    lines = u.readlines()
    founditflag = 0
    #iterate through each line of the list searching for the name that you want to change
    for line in lines:
        #found it!
        if(line.__contains__(currentusername)):
            print("username found")
            passline = line[11:15]
            founditflag = 1
            u.close()
    if (founditflag == 0):
        print("Username not found in database")
        AddToRecords(currentusername)
    if (founditflag == 1):
        passwordinput = input("Please enter your password: ")
        print(passline)
        if (passline == passwordinput):
            print("Password match")
        else:
            print("Password doesn't match")

print("FIN")