

from tkinter import *

root = Tk()
root.geometry("500x400")


scrollbar =Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)


listbox = Listbox(root, yscrollcommand=scrollbar.set)
for i in range(100):
    listbox.insert(END , f"item{i}")

listbox.pack()
scrollbar.config(command=listbox.yview)

root.mainloop()