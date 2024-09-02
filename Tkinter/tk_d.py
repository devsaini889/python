
from tkinter import *

root = Tk()
root.geometry("500x400")
root.title('Frame')
f1 = Frame(root, bg= 'grey' , borderwidth=10, relief='sunken')
f1.pack(side='top', fill='x')
l = Label(f1 , text='Notepad ', fg= 'black')
l.pack(side='top' , fill='x')

root.mainloop()