#library Section
import tkinter as tk

#window Control
root=tk.Tk()

root.title("My First app")

root.geometry("400x300")

root.resizable(False,False)

def b():
    lbl = tk.Label(root,
                   text="Welcome to my App\n Hello",
                   font=('galada', 24),
                   fg='red',
                   bg='brown')

    lbl.pack(expand=True)

a=tk.Button(root,text ="1",
              font=('galada',16),
              fg='blue',
              bg='teal',
              bd='5',
              activebackground='red',
              command=b)
a.pack()
a=tk.Button(root,text ="2",
              font=('galada',16),
              fg='blue',
              bg='teal',
              bd='5',
              activebackground='red',
              command=b)
a.pack()
a=tk.Button(root,text ="3",
              font=('galada',16),
              fg='blue',
              bg='teal',
              bd='5',
              activebackground='red',
              command=b)
a.pack()

#window show always
root.mainloop()
