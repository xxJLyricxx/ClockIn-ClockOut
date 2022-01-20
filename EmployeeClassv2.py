import time
import os
def remove(string):
    return string.replace(" ", "")

class Employee:
    #Initialize class
    def __init__(self, name, position, department, totalhours):
        self.name = name
        self.position = position
        self.department = department
        self.totalHours = totalhours
        return
    #___________________________________________________________________
    #-------------------------------------------------------------------
    #---------------------getters and setters---------------------------
    def setName(self, x):
        self.name = x
        return
    
    def getName(self):
        x = self.name
        return x

    def setPosition(self, x):
        self.position = x
        return x
    
    def getPosition(self):
        x = self.position
        return x
    
    def setdepartment(self, x):
        self.department = x
        return x
    
    def getdepartment(self):
        x = self.department
        return x

    def setHours(self, x):
        self.hours = x
        return x
    
    def getHours(self):
        x = self.totalHours
        return x
    
    #-----------------end getters and setters---------------------------
    #-------------------------------------------------------------------
    #___________________________________________________________________


def main():
    
    print("EmployeeClassv2Start")
    #Test creating an Employee ------------------------------------------ Successful
    #print("create an employee")
    #x = Employee("John", "cashier", "admin", 0)
    #y = x.name
    #print(y)
    #print()
    #y = x.department
    #print(y)
    #print()
    #---------------------------------------------------------------------


    #print("---------------begin phase 2--------------")
    #print("-----------------create array-------------")
    #team = []
    #for i in range(10):
    #    testData = Employee("John", "Cashier2", "admin", i)
    #    team.append(testData)
    #    print("added employee number ", i)
    #    time.sleep(1)

    #print("---------------begin phase 3--------------")
    #print("----------------Read the document---------")
    #print("Attempting to open 'read' document")
    f = open("C:/Users/davisgj/Desktop/Python Files/Employee Time Project/EmployeeProject/Employees.txt", "r")
    #print("Document opened")
    #print(f)
    print()
    
    team = []
    i=0
    q = 0                                                       #This is just a flag                                                                                      
    while (q != 1):
        testData = Employee(remove(f.readline(11)),remove(f.readline(11)),remove(f.readline(10)), remove(f.readline(5)))
        if (testData.getName() == ""):
            q = 1
            break
        team.append(testData)
        '''
        print("added employee number ", i)
        print("Name: ", testData.getName())
        print("Position: ", testData.getPosition())
        print("Admin?: ", testData.getdepartment())
        print("Hours: ", testData.getHours())
        time.sleep(0.1)
        '''
        i+=1
        if (testData.getName() == ""):
            q = 1
        
    #selection = team[0].getName()
    #print(team[19].getHours())
    f.close()
    #print("Done for now")
    print("---------")
    print("EmployeeClassv2 End")
    print("---------")
    #f.close()

    return
main()