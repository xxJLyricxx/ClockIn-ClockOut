#Python exploration
#USet this program to accept an imput from the user
# once the input is accepted (Should be a route to a folder where the database can be stored),
#  use that file location to create a folder that will contain the databases

#****************LATER***************
#CHECK TO SEE IF THE FOLDER ALREADY CONTAINS THE DATABASE AND UPDATE IT INSTEAD OF CREATING A NEW ONE.


datalocation = input("Please enter the location of your database: ")
print(type(datalocation))
with open(datalocation, 'r') as f:
    print("Found it")
    f.close()
