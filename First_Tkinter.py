#This is my first(sorta) attempt at using tkinter to create a desktop application
#The following appplication is just a hello world. It should work well enough.
#May include a lot of 'junk code' just for testin purposes


from tkinter import *
from tkinter import ttk

root = Tk("This is the name of the window")
frm = ttk.Frame(root, padding=50)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=2, row=0)
ttk.Checkbutton(frm, text="Da Check box").grid(column=3, row=0)
ttk.Label(frm, text=" ").grid(column=1)
root.mainloop()