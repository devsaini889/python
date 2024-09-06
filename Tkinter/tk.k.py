
from tkinter import *

root = Tk()
root.geometry("700x500")
def myfunc():
    print("mujhe bs itna hi ata h ")


# this is basic menubar
mymenu = Menu(root)
mymenu.add_command(label='file', command=myfunc)
mymenu.add_command(label='exit',command=quit)
root.config(menu = mymenu)

# a dropdown menubar

urmenu = Menu(root)

m1 = Menu(urmenu)
m1.add_command(label="project", command=myfunc)
m1.add_command(label="save", command=myfunc)
m1.add_command(label="save as", command=myfunc)
m1.add_command(label="print", command=myfunc)

root.config(menu=urmenu)
urmenu.add_cascade(label="file",menu= m1)

root.mainloop()