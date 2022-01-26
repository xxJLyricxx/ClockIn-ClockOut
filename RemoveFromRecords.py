#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# PROGRAM NAME: RemoveFromRecords.py
# AUTHOR: GARY DAVIS
# DATE: 1/20/2022
# DESCRIPTION: THIS PROGRAM IS RELATIVELY SIMPLE... AND SHORT. IT STARTS UP, ASKS FOR AN INPUT FROM THE USER, TAKES THAT INPUT AND SEARCHES
# THROUGH THE DATABASE AND ERASES THE LINE THAT CONTAINS THE VALUE OF THE INPUT. WHEN FINISHED 
# 
# 
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
from operator import contains
d = input("Which line would you like to delete? ")
d = d.lower()
foundit = 0
with open("C:/Users/davisgj/Desktop/Python Files/Employee Time Project/EmployeeProject/test2.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        if (line.__contains__(d)):
            foundit = 1
    if (foundit==1):
        print("found it!")
    else:
        print("Does not exist in the database")

with open("C:/Users/davisgj/Desktop/Python Files/Employee Time Project/EmployeeProject/test2.txt", "w") as f:
    for line in lines:
        #print(line)
        if (line.__contains__(d)):
            f.write("")
            print("**deleted**")
        else:
            f.write(line)

f.close()