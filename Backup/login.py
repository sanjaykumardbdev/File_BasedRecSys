# https://www.youtube.com/watch?v=OVwKzIvCdsA
# https://www.youtube.com/watch?v=D39hDyBp9Go
# https://www.youtube.com/watch?v=IGYg3Z82Sok
# https://www.youtube.com/watch?v=ixgFBsvDsQk

from tkinter import *
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk

class Login:
    def __init__(self, root):
        # initialize the root
        self.root = root
        self.root.title("File Based Record System")
        self.root.geometry("1350x750+0+0")
        self.root.resizable(False, False)
        self.root.config(bg='white')

        # ======= Bg Image ==========
        # self.bg is obj of class
        # self.bg=ImageTk.PhotoImage(file="Files/bg1.png")
        # below bg will becode obj of root
        # bg=Label(self.root, image=self.bg).place(x=250, y=80, relwidth=1, relheight=1)

        # ======= Left Image ==========
        # self.bg is obj of class
        # self.left=ImageTk.PhotoImage(file="Files/side.PNG")
        # below bg will becode obj of root
        # left=Label(self.root, image=self.left).place(x=100, y=250)

        #  Variables

        self.user = StringVar()
        self.password = StringVar()

        #  Frame Design
        F1=Frame(self.root, bd=10, relief=GROOVE)
        # F1.place(x=450, y=150, width=450, height=300)
        F1.place(x=650, y=150, height=350)

        # create heading
        title = Label(F1, text='Login System', font=("times new roman", 30, "bold")).grid(row=0, columnspan=2, pady=20)

        lblusername = Label(F1, text='Username', font=("times new roman", 25, "bold")).grid(row=1, column=0, pady=15, padx=10)
        txtuser = Entry(F1, bd=7, relief=GROOVE, width=25, font="arial 15 bold", textvariable=self.user).grid(row=1, column=1, pady=10, padx=10)

        lblpass = Label(F1, text='Password', font=("times new roman", 25, "bold")).grid(row=2, column=0, pady=15, padx=20)
        txtpass = Entry(F1, bd=7, relief=GROOVE, width=25, font="arial 15 bold",show='*', textvariable=self.password).grid(row=2, column=1, pady=10, padx=20)

        btnlog = Button(F1, text='Login', bd=7, font="arial 15 bold", width=10, command=self.logfun).place(x=10, y=250)
        btnreset = Button(F1, text='Reset', bd=7, font="arial 15 bold", width=10, command=self.reset).place(x=180, y=250)
        btnexit = Button(F1, text='Exit', bd=7, font="arial 15 bold", width=10, command=self.exit).place(x=350, y=250)

    def logfun(self):
        if self.user.get()=='Sanjay' and self.password.get()=='sanjay':
            messagebox.showinfo('Success', "Login Success")
        else:
            messagebox.showerror('Error', 'Invalid Username/Password')

    def reset(self):
        self.user.set("")
        self.password.set("")

    def exit(self):
        option=messagebox.askyesno('Exit',"Do you really want to close")
        if option>0:
            self.root.destroy()

        print(self.user.get())
        print(self.password.get())


# commented bec calling software.py from this page.

# create an obj of class Tk()
root=Tk()
# create obj of class Login, pass obj of class TK() to Login class
obj=Login(root)
root.mainloop()



