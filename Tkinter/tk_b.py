

from tkinter import *
from PIL import Image,ImageTk
dev_root = Tk()
dev_root.geometry("1200x500")

# for png img
pic = PhotoImage(file='2.png')
label = Label(image=pic)
label.pack()


# for jpg file 
img = Image.open("1.jpg")
photo = ImageTk.PhotoImage(img)

label = Label(image=photo)
label.pack()
dev_root.mainloop()
