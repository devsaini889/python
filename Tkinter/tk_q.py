from tkinter import *

class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("500x400")

    def status (self):
        self.var = StringVar()
        self.var.set("Ready")
        self.statusbar= Label(self , textvariable=self.var, anchor='w')
        self.statusbar.pack(side=BOTTOM , fill=X)



if __name__ == '__main__':
    window = GUI()
    window.status()
    window.mainloop()