#---------------------------------------------------
#initialize
#---------------------------------------------------

print("Which would you like to change? ")
print("1 Username")
print("2 Password")
print("3 Admin Rights")
print("4 Position")
print("5 Hours")
d = input("Input: ")

#flags fo validating user input
inputflag = 0
foundit = 0

#Check to make sure that the input is one of the numbers available.
while (inputflag == 0):
    if (d == "1") or (d =="2") or (d =="3") or (d=="4") or (d=="5"):
        inputflag = 1
        #if its true:
        #do the thing
        

        #------------------------------------------------------------------------------------------------------------------------------
        #-------------------------------------------change name------------------------------------------------------------------------
        #------------------------------------------------------------------------------------------------------------------------------

        #if the value entered was one;
        #change the name of one of the entries

        if (d == "1"):
            dd = input("Which would you like to change? ")
            dd = dd.lower()
            #open the doucment as readable
            with open("C:/Users/davisgj/Desktop/Python Files/Employee Time Project/EmployeeProject/test2.txt", "r") as f:
                #store the document in 'lines'
                lines = f.readlines()
                #iterate through each line of the list searching for the name that you want to change
                for line in lines:
                    #found it!
                    if(line.__contains__(dd)):
                        print("username found")
                        foundit = 1
                        ddd = input("What woud you like to change it to?")

                        #check to make sure that the name is within 10 characters

                        lengthflag = 0
                        while (lengthflag == 0):
                            if (len(ddd) > 10):
                                print("That name is too long. Enter a name shorter than 10 characters.")
                                ddd = input("Try Again: ")
                            else:
                                lengthflag = 1

                        #set up the space counter to fill in spaces when a name has fewer than 10 characters
                        newnamelen = len(ddd)
                        spacecounter = 10 - newnamelen

                        #-------------
                        #Close the other instances of the document
                        f.close()
                        #open the doucment as readable so that it can be added to 'lines'
                        with open("C:/Users/davisgj/Desktop/Python Files/Employee Time Project/EmployeeProject/test2.txt", "r") as f:
                            lines = f.readlines()
                        #open the document as writable so that we can add the new input to it
                        with open("C:/Users/davisgj/Desktop/Python Files/Employee Time Project/EmployeeProject/test2.txt", "w") as f:
                            for line in lines:
                                #//print(line)
                                #if the line that we're about to print contains the value typed in,
                                #don't write anything. If not, then write the line.
                                if (line.__contains__(dd)):
                                    holdline = line
                                    f.write("")
                                else:
                                    f.write(line)
                        #-------------
                        #Now that the old record is removed,
                        #Write the new line at the bottom of the database

                        #close the other open instances of the database for ram purposes
                        f.close()
                        #reopen as an ammendable document
                        with  open("C:/Users/davisgj/Desktop/Python Files/Employee Time Project/EmployeeProject/test2.txt", "a") as f:
                            #new line
                            f.write("\n")
                            #new name
                            f.write(ddd)
                            #spaces if necessary
                            for x in range(spacecounter):
                                f.write(" ")
                            #Print the rest of the line that isn't being changed
                            f.write(holdline[10:])
                            #close the document.
                            #all done!
                            f.close()
                            print("All Done!")
                            
                #if the combination of characters isn't found in the database print this
                if (foundit == 0):
                    print("Does not exist in the database.")
        #---------------------------------------------------------------------------------------------------------------------------------------------------
        #-----------------------------------------------change password---------------------------------------------------------------------------------------
        #----------------------------------------------------------------------------------------------------------------------------------------------
        elif (d == "2"):
            dd = input("Which would you like to change? ")
            dd = dd.lower()
            #open the doucment as readable
            with open("C:/Users/davisgj/Desktop/Python Files/Employee Time Project/EmployeeProject/passwordtest.txt", "r") as f:
                #store the document in 'lines'
                lines = f.readlines()
                #iterate through each line of the list searching for the name that you want to change
                for line in lines:
                    #found it!
                    if(line.__contains__(dd)):
                        print("username found")
                        foundit = 1
                        ddd = input("What would you like to change the password to?")

                        #check to make sure that the password is within 4 characters

                        lengthflag = 0
                        while (lengthflag == 0):
                            if (len(ddd) > 4):
                                print("That password is too long. Enter a password that is 4 characters.")
                                ddd = input("Try Again: ")
                            else:
                                lengthflag = 1

                        #set up the space counter to fill in spaces when a name has fewer than 10 characters
                        newpasswordlen = len(ddd)
                        spacecounter = 4 - newpasswordlen

                        #-------------
                        #Close the other instances of the document
                        f.close()
                        #open the doucment as readable so that it can be added to 'lines'
                        with open("C:/Users/davisgj/Desktop/Python Files/Employee Time Project/EmployeeProject/passwordtest.txt", "r") as f:
                            lines = f.readlines()
                        #open the document as writable so that we can add the new input to it
                        with open("C:/Users/davisgj/Desktop/Python Files/Employee Time Project/EmployeeProject/passwordtest.txt", "w") as f:
                            for line in lines:
                                #//print(line)
                                #if the line that we're about to print contains the value typed in,
                                #don't write anything. If not, then write the line.
                                if (line.__contains__(dd)):
                                    holdline = line
                                    f.write("")
                                else:
                                    f.write(line)
                        #-------------
                        #Now that the old record is removed,
                        #Write the new line at the bottom of the database

                        #close the other open instances of the database for ram purposes
                        f.close()
                        #reopen as an ammendable document
                        with  open("C:/Users/davisgj/Desktop/Python Files/Employee Time Project/EmployeeProject/passwordtest.txt", "a") as f:
                            #new line
                            f.write("\n")
                            #new name
                            f.write(holdline[0:10])
                            f.write(ddd)
                            #spaces if necessary
                            for x in range(spacecounter):
                                f.write(" ")
                            #Print the rest of the line that isn't being changed
                            #f.write(holdline[10:])
                            #close the document.
                            #all done!
                            f.close()
                            print("All Done!")
                            
                #if the combination of characters isn't found in the database print this
                if (foundit == 0):
                    print("Does not exist in the database.")


            #-------------------------------------------------------------------------------------------------------------------------------------------
            #-------------------------------------------------------end change password-----------------------------------------------------------------
            # ----------------------------------------------------begin admin change-----------------------------------------------------------------
            #-------------------------------------------------------------------------------------------------------------------------------------------

        elif (d == "3"):
            dd = input("Which would you like to change? ")
            dd = dd.lower()
            #open the doucment as readable
            with open("C:/Users/davisgj/Desktop/Python Files/Employee Time Project/EmployeeProject/test2.txt", "r") as f:
                #store the document in 'lines'
                lines = f.readlines()
                #iterate through each line of the list searching for the name that you want to change
                for line in lines:
                    #found it!
                    if(line.__contains__(dd)):
                        print("username found")
                        foundit = 1
                        onetwocheck = 0
                        print("What would you like to change their rights to?")
                        while (onetwocheck == 0):
                            ddd = input("1 for team member or 2 for admin.")
                            #check to make sure that the position is a 1 or a 2
                            if (ddd == "1"):
                                ddd = "team"
                                onetwocheck = 1
                            elif(ddd =="2"):
                                ddd = "admin"
                                onetwocheck = 1
                            else:
                                print("Input not accepted.")
                                print("You must enter a 1 or a 2")
                        
                        #-------------
                        #Close the other instances of the document
                        f.close()
                        #open the doucment as readable so that it can be added to 'lines'
                        with open("C:/Users/davisgj/Desktop/Python Files/Employee Time Project/EmployeeProject/test2.txt", "r") as f:
                            lines = f.readlines()
                        #open the document as writable so that we can add the new input to it
                        with open("C:/Users/davisgj/Desktop/Python Files/Employee Time Project/EmployeeProject/test2.txt", "w") as f:
                            for line in lines:
                                #//print(line)
                                #if the line that we're about to print contains the value typed in,
                                #don't write anything. If not, then write the line.
                                if (line.__contains__(dd)):
                                    holdline = line
                                    f.write("")
                                else:
                                    f.write(line)
                        #-------------
                        #Now that the old record is removed,
                        #Write the new line at the bottom of the database

                        #close the other open instances of the database for ram purposes
                        f.close()
                        #reopen as an ammendable document
                        with  open("C:/Users/davisgj/Desktop/Python Files/Employee Time Project/EmployeeProject/test2.txt", "a") as f:
                            #new line
                            f.write("\n")
                            #new name
                            f.write(holdline[0:22])
                            f.write(ddd)
                            #spaces if necessary
                            if (ddd == "admin"):
                                f.write("    ")
                            else:
                                f.write("     ")
                            f.write(holdline[31:])
                            #for x in range(spacecounter):
                            #    f.write(" ")
                            #Print the rest of the line that isn't being changed
                            #f.write(holdline[10:])
                            #close the document.
                            #all done!
                            f.close()
                            print("All Done!")
                            
                #if the combination of characters isn't found in the database print this
                if (foundit == 0):
                    print("Does not exist in the database.")
            #--------------------------------------------------------------------------------------------------------------------------------------------
            #-----------------------------------------------end admin rights / begin position change-----------------------------------------------------
            #--------------------------------------------------------------------------------------------------------------------------------------------


        elif (d == "4"):
            dd = input("Which would you like to change? ")
            dd = dd.lower()
            #open the doucment as readable
            with open("C:/Users/davisgj/Desktop/Python Files/Employee Time Project/EmployeeProject/test2.txt", "r") as f:
                #store the document in 'lines'
                lines = f.readlines()
                #iterate through each line of the list searching for the name that you want to change
                for line in lines:
                    #found it!
                    if(line.__contains__(dd)):
                        print("username found")
                        foundit = 1
                        lencheck = 0
                        ddd = input("What would you like to change their position to?")
                        while (lencheck == 0):
                            if (len(ddd) > 11):
                                print("Input not accepted.")
                                ddd = input("Please enter a position that has less than 11 characters: ")
                            else:
                                lencheck = 1
                        
                        
                        #-------------
                        #Close the other instances of the document
                        f.close()
                        #open the doucment as readable so that it can be added to 'lines'
                        with open("C:/Users/davisgj/Desktop/Python Files/Employee Time Project/EmployeeProject/test2.txt", "r") as f:
                            lines = f.readlines()
                        #open the document as writable so that we can add the new input to it
                        with open("C:/Users/davisgj/Desktop/Python Files/Employee Time Project/EmployeeProject/test2.txt", "w") as f:
                            for line in lines:
                                #//print(line)
                                #if the line that we're about to print contains the value typed in,
                                #don't write anything. If not, then write the line.
                                if (line.__contains__(dd)):
                                    holdline = line
                                    f.write("")
                                else:
                                    f.write(line)
                        #-------------
                        #Now that the old record is removed,
                        #Write the new line at the bottom of the database

                        #close the other open instances of the database for ram purposes
                        f.close()
                        #reopen as an ammendable document
                        with  open("C:/Users/davisgj/Desktop/Python Files/Employee Time Project/EmployeeProject/test2.txt", "a") as f:
                            #new line
                            f.write("\n")
                            #new name
                            f.write(holdline[0:11])
                            f.write(ddd)
                            #spaces if necessary
                            spacecounter = 10 - len(ddd)
                            for x in range(spacecounter):
                                f.write(" ")
                            f.write(holdline[21:])
                            #for x in range(spacecounter):
                            #    f.write(" ")
                            #Print the rest of the line that isn't being changed
                            #f.write(holdline[10:])
                            #close the document.
                            #all done!
                            f.close()
                            print("All Done!")
                            
                #if the combination of characters isn't found in the database print this
                if (foundit == 0):
                    print("Does not exist in the database.")

        #------------------------------------------------------------------------------------------------------------------------------------------------------------
        # ----------------------------------------------------end position / begin hours ----------------------------------------------------------------------------
        # --------------------------------------------------------------------------------------------------------------------------------------------------------------
        elif (d == "5"):
            print("Input accepted. Beginning Hours change.")
            changename= input("What is the name of the person you would like to change the hours of: ")
            changename = changename.lower()
            #open the doucment as readable
            with open("C:/Users/davisgj/Desktop/Python Files/Employee Time Project/EmployeeProject/test2.txt", "r") as f:
                #store the document in 'lines'
                lines = f.readlines()
                #iterate through each line of the list searching for the name that you want to change
                for line in lines:
                    #found it!
                    if(line.__contains__(changename)):
                        print("username found")
                        foundit = 1
                        inputflag = 0
                        #*************************************************************************
                        #
                        #subsection - found entry
                        #
                        #*************************************************************************
                        lencheck = 0
                        while (inputflag == 0):
                            print("-----------------------------------")
                            print("What would you like to do?")
                            print("1. Add hours(Coming Soon!)")
                            print("2. Subtract hours(Coming Soon!)")
                            print("3. Edit Hours")
                            print("4. Reset Hours")
                            print("-----------------------------------")
                            newhourssel = input("Input: ")
                            if(newhourssel == "1"):
                                print("input received: add hours")
                                print("this feature is coming soon! But is not ready yet...")
                                print("Please select from one of the other options.")
                            elif(newhourssel == "2"):
                                print("input recieved: subtract hours")
                                print("this feature is coming soon! But is not ready yet...")
                                print("Please select from one of the other options.")
                            elif(newhourssel == "3"):
                                inputflag = 1
                                print("Input accepted: Edit hours")
                                #print("Bucha code incoming....")
                                #************************opportunity******************
                                #how do I print the person's name here inside of the "input statement"'s question
                                #Example: "What would you like to change NOAH'S hours to?"
                                newhours = input("What you you like to change this person's hours to?: ")
                                #******************opportunity**************
                                #validate numerical input 
                                try:
                                    int(newhours)
                                    it_is = True
                                
                                except ValueError:
                                    it_is = False
                                
                                print("Input is a a number?: ", it_is)
                                if (it_is == False):
                                    print("[force numerical input function coming soon.]")
                                    print("[for now this input will be added to the database either way.]")
                                #close everything just in case
                                f.close()
                                #open up only what we need
                                #open the doucment as readable so that it can be added to 'lines'
                                with open("C:/Users/davisgj/Desktop/Python Files/Employee Time Project/EmployeeProject/test2.txt", "r") as f:
                                    lines = f.readlines()
                                #open the document as writable so that we can add the new input to it
                                with open("C:/Users/davisgj/Desktop/Python Files/Employee Time Project/EmployeeProject/test2.txt", "w") as f:
                                    for line in lines:
                                        #//print(line)
                                        #if the line that we're about to print contains the value typed in,
                                        #don't write anything. If not, then write the line.
                                        if (line.__contains__(changename)):
                                            holdline = line
                                            f.write("")
                                        else:
                                            f.write(line)
                                
                                #-------------
                                #Now that the old record is removed,
                                #Write the new line at the bottom of the database
                                        #close the other open instances of the database for ram purposes
                                f.close()
                                #reopen as an ammendable document
                                with  open("C:/Users/davisgj/Desktop/Python Files/Employee Time Project/EmployeeProject/test2.txt", "a") as f:
                                    #new line
                                    f.write("\n")
                                    #new name
                                    f.write(holdline[0:32])
                                    f.write(newhours)
                                    f.close()
                                    print("All Done!")

                                #buncha code here
                            elif(newhourssel == "4"):
                                inputflag = 1
                                print("Input accepted: Reset hours")
                                print("Construction in process")
                                print("This person's total hours for now is: ",line[32:])
                                yesorno = input("Are you sure you want to change it? (y/n): ")
                                yornflag = 0
                                while (yornflag == 0):
                                    if (yesorno == 'y') or (yesorno == 'n'):
                                        yornflag = 1
                                        print("Input accepted: changing hours to zero.")
                                    else:
                                        yesorno = input("Input not accepted! Please enter 'y' or 'n': ")
                                #begin Rewriting database from the top
                                f.close()
                                if(yesorno == 'y'):
                                    #if the response to "are you sure" was yes, then rewrite the database.
                                    with open("C:/Users/davisgj/Desktop/Python Files/Employee Time Project/EmployeeProject/test2.txt", "r") as f:
                                        lines = f.readlines()
                                    #open the document as writable so that we can add the new input to it
                                    with open("C:/Users/davisgj/Desktop/Python Files/Employee Time Project/EmployeeProject/test2.txt", "w") as f:
                                        for line in lines:
                                            #//print(line)
                                            #if the line that we're about to print contains the value typed in,
                                            #don't write anything. If not, then write the line.
                                            if (line.__contains__(changename)):
                                                holdline = line
                                                f.write("")
                                            else:
                                                f.write(line)
                                    
                                    #-------------
                                    #Now that the old record is removed,
                                    #Write the new line at the bottom of the database
                                            #close the other open instances of the database for ram purposes
                                    f.close()
                                    #reopen as an ammendable document
                                    with  open("C:/Users/davisgj/Desktop/Python Files/Employee Time Project/EmployeeProject/test2.txt", "a") as f:
                                        #new line
                                        f.write("\n")
                                        #new name
                                        f.write(holdline[0:32])
                                        f.write("0")
                                        f.close()
                                        print("All Done!")
                                else:
                                    #input was 'n' so do nothing
                                    print("Input received")
                                    print("No changes made")
                                    print("Update cancelled.")

                                
                                #buncha code here
                            else:
                                print("------------------------------------")
                                print("That input is not valid.")
                                print("Please select one of the above options.")
                                print("------------------------------------")

                            


                        #*************************************************************************
                        #
                        #End Subsection
                        #
                        #*************************************************************************

                #if the combination of characters isn't found in the database print this
                if (foundit == 0):
                    print("Does not exist in the database.")



        #------------------------------------------------------------------------------------------------------------------------------------------------------------
        # ----------------------------------------------------end position / begin hours ----------------------------------------------------------------------------
        # --------------------------------------------------------------------------------------------------------------------------------------------------------------

    #If the input isn't valid let the user know and end
    else:
        print("Input not accepted. Try again")
        print("-------------------------------------------------------")
        d = input("Input: ")

#recycled code
#-----------------------------
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
#-----------------------------
