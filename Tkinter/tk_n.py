

from tkinter import *

root = Tk()
root.geometry("500x400")
lbx = Listbox(root)
lbx.pack()
lbx.insert(END, "first item")
lbx.insert(ACTIVE,"2 item") #you can change accordingly 
lbx.insert(ACTIVE,"2 item")
lbx.insert(ACTIVE,"2 item")
lbx.insert(ACTIVE,"2 item")
lbx.insert(ACTIVE,"2 item")
lbx.insert(ACTIVE,"2 item")
lbx.insert(ACTIVE,"2 item")
root.mainloop()

