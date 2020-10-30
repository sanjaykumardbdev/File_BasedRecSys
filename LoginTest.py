from tkinter import *
root = Tk()
from PIL import Image
from PIL import ImageTk
# from db_conn import *

class Login():
    def __init__(self, root):
        self.root = root
        self.root.geometry("500x500+30+100")
        self.root.resizable(False,False)

        # ======= Bg Image ==========
        # self.bg is obj of class
        self.bg=ImageTk.PhotoImage(file="Files/bg1.png")
        # below bg will becode obj of root
        bg=Label(self.root, image=self.bg).place(x=250, y=40, relwidth=1, relheight=1)

        # ======= Left Image ==========
        # self.bg is obj of class
        self.left=ImageTk.PhotoImage(file="Files/side.PNG")
        # below bg will becode obj of root
        left=Label(self.root, image=self.left).place(x=20, y=80)


        # Design Frame
        F1 = Frame(self.root, bd=10, relief=GROOVE)
        F1.place(x=225, y=200, height=180)

        title = Label(F1, text="Login System", font=("times new roman", 15, "bold")).grid(row=0, columnspan=2)

        lblusername = Label(F1, text='UserName', font=("arial 10 bold")).grid(row=1, column=0, padx=10, pady=10)
        txtusername = Entry(F1, font=("arial 10 bold")).grid(row=1, column=1, padx=10, pady=10)

        lbluserpass = Label(F1, text='Password', font=("arial 10 bold")).grid(row=2, column=0, padx=10, pady=10)
        txtuserpass = Entry(F1, font=("arial 10 bold"),show='*').grid(row=2, column=1, padx=10, pady=10)

        btnlogin = Button(F1,text='Login', font=("arial 10 bold"), width=8).place(x=5, y=120)
        btnreset = Button(F1, text='Reset', font=("arial 10 bold"), width=8).place(x=90, y=120)
        btnexit = Button(F1, text='Exit', font=("arial 10 bold"), width=8).place(x=170, y=120)



obje = Login(root)
root.mainloop()
