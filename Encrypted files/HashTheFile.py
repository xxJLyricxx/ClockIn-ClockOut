# Hash The File v.2
# January 7 2023
# 
# Purpose: input a text file and a path to have the file hashed from start to finish and create a new text file of
# The text below is from Lorem Ipsum, which is a random text generator. this will be the file that gets hashed and verified.
"""
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam convallis enim nec justo aliquet cursus. Vestibulum erat dolor, semper et velit nec, ornare dignissim velit. Fusce eget massa ornare ligula elementum accumsan. Sed sagittis dapibus arcu nec maximus. Etiam non eros felis. Fusce vel mi eros. Maecenas et arcu vel elit suscipit bibendum. Morbi semper risus id ex molestie, ut euismod tellus molestie. Donec quis dui pellentesque, accumsan mauris ut, sagittis neque. Pellentesque dapibus enim ligula, quis aliquam ligula laoreet ut. Suspendisse lacus nunc, fringilla sed libero nec, aliquam elementum justo. Aenean aliquet lorem eget ullamcorper dignissim. Nam neque dui.
"""
#This text will be stored in LoremIpsum.txt
import hashlib
#the above text must be put into the code  so that the <encode> function will work.
lorem_pen = str 
#open the original document as readable so that it can be read and copied later
with open('C:\\Users\\User\\OneDrive\\Documents\\GitHub\\ClockIn-ClockOut\\Encrypted files\\newdatabase.txt', 'r') as lorem_ipsum_original:
    #read the lines and store the output into lorem_lines
    lorem_lines = lorem_ipsum_original.readlines()
    #open the new document (LoremIpsumCode as writable so that it can hold the new encoded text)
    with open("C:\\Users\\User\\OneDrive\\Documents\\GitHub\\ClockIn-ClockOut\\Encrypted files\\newdatabaseCode.txt", "w") as lorem_ipsum_code:
        #Read the text line by line and encode it
        for x in lorem_lines:
            #lorem_ipsum_code.write("---")
            lorem_pen = hashlib.sha512(x.encode())
            #lorem_ipsum_code.write(x)
            lorem_ipsum_code.write("")
            lorem_pen = lorem_pen.hexdigest()
            lorem_ipsum_code.write(lorem_pen)
            lorem_ipsum_code.write("\n")
    lorem_ipsum_code.close()
lorem_ipsum_original.close()
print("all done")
#print("this is a test")