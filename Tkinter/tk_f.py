from tkinter import *

root = Tk()
root.geometry("500x400")

def getvals():
    print(uservalue.get())
    print(passvalue.get())

# Create Labels
user = Label(root, text='Username')
password = Label(root, text='Password')
user.grid(row=0, column=0)
password.grid(row=1, column=0)

# Create StringVar variables
uservalue = StringVar()
passvalue = StringVar()

# Create Entry widgets with the correct textvariable assignment
userentry = Entry(root, textvariable=uservalue)
passentry = Entry(root, textvariable=passvalue)

userentry.grid(row=0, column=1)
passentry.grid(row=1, column=1)

# Create a Submit button
Button(root, text='Submit', command=getvals).grid(row=2, column=1)

root.mainloop()
