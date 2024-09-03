from tkinter import *

root = Tk()
root.geometry("500x400")

def getvals():
    print("The form is completed")

Label(root , text='Welcome to our form ', font= "comicsansm 13 bold" , pady=15).grid(row=0,column=3)
name = Label( root , text='username')
password = Label( root , text='password')
clg = Label( root , text='collage')
id_clg = Label( root , text= 'collage id')

name.grid(row=1 , column=0)
password.grid(row=2,column=0)
clg.grid(row=3, column=0)
id_clg.grid(row=4, column=0)

namevalue = StringVar()
passvalue = StringVar()
clgvalue = StringVar()
id_clgvalue = StringVar()
attendencevalue = IntVar()

nameentry = Entry(root , textvariable=namevalue)
passentry = Entry(root , textvariable=passvalue)
clgentry = Entry(root , textvariable=clgvalue)
id_clgentry = Entry(root , textvariable=id_clgvalue)


nameentry.grid(row=1, column=3)
passentry.grid(row=2, column=3)
clgentry.grid(row=3, column=3)
id_clgentry.grid(row=4, column=3)


stu = Checkbutton(text='attendence is 75 above', variable= attendencevalue)
stu.grid(row=5 , column= 3)


Button(text="submit" , command=getvals).grid(rows= 5 ,column=2)

root.mainloop()