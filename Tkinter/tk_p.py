from tkinter import *

root = Tk()

def update():
    print("updating geometry")
    root.geometry(f"{width.get()}x{height.get()}")

root.geometry("500x400")

width = StringVar()
height = StringVar()

# Create and pack the labels and entry widgets
Label(root, text="Width:").pack()
Entry(root, textvariable=width).pack()

Label(root, text="Height:").pack()
Entry(root, textvariable=height).pack()

Button(root, text='Update', command=update).pack(pady=10)

root.mainloop()
