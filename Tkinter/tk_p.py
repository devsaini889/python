from tkinter import *

root = Tk()
def update():
    print("updating geometry")
    root.geometry(f"{width.get()}x{height.get()}")
root.geometry("500x400")
width = StringVar()
height = StringVar()

Entry(root , textvariable= width).pack()
Entry(root , textvariable=  height).pack()
Button(root ,text= 'update', command= update).pack()

root.mainloop()