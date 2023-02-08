# Hash The File v.2
# January 7 2023
# 
# Purpose: input a text file and a path to have the file hashed from start to finish and create a new text file of the hashed lines
#first, import the hash library
import hashlib
original_pen = str
input_file_path = input("Please Input the path of the file: ")
with open(input_file_path, 'r') as original_file:
    #read the lines and store the output into lorem_lines
    original_file = original_file.readlines()
    #open the new document and read the lines
    with open(input_file_path + "Encoded", "w") as output_file:
        #Read the text line by line and encode it
        for x in original_file:
            #output_file.write("---")
            original_pen = hashlib.sha512(x.encode())
            #output_file.write(x)
            output_file.write("")
            original_pen = original_pen.hexdigest()
            output_file.write(original_pen)
            output_file.write("\n")
    output_file.close()
    print("done hashing")
#original_file.close()
print("all done")
#print("this is a test")