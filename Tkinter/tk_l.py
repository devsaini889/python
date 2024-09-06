from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.geometry("700x500")
def myfunc():
    print("ab aa gaya")

def help():
    a = tmsg.showinfo("Help","i will help you")


urmenu = Menu(root)

m1 = Menu(urmenu)
m1.add_command(label="project", command=myfunc)
m1.add_command(label="save", command=myfunc)
m1.add_command(label="save as", command=myfunc)
m1.add_command(label="print", command=myfunc)

root.config(menu=urmenu)
urmenu.add_cascade(label="file",menu= m1)




m2 = Menu(urmenu)
m2.add_command(label="click here", command=help)

root.config(menu=urmenu)
urmenu.add_cascade(label="help",menu= m2)



root.mainloop()