from tkinter import *

root = Tk()
root.geometry("500x650")
def click(event):
    global sc
    text = event.widget.cget("text")
    print(text)
    if text == '=':
        if sc.get().isdigit():
            value = int(sc.get())

        else:
            try:
                value=eval(screen.get())
            except Exception as e:
                print(e)
                value = "Error"

    elif text == 'C':
        sc.set("")
        screen.update()
    
    else:
        sc.set(sc.get()+text)
        screen.update()

    sc.set(value)
    screen.update()

sc = StringVar()
sc.set("")
screen = Entry(root, textvariable=sc , font="lucida 40 bold")
screen.pack(fill = X ,ipadx=15 , pady=10, padx=10)

F = Frame(root, bg="grey")
b= Button(F,text='9',font="lucida 30 bold" , padx=10)
b.pack(side= LEFT,padx=10, pady=10)
b.bind("<Button-1>",click)

b= Button(F,text='8',font="lucida 30 bold" , padx=10)
b.pack(side= LEFT,padx=10, pady=10)
b.bind("<Button-1>",click)

b= Button(F,text='7',font="lucida 30 bold" , padx=10)
b.pack(side=LEFT,padx=10, pady=10)
b.bind("<Button-1>",click)

F.pack()
F = Frame(root, bg="grey")
b= Button(F,text='6',font="lucida 30 bold" , padx=10)
b.pack(side= LEFT,padx=10, pady=10)
b.bind("<Button-1>",click)

b= Button(F,text='5',font="lucida 30 bold" , padx=10)
b.pack(side= LEFT,padx=10, pady=10)
b.bind("<Button-1>",click)

b= Button(F,text='4',font="lucida 30 bold" , padx=10)
b.pack(side=LEFT,padx=10, pady=10)
b.bind("<Button-1>",click)

F.pack()
F = Frame(root, bg="grey")
b= Button(F,text='3',font="lucida 30 bold" , padx=10)
b.pack(side= LEFT,padx=10, pady=10)
b.bind("<Button-1>",click)

b= Button(F,text='2',font="lucida 30 bold" , padx=10)
b.pack(side= LEFT,padx=10, pady=10)
b.bind("<Button-1>",click)

b= Button(F,text='1',font="lucida 30 bold" , padx=10)
b.pack(side=LEFT,padx=10, pady=10)
b.bind("<Button-1>",click)

F.pack()
F = Frame(root, bg="grey")
b= Button(F,text='0',font="lucida 30 bold" , padx=11)
b.pack(side= LEFT,padx=10, pady=10)
b.bind("<Button-1>",click)

b= Button(F,text='+',font="lucida 30 bold" , padx=11)
b.pack(side= LEFT,padx=10, pady=10)
b.bind("<Button-1>",click)

b= Button(F,text='-',font="lucida 30 bold" , padx=11)
b.pack(side=LEFT,padx=10, pady=10)
b.bind("<Button-1>",click)

F.pack()

F = Frame(root, bg="grey")
b= Button(F,text='*',font="lucida 30 bold" , padx=12)
b.pack(side= LEFT,padx=10, pady=10)
b.bind("<Button-1>",click)

b= Button(F,text='/',font="lucida 30 bold" , padx=12)
b.pack(side= LEFT,padx=10, pady=10)
b.bind("<Button-1>",click)

b= Button(F,text='C',font="lucida 30 bold" , padx=12)
b.pack(side=LEFT,padx=10, pady=10)
b.bind("<Button-1>",click)

F.pack()
F = Frame(root, bg="grey")
b= Button(F,text='=',font="lucida 30 bold" , padx=12)
b.pack(side= BOTTOM,padx=10, pady=10)
b.bind("<Button-1>",click)
F.pack()




root.mainloop()