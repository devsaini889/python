from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.geometry("500x400")

def daaku():
    print(f"{uslider.get()}")
    tmsg.showinfo('sardar', f"{uslider.get()} the sardaar")

A = Label(root, text="Kitne aadmi the ??")
A.pack()


uslider = Scale(root, from_=0, to=50, orient=HORIZONTAL)
uslider.pack()

btn = Button(root, text="jawab", command=daaku)
btn.pack()

root.mainloop()
