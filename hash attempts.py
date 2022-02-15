#python code to demonstrate
#SHA has algorithms

#import the library
import hashlib
#create a string
name = 'GARY'
#this just prints the different hash libraries that come with the 'hashlib' imported library
print (hashlib.algorithms_guaranteed)
print('=-=-=-=-=-=-=-=-=-=')
#not sure what the 'encode()' function does in python.... not gonna lie
name.encode()
print("-=-=-=-=-=-=-=-=-=-=")
#this only prints 'bGARY'. havent found a use for this yet
print(name.encode())
print('-=-=-=-=-=-=-==')
print("")


#this will hash the string that has been input in to a SHA512 HASH.
#the output is raw data that is unique to this string's location in memory
result = hashlib.sha512(name.encode())
print("the hexidecimal equivbalent of SHA512 is: ")
print (result)
#          *~ THIS ~* IS the hex digest of the string once it is hashed. this is the value you're probably looking for.
# it can be used to check the hash of the value that is input and can be used to verify the input.
#if the hashes match then the input value is the same.
#this is notably different from just checking using the 'encode()' funtion or just checking the value of the output 'print(result)'
print("this is the hex digest")
print(result.hexdigest())

print ("\r")

print("-=-=-=-=-=-=-=-=")

#this is the test for validating the new input from the user by checking to see if the hashes match
#create a new string that's the same as the original
newname = 'GARY'
#create a new variable that is the hash of the string
newresult = hashlib.sha512(newname.encode())
#print what the result is. this will result in a bunch of letters and numbers that are the hex digest of the string that was encoded
print(newresult.hexdigest())

#this function simply checks to see if the hashes match.
#this works!
#this fucntion will also print the different memory values that show that these are two separate objects in memory.
if newresult.hexdigest() == result.hexdigest():
    print("These match")
    print(name)
    print(newname)
    print("=-=-=-=-=-=-=-=-=")
    print(result)
    print(newresult)
    print("-=-=-=-=-=-=-=-=-=")
else:
    print("These do NOT match")
    print(name)
    print(newname)
    print("=-=-=-=-=-=-=-=-=")
    print(result)
    print(newresult)
    print("-=-=-=-=-=-=-=-=-=")
print("-=-=-=-=-=-=-=")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=")
print("\r")
print("\r")
print("\r")
print("::::::::::::::::::::::::::::::BEGINNING NEW TESTING SECTION::::::::::::::::::::::::::::::::::::::::::::")
#next test
#the purpose of what's below is to retreive data from an outside source and test its 
# value against an input value from the user.
#for simplicity, we'll use the string 'DAVIS'
#the string was encoded using python in the same manner as above. the hex digest was put 
# into a text file and will be read into the program


#create a new variable
lastname = 'DAVIS'
lastnamehex = hashlib.sha512(lastname.encode())

#for testing purposes, go ahead and print it
print("The new string is", lastname)
print("The new hex is ", lastnamehex)
print("The hex digest is", lastnamehex.hexdigest())

#write the hashed hex digest out to a text document that i made called 'hashwords.txt'
with open('hashwords.txt', 'w') as f:
    f.write(lastnamehex.hexdigest())
f.close()
print("data was written to the file")

#now that we can do that, lets read the same data and compare it

#first read the data and print what you've got
#open the file
with open('hashwords.txt', 'r') as f:
    #read the line
    incomingline = f.readline()
    #print what you read
    print(incomingline)
    print("Thats the line that was read.")

    #this will compare the line that was read to the orignal hex digest.
    if incomingline == lastnamehex.hexdigest():
        print("that matches what was originally input")
    else:
        print("That doesn't match was was originally input")

#Sucess!!
print("Success so far!")
