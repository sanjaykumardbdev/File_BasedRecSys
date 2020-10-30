import shutil
from datetime import datetime
from tkinter import *
from tkinter import ttk, messagebox
import os


# from login import *


class File_App:
    def __init__(self, root):
        self.root = root
        self.root.title("File Based Record System")
        self.root.geometry("1350x750+0+0")
        # self.root.config(bg='gray')

        title = Label(self.root, text='File Based Record System', pady=10, font=("times new roman", 35, "bold"),
                      bg='gray', bd=10, relief=GROOVE).pack(fill=X)

        # All variables:

        self.sid = StringVar()
        self.name = StringVar()
        self.course = StringVar()
        self.address = StringVar()
        self.city = StringVar()
        self.contact = StringVar()
        self.date = StringVar()
        self.degree = StringVar()
        self.proof = StringVar()
        self.payment = StringVar()

        Student_Frame = Frame(self.root, bd=10, relief=GROOVE)  # , bg='gray')
        Student_Frame.place(x=0, y=100, width=800, height=400)
        # Student_Frame.place(x=0, y=100, height=300)

        stitle = Label(Student_Frame, text='Student Details', font=("times new roam", 30, "bold")).grid(row=0,
                                                                                                        columnspan=5,
                                                                                                        padx=5, pady=5)

        # lblsid = Label(Student_Frame, text='Student ID', relief=GROOVE, font=("times new roam", 12, "bold")).grid(row=1,column=1,padx=5,pady=5,sticky="w")

        lblsid = Label(Student_Frame, text='Student ID', font=("times new roam", 12, "bold")).grid(row=1, column=1,
                                                                                                   padx=5, pady=5,
                                                                                                   sticky="w")
        txtsid = Entry(Student_Frame, width=15, textvariable=self.sid, relief=GROOVE, font=("arial", 12)).grid(row=1,
                                                                                                               column=2,
                                                                                                               padx=5,
                                                                                                               pady=5)

        lblname = Label(Student_Frame, text='Name', font=("times new roam", 12, "bold")).grid(row=2, column=1, padx=5,
                                                                                              pady=5, sticky="w")
        txtname = Entry(Student_Frame, width=15, textvariable=self.name, relief=GROOVE, font=("arial", 12)).grid(row=2,
                                                                                                                 column=2,
                                                                                                                 padx=5,
                                                                                                                 pady=5)

        lblcontact = Label(Student_Frame, text='Contact', font=("times new roam", 12, "bold")).grid(row=1, column=3,
                                                                                                    padx=10, pady=5,
                                                                                                    sticky="w")
        txtcontact = Entry(Student_Frame, width=15, textvariable=self.contact, relief=GROOVE, font=("arial", 12)).grid(
            row=1, column=4, padx=10, pady=5)

        lbldate = Label(Student_Frame, text='Date(dd/mm/yyyy)', font=("times new roam", 12, "bold")).grid(row=2,
                                                                                                          column=3,
                                                                                                          padx=10,
                                                                                                          pady=5,
                                                                                                          sticky="w")
        txtdate = Entry(Student_Frame, width=15, textvariable=self.date, relief=GROOVE, font=("arial", 12)).grid(row=2,
                                                                                                                 column=4,
                                                                                                                 padx=10,
                                                                                                                 pady=5)

        lblcourse = Label(Student_Frame, text='Course', font=("times new roam", 12, "bold")).grid(row=3, column=1,
                                                                                                  padx=10, pady=5,
                                                                                                  sticky="w")
        txtcourse = Entry(Student_Frame, width=15, textvariable=self.course, relief=GROOVE, font=("arial", 12)).grid(
            row=3, column=2, padx=10, pady=5)

        lbladdress = Label(Student_Frame, text='Address', font=("times new roam", 12, "bold")).grid(row=4, column=1,
                                                                                                    padx=10, pady=5,
                                                                                                    sticky="w")
        txtaddress = Entry(Student_Frame, width=15, textvariable=self.address, relief=GROOVE, font=("arial", 12)).grid(
            row=4, column=2, padx=10, pady=5)

        lblcity = Label(Student_Frame, text='City', font=("times new roam", 12, "bold")).grid(row=5, column=1, padx=10,
                                                                                              pady=5, sticky="w")
        txtcity = Entry(Student_Frame, width=15, textvariable=self.city, relief=GROOVE, font=("arial", 12)).grid(row=5,
                                                                                                                 column=2,
                                                                                                                 padx=10,
                                                                                                                 pady=5)

        lbldegree = Label(Student_Frame, text='Select Degree', font=("times new roam", 12, "bold")).grid(row=3,
                                                                                                         column=3,
                                                                                                         padx=10,
                                                                                                         pady=5,
                                                                                                         sticky="w")
        degcombo = ttk.Combobox(Student_Frame, textvariable=self.degree, width=15, font=("arial", 11, "bold"))
        degcombo['values'] = ("BCA", "MCA", "Btech", "Mtech", "MBA")
        degcombo.grid(row=3, column=4, padx=10, pady=5)

        lblid = Label(Student_Frame, text='Select ID', font=("times new roam", 12, "bold")).grid(row=4, column=3,
                                                                                                 padx=10, pady=5,
                                                                                                 sticky="w")
        idcombo = ttk.Combobox(Student_Frame, textvariable=self.proof, width=15, font=("arial", 11, "bold"))
        idcombo['values'] = ("PAN Card", "Passport", "DL", "Aadhar Card", "Stud ID Card")
        idcombo.grid(row=4, column=4, padx=10, pady=5)

        lblpaymode = Label(Student_Frame, text='Payment Mode', font=("times new roam", 12, "bold")).grid(row=5,
                                                                                                         column=3,
                                                                                                         padx=10,
                                                                                                         pady=5,
                                                                                                         sticky="w")
        paycombo = ttk.Combobox(Student_Frame, textvariable=self.payment, width=15, font=("arial", 11, "bold"))
        paycombo['values'] = ("NEFT", "Net Banking", "Other Pay")
        paycombo.grid(row=5, column=4, padx=10, pady=5)

        # Bottom Frame

        btnfrm = Frame(self.root, bd=8, relief=GROOVE, bg='gray')
        btnfrm.place(x=0, y=410, width=695, height=70)
        # btnfrm.place(x=0, y=410)

        btnsave = Button(btnfrm, text='Save', bd=8, font=("times new roman", 11, "bold"), width=10,
                         command=self.save_entry)
        btnsave.grid(row=1, column=1, padx=10, pady=5)

        btndel = Button(btnfrm, text='Delete', bd=8, font=("times new roman", 11, "bold"), width=10,
                        command=self.delete_rec)
        btndel.grid(row=1, column=2, padx=10, pady=5)

        btnclr = Button(btnfrm, text='Clear', bd=8, font=("times new roman", 11, "bold"), width=10,
                        command=self.clear_inputs)
        btnclr.grid(row=1, column=3, padx=10, pady=5)

        btnlogout = Button(btnfrm, text='Logout', bd=8, font=("times new roman", 11, "bold"), width=10,
                           command=self.logout)
        btnlogout.grid(row=1, column=4, padx=10, pady=5)

        btnexit = Button(btnfrm, text='Exit', bd=8, font=("times new roman", 11, "bold"), width=10,
                         command=self.exit_fun)
        btnexit.grid(row=1, column=5, padx=10, pady=5)

        # List Frame
        listfrm = Frame(root, bd=10, relief=GROOVE, bg="gray")
        listfrm.place(x=700, y=100, width=650, height=600)

        Label(listfrm, text='All Files', bd=10, relief=GROOVE, font=("times new roman", 12, "bold")).pack(side=TOP,
                                                                                                          fill=X)

        # create listbox here

        scroll_y = Scrollbar(listfrm, orient=VERTICAL)
        self.file_list = Listbox(listfrm, yscrollcommand=scroll_y.set)

        scroll_y.pack(side=RIGHT, fill=Y)
        self.file_list.pack(fill=BOTH, expand=1)

        scroll_y.config(command=self.file_list.yview)
        # for i in range(100):            i += 1;            file_list.insert(END, str(i))

        self.file_list.bind("<ButtonRelease-1>", self.get_list)
        self.show_files()

    def logout(self):
        self.root.destroy()
        from Files import login
        # obj = login()


    def save_entry(self):
        present = 'no'
        if self.sid.get() == "":
            messagebox.showerror("Error", " ID is required")
        else:
            print('path= ')
            print(os.getcwd())
            files = os.listdir("C:/Users/sanjay.kumar12/PycharmProjects/Projects/File_BasedRecSys/Files/Data_Files/")
            if len(files) > 0:
                for i in files:
                    if i.split(".")[0] == self.sid.get():
                        present = 'yes'
                if present == 'yes':
                    # copy file to backup before delete.
                    ask = messagebox.askyesno("Update", "File already present \n Do you want to update")
                    if ask > 0:
                        messagebox.showinfo("Update", "Record updated Successfully")
                        self.save_file()
                        self.show_files()
                        # self.clear_inputs()
                else:
                    self.save_file()
                    self.show_files()
                    messagebox.showinfo("Saved", "Record saved Successfully")
            else:
                self.save_file()
                self.show_files()
                messagebox.showinfo("Saved", "Record saved Successfully")

    def save_file(self):
        f = open("C:/Users/sanjay.kumar12/PycharmProjects/Projects/File_BasedRecSys/Files/Data_Files/" + str(
            self.sid.get()) + ".txt", "w+")
        f.write(
            str(self.sid.get()) + "," +
            str(self.name.get()) + "," +
            str(self.course.get()) + "," +
            str(self.address.get()) + "," +
            str(self.city.get()) + "," +
            str(self.contact.get()) + "," +
            str(self.date.get()) + "," +
            str(self.degree.get()) + "," +
            str(self.proof.get()) + "," +
            str(self.payment.get())
        )
        f.close()
        # messagebox.showinfo("Success", "File created  :-  " + str(self.sid.get()) + ".txt")
        # self.show_files()

    def show_files(self):
        files = os.listdir("C:/Users/sanjay.kumar12/PycharmProjects/Projects/File_BasedRecSys/Files/Data_Files/")
        self.file_list.delete(0, END)
        if len(files) > 0:
            for i in files:
                self.file_list.insert(END, i)

    def get_list(self, ev):
        cur_sel = self.file_list.curselection()
        # print(cur_sel)
        # print(self.file_list.get(cur_sel))

        f1 = open(
            "C:/Users/sanjay.kumar12/PycharmProjects/Projects/File_BasedRecSys/Files/Data_Files/" + self.file_list.get(
                cur_sel))
        values = []
        for i in f1:
            values = i.split(",")
        # print(values)
        # print(values[0])

        self.sid.set(values[0])
        self.name.set(values[1])
        self.course.set(values[2])
        self.address.set(values[3])
        self.city.set(values[4])
        self.contact.set(values[5])
        self.date.set(values[6])
        self.degree.set(values[7])
        self.proof.set(values[8])
        self.payment.set(values[9])

    def clear_inputs(self):
        self.sid.set("")
        self.name.set("")
        self.course.set("")
        self.address.set("")
        self.city.set("")
        self.contact.set("")
        self.date.set("")
        self.degree.set("")
        self.proof.set("")
        self.payment.set("")

    def delete_rec(self):
        # print(self.sid.get())
        present = 'no'
        if self.sid.get() == "":
            messagebox.showerror("Error", " Select record to delete")
        else:
            files = os.listdir("C:/Users/sanjay.kumar12/PycharmProjects/Projects/File_BasedRecSys/Files/Data_Files/")
            if len(files) > 0:
                for i in files:
                    if i.split(".")[0] == self.sid.get():
                        present = 'yes'
                if present == 'yes':
                    # copy file to backup before delete.
                    ask = messagebox.askyesno("Delete", " Do you want to delete")
                    if ask > 0:
                        # src = r'C:\Users\sanjay.kumar12\PycharmProjects\Projects\File_BasedRecSys\Files\Data_Files\"+self.sid.get()+".txt'

                        src1 = r'C:\Users\sanjay.kumar12\PycharmProjects\Projects\File_BasedRecSys\Files\Data_Files'
                        src = os.path.join(src1, self.sid.get() + ".txt")

                        trg = r'C:\Users\sanjay.kumar12\PycharmProjects\Projects\File_BasedRecSys\Files\Data_Files\Deleted_Files'
                        print(src)
                        print(trg)
                        self.replace_file()

                        shutil.move(src, trg)
                        # os.remove("C:/Users/sanjay.kumar12/PycharmProjects/Projects/File_BasedRecSys/Files/Data_Files/"+self.sid.get()+".txt")
                        messagebox.showinfo("Success", "File Deleted")
                        self.show_files()
                        self.clear_inputs()
                else:
                    messagebox.showerror("Error", "File not found")

    def replace_file(self):
        present = 'no'
        deleted_files = os.listdir("C:/Users/sanjay.kumar12/PycharmProjects/Projects/File_BasedRecSys/Files/Data_Files/Deleted_Files/")
        print('delete fiels list')
        print(deleted_files)

        if len(deleted_files) > 0:
            for i in deleted_files:
                if i.split(".")[0] == self.sid.get():
                    present = 'yes'
                    print('val of i')
                    print(i)
            if present == 'yes':
                print('file is present')
                ct = datetime.now()
                print(ct.microsecond)
                cur_time = ct.microsecond

                existing_file = 'C:/Users/sanjay.kumar12/PycharmProjects/Projects/File_BasedRecSys/Files/Data_Files/Deleted_Files/' + self.sid.get() + ".txt"
                new_file_name = 'C:/Users/sanjay.kumar12/PycharmProjects/Projects/File_BasedRecSys/Files/Data_Files/Deleted_Files/' + self.sid.get() + '_' + str(cur_time) +".txt"
                os.rename(existing_file, new_file_name)
                # os.remove("C:/Users/sanjay.kumar12/PycharmProjects/Projects/File_BasedRecSys/Files/Data_Files/Deleted_Files/" + self.sid.get() + ".txt")
                # if file is older than 3 days , remove from system.

    def exit_fun(self):
        ask = messagebox.askyesno("Exit", " Do you want to exit?")
        if ask > 0:
            self.root.destroy()


root = Tk()
obj = File_App(root)
root.mainloop()
