from operator import contains
d = input("Which line would you like to delete? ")
with open("C:/Users/davisgj/Desktop/Python Files/Employee Time Project/EmployeeProject/test2.txt", "r") as f:
    lines = f.readlines()
with open("C:/Users/davisgj/Desktop/Python Files/Employee Time Project/EmployeeProject/test2.txt", "w") as f:
    for line in lines:
        print(line)
        if (line.__contains__(d)):
            f.write("")
        else:
            f.write(line)