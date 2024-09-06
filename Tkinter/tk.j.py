from tkinter import *

root = Tk()

root.geometry("600x300")
def harry(event):
    print(f"Your coordinate is {event.x},{event.y}")
widget = Button(root , text = "click me please")
widget.pack()
widget.bind('<Button-1>',harry )
widget.bind('<Double-1>',quit)


root.mainloop()