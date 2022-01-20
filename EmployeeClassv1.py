import time
class Employee:
    #Initialize class
    def __init__(self, name, position, department, totalhours):
        self.name = name
        self.position = position
        self.department = department
        self.totalhours = totalhours
        return
    #___________________________________________________________________
    #-------------------------------------------------------------------
    #---------------------getters and setters---------------------------
    def setName(self, x):
        self.name = x
        return
    
    def getName(self, x):
        x = self.name
        return x

    def setPosition(self, x):
        self.position = x
        return x
    
    def getPosition(self, x):
        x = self.position
        return x
    
    def setdepartment(self, x):
        self.department = x
        return x
    
    def getdepartment(self, x):
        x = self.department
        return x

    def setHours(self, x):
        self.hours = x
        return x
    
    def getHours(self, x):
        x = self.hours
        return x
    
    #-----------------end getters and setters---------------------------
    #-------------------------------------------------------------------
    #___________________________________________________________________


def main():
    
    print("Begin class test")
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
    f = open("employees", "r")


    print("Done for now")
    print("---------")

    return
main()