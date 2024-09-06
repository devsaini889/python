

from tkinter import *

root = Tk()

Canvas_width = 800
canvas_height = 400
root.geometry(f"{Canvas_width}x{canvas_height}")

can_widget = Canvas(root , width= Canvas_width , height= canvas_height)
can_widget.pack()
# creating the line with canvas 
can_widget.create_line(50,400,800,50)
# creating a rectangle
can_widget.create_rectangle(100,300,400,50)

# ypu can create many more thing try to explore canvas in tkinter

root.mainloop()