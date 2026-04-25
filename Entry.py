from tkinter import *

top = Tk()
top.title("Pollob")

top.geometry("400x250")

name = Label(top, text="Name",fg="teal",font='galada').place(x=30, y=50)

email = Label(top, text="Email",fg="teal",font='galada').place(x=30, y=90)

password = Label(top, text="Password",fg="teal",font='galada').place(x=30, y=130)

sbmitbtn = Button(top, text="Submit", activebackground="teal", activeforeground="white",fg="teal",font='galada').place(x=30, y=170)

e1 = Entry(top).place(x=100, y=50)

e2 = Entry(top).place(x=100, y=90)

e3 = Entry(top).place(x=100, y=130)

top.mainloop()