

from tkinter import *

root  = Tk()
root.geometry("500x400")
def name():
    print("Dev")

def place():
    print("Smpr")

def clg():
    print("AUR")

def state():
    print("Rajasthan")

f1 = Frame(root , bg='grey',borderwidth=9,relief='sunken')
f1.pack(side='top',fill='x'  )

b= Button(f1, text='Click me', command=name)
b.pack(side='left',padx=5)

c = Button(f1, text='Click me', command=place)
c.pack(side='left',padx=5)

d = Button(f1, text='Click me', command=clg)
d.pack(side='left',padx=5)

e = Button(f1, text='Click me', command=state)
e.pack(side='left', padx=5)


root.mainloop()