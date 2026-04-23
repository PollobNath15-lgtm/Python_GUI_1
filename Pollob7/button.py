from tkinter import *
top=Tk()
top.geometry("200x200")

checkvar1 =IntVar()
checkvar2 =IntVar()
checkvar3 =IntVar()
cb1=Checkbutton(top, text="C", variable=checkvar1,onvalue=1,offvalue=0,height=2, width=10)
cb2=Checkbutton(top, text="Ccc",variable=checkvar2,onvalue=1,offvalue=0,height=2, width=10)
cb3=Checkbutton(top, text="Cc",variable=checkvar3,onvalue=1,offvalue=0,height=2, width=10)

cb1.pack()
cb2.pack()
top.mainloop()