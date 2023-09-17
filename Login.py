import tkinter.messagebox
from tkinter import*
from logMe import logMe
#from Overhead import*

def confirmName(x):
    with open("Employees.txt", "r") as ur:
        lines = ur.readlines();
        for line in lines:
            if(line.__contains__(x)):
                foundname = line[0:10]
                foundname = foundname.replace(" ", "")
                if (foundname == x):
                    return True;



def submitLogin():
    name = entrySpace.get()
    password = entrySpace2.get()
    logMe(str("Login attempt(tkinter): " + name))
    tkinter.messagebox.showinfo(message="this is the message box " + name + " " + password)
    confirmName(name)

root = Tk()
label1 = Label(root, text = "Name: ")
label1.grid(row = 0, column = 0, sticky = "E")
entrySpace = Entry(root)
entrySpace.grid(row=0, column=1, columnspan=2)

label2 = Label(root, text = "Password: ")
label2.grid(row = 1, column = 0, sticky = "E")
entrySpace2 = Entry(root)
entrySpace2.grid(row=1, column=1, columnspan= 2)

cbutton = Checkbutton(root, text = "Remember Name: ")
cbutton.grid(columnspan = 2)

button1 = Button(root, text = "  Submit  ", command= submitLogin)
button1.grid(row=2, column=2)
root.mainloop()