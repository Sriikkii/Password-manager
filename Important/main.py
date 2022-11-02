from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from cryptography.fernet import Fernet
import mysql.connector as m
import pickle
import os
import string
import random , sys
import pyperclip


def SetMasterPassword(mp):
    with open("key.key", "rb") as key_file:
        k = key_file.read()
        key = k
        fer = Fernet(key)
    g = fer.encrypt(mp.encode()).decode()
    # o = input(
    #     "Enter the file name in which you want to store your master password ")
    j = "Master.dat"
    with open(j, "wb") as t:
        pickle.dump(g, t)
        pass


def Biget():
    # global root
    # messagebox.showinfo("TEST")
    # return None
    with open("preferiti.txt", "w") as f:
        f.write("Binary")
    with open("binary.dat", "wb") as f:
        pickle.dump(["__Init__"], f)


def Textet():
    # global root
    # messagebox.showinfo("TEST")
    # return None
    with open("preferiti.txt", "w") as f:
        f.write("Text")
    with open("text.txt", "w") as f:
        f.write("")


def Database():
    # global root
    # messagebox.showinfo("TEST")
    # return None
    with open("preferiti.txt", "w") as f:
        f.write("database")
    con = m.connect(host="localhost", user="root", password="Modern@2021")
    cur = con.cursor()
    cur.execute("CREATE DATABASE IF NOT EXISTS PasswordManager")
    cur.execute("USE PasswordManager")
    cur.execute(
        "CREATE TABLE IF NOT EXISTS Passwords (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), password VARCHAR(255))"
    )


# Add passwordsand user names
def AddPassword():
    root = Tk()
    root.title("Add Password")
    root.geometry("480x240")
    root.configure(background="#2c3e50")
    root.resizable(False, False)
    Name = Entry(root, width=30)
    Lab = Label(root, text="Name", background="#2c3e50", foreground="white")
    Lab.grid(row=0, column=0, padx=20)
    Name.grid(row=0, column=1, padx=20)
    Password = Entry(root, width=30)
    Lab2 = Label(root, text="Password", background="#2c3e50", foreground="white")
    Lab2.grid(row=1, column=0, padx=20)
    Password.config(show="*")
    Password.grid(row=1, column=1, padx=20)
    B1 = Button(root, text="Add", command=lambda: Add(Name.get(), Password.get()))
    B1.grid(row=2, column=1, padx=20)
    root.mainloop()


def Add(Name, Password):
    with open("key.key", "rb") as r:
        k = r.read()
        key = k
        fer = Fernet(key)

    with open("preferiti.txt", "r") as f:
        x = f.readline()
        if x == "Binary":
            with open("binary.dat", "ab") as f:
                pickle.dump([Name, fer.encrypt(Password.encode()).decode()], f)
                messagebox.showinfo("Success ", "Password Added")
        elif x == "Text":
            with open("text.txt", "a") as f:
                f.write(
                    Name + ":" + fer.encrypt(Password.encode()).decode("UTF-8") + "\n"
                )
                messagebox.showinfo("Success ", "Password Added")
        elif x == "database":
            con = m.connect(
                host="localhost",
                user="root",
                password="Modern@2021",
                database="PasswordManager",
            )
            cur = con.cursor()
            cur.execute(
                "INSERT INTO Passwords (name, password) VALUES (%s, %s)",
                (Name, fer.encrypt(Password.encode())),
            )
            con.commit()
            messagebox.showinfo("Success ", "Password Added")


class Log:
    def __init__(self) -> None:
        self.root = Tk()
        self.root.title("Login")
        self.root.geometry("480x240")
        self.root.configure(background="#2c3e50")
        self.root.resizable(False, False)
        self.Lab = Label(self.root, text="Master Password", background="#2c3e50", foreground="white")
        self.Lab.grid(row=0, column=0, padx=20)
        self.Password = Entry(self.root, width=30)
        self.Password.config(show="*")
        self.Password.grid(row=0, column=1, padx=20)
        self.B1 = Button(self.root, text="Login", command=lambda : self.Login(self.Password.get()))
        self.B1.grid(row=1, column=1, padx=20)
        self.root.mainloop()

    def Login(self, Password):
        with open("key.key", "rb") as r:
            k = r.read()
            key = k
            fer = Fernet(key)
        with open("Master.dat", "rb") as f:
            x = pickle.load(f)
            if fer.decrypt(x.encode()).decode() == Password:
                self.root.destroy()
                ViewPassword()
            else:
                messagebox.showerror("Error", "Wrong Password")
                return False




class ViewPassword:
    def __init__(self) -> None:
        (self.root, self.treee) = self.ViewPass()
        self.DecBut = Button(self.root, text="Decrypt", command=lambda : self.Decrypt(self.root, self.treee) , width=30)
        self.DecBut.grid(row=1, column=0)
        self.EncBut = Button(self.root, text="Encrypt", command=lambda : self.Encrypt(self.root, self.treee) , width=30)
        self.EncBut.grid(row=1, column=1)
        self.root.mainloop()
        self.root.mainloop()
            
    def Decrypt (self , Window , tree):
        with open("key.key", "rb") as r:
            k = r.read()
            key = k
            fer = Fernet(key)
        for i in tree.get_children():
            tree.set(i, "two", fer.decrypt(tree.item(i)["values"][1].encode()).decode("UTF-8"))
        Window.DecBut.destroy()
        Window.DecBut = Button(Window.root, text="Encrypt", command=lambda : self.Encrypt(Window.root, Window.treee))
        Window.DecBut.grid(row=1, column=0, columnspan=2)

    def Encrypt (self , Window , tree):
        with open("key.key", "rb") as r:
            k = r.read()
            key = k
            fer = Fernet(key)
        for i in tree.get_children():
            tree.set(i, "two", fer.encrypt(tree.item(i)["values"][1].encode()).decode("UTF-8"))
        Window.EncBut.destroy()
        Window.EncBut = Button(Window.root, text="Decrypt", command=lambda : self.Decrypt(Window.root, Window.treee))
        Window.EncBut.grid(row=1, column=0, columnspan=2)

    def ViewPass(self):
       
        root = Tk()
        root.title("View Password")
        root.geometry("480x480")
        root.configure(background="#2c3e50")
        root.resizable(False, False)
        treee = Treeview(root)
        treee["columns"] = ("one", "two")
        treee.column("#0", width=0, stretch=NO)
        treee.column("one", anchor=W, width=240)
        treee.column("two", anchor=W, width=240)
        treee.heading("one", text="Name", anchor=W)
        treee.heading("two", text="Password", anchor=W)
        treee.grid(row=0, column=0, columnspan=2)
        with open("key.key", "rb") as r:
            k = r.read()
            key = k
            fer = Fernet(key)
        with open("preferiti.txt", "r") as f:
            x = f.readline()
            if x == "Binary":
                with open("binary.dat", "rb") as f:
                    try:
                        while True:
                            a = pickle.load(f)
                            treee.insert(
                                "",
                                "end",
                                values=(a[0], a[1]),
                            )
                    except EOFError:
                        pass
            elif x == "Text":
                with open("text.txt", "r") as f:
                    for line in f:
                        (key, val) = line.split(":")
                        treee.insert(
                            "",
                            0,
                            text="",
                            values=(key, val),
                        )
            elif x == "database":
                con = m.connect(
                    host="localhost",
                    user="root",
                    password="Modern@2021",
                    database="PasswordManager",
                )
                cur = con.cursor()
                cur.execute("SELECT * FROM Passwords")
                for i in cur:
                    treee.insert(
                        "",
                        0,
                        text="",
                        values=(i[1], i[2]),
                    )
        return (root, treee)
      



def EncFile(f, t):
    k =  Fernet.generate_key()
    fer = Fernet(k)
    f=f+".txt"
    with open(f) as j:
        data = j.readline()
        M  = fer.encrypt(data.encode()).decode("UTF-8")
    messagebox.showinfo("Success"  ,  "Encrypted the  File")
    t = t + '.txt'
    with open("Nkey.txt" , 'w') as lxx:
        lxx.write(k.decode())

    with open(t, "w") as n:
        n.write(M)
        n.write("\n")
    messagebox.showinfo("Success" , "File Saved")
    
    
    

def EncData(f, w):
    k = Fernet.generate_key()
    fer = Fernet(k)
    M = fer.encrypt(f.encode()).decode("UTF-8")
    messagebox.showinfo("Success,Encrypted the Data")
    t = w + '.txt'
    with open("Nkey.txt" , 'w') as lxx:
        lxx.write(k.decode())
    with open(t, "a") as n:
        n.write(M)
        n.write("\n")
    messagebox.showinfo("Success" , "File Saved")    






def Encryptdata():
    root1 = Tk()
    root1.title("Encrypt Data")
    root1.geometry("480x240")
    root1.configure(background="#2c3e50")
    root1.resizable(False, False)

    DatLabel = Label(root1, text="Enter Data/File Name", background="#2c3e50", foreground="white")
    DatLabel.grid(row=0, column=0, columnspan=2)
    FileocLable = Label(root1, text="Enter File Name", background="#2c3e50", foreground="white")
    FileocLable.grid(row=1, column=0, columnspan=2)

    Datafile = Entry(root1, width=30)
    Datafile.grid(row=0, column=2)
    FileLoc = Entry(root1, width=30)
    FileLoc.grid(row=1, column=2)
    
    Bfile = Button(root1 ,text = 'filemode', command = lambda: EncFile(Datafile.get(), FileLoc.get())) 
    Bfile.grid(row=0, column=3, padx=20)
    Bdata = Button(root1 ,text = 'datamode', command = lambda: EncData(Datafile.get(), FileLoc.get()))
    u = FileLoc.get()+'.txt'
    Bdata.grid(row=1, column=3, padx=20)
    
    


def DecFile(f, k, t):
    key = k.encode()
    fer = Fernet(key)
    f=f+".txt"
    with open(f) as x:
        y = x.readline()
        m = fer.decrypt(y).decode("UTF-8")
        messagebox.showinfo("Decrypted")
    
    t=t+".txt"
    with open(t, "a") as n:
        n.write(m)
    messagebox.showinfo("File Saved")    


def DecData(f, k , t) :
    
    fer = Fernet(k.encode())
    ll = fer.decrypt(f).decode("UTF-8")
    messagebox.showinfo("Decrypted", ll)
    t=t+".txt"
    with open(t, "a") as n:
        n.write(ll)
    messagebox.showinfo("File Saved")


def Decryptdata():
    root = Tk()
    root.title("Decrypt Data")
    root.geometry("600x240")
    root.configure(background="#2c3e50")
    root.resizable(False, False)

    DataLabel = Label(root, text="Enter the Data/FileName" , width=15)
    DataLabel.config(background="#2c3e50" , foreground = "white")
    DataLabel.grid(row=0, column=0, padx=20)
    KeyLabel = Label(root, text="Enter the Key" , width=15)
    KeyLabel.config(background="#2c3e50" , foreground = "white")
    KeyLabel.grid(row=1, column=0, padx=20)
    FileLocLabel = Label(root, text="Enter the File Location" , width=15)
    FileLocLabel.config(background="#2c3e50" , foreground = "white")
    FileLocLabel.grid(row=2, column=0, padx=20)
    
    DataFile = Entry(root, width=30)
    DataFile.grid(row=0, column=1, padx=20)
    Keyyyyy = Entry(root, width=30)
    Keyyyyy.grid(row=1, column=1, padx=20)
    FileLoc = Entry(root, width=30)
    FileLoc.grid(row=2, column=1, padx=20)
    Bfile = Button(
        root, text="FileMode", command=lambda: DecFile(DataFile.get(), Keyyyyy.get() , FileLoc.get()) , width=30
    )
    Bfile.grid(row=0, column=2, padx=20)
    Bdata = Button(
        root, text="DataMode", command=lambda: DecData(DataFile.get(), Keyyyyy.get() , FileLoc.get()) , width=30
    )
    
    
    Bdata.grid(row=1, column=2, padx=20)


def GeneratePassword(root):
    k = "".join(
        [
            random.choice(string.ascii_letters + string.digits + string.punctuation)
            for n in range(8, 17)
        ]
    )
    pyperclip.copy(k)
    messagebox.showinfo("Password", k)


def main():
    root = Tk()
    root.title("Password Manager")
    root.geometry("572x50")
    root.configure(background="#2c3e50")
    root.resizable(False, False)
    B1 = Button(root, text="Add Password", command=lambda: AddPassword(), width=30)
    B2 = Button(root, text="View Passwords", command=lambda: Log(), width=30)
    B3 = Button(root, text="Encrypt Data", command=lambda: Encryptdata(), width=30)
    B4 = Button(root, text="Decrypt Data", command=lambda: Decryptdata(), width=30)
    B5 = Button(
        root, text="Generate Password", command=lambda: GeneratePassword(root), width=30
    )
    B6 = Button(root, text="Exit", command=lambda: sys.exit(), width=30)
    B1.grid(row=1, column=0, sticky=E)
    B2.grid(row=1, column=1, sticky=E)
    B3.grid(row=1, column=2, sticky=E)
    B4.grid(row=2, column=0, sticky=E)
    B5.grid(row=2, column=1, sticky=E)
    B6.grid(row=2, column=2, sticky=E)
    root.mainloop()


def chkpass(Pass, win):
    with open("key.key", "rb") as r:
        k = r.read()
        key = k
        fer = Fernet(key)

    with open("Master.dat", "rb") as f:
        try:
            x = pickle.load(f)
            o = fer.decrypt(x).decode("utf-8")
            if o == Pass:
                print(True)
                win.destroy()
                main()
            else:
                print(False)

        except EOFError:
            print("End of file")


def master():
    root = Tk()
    root.title("Login")
    root.geometry("480x240")
    root.configure(background="#2c3e50")
    root.resizable(False, False)
    Lab = Label(root, text="Master Password", width=15)
    Lab.config(background= "#2c3e50" , foreground = "white")
    Lab.grid(row=0, column=0, padx=20)
    mp = Entry(root, width=25)
    mp.grid(row=0, column=1, columnspan=2)
    mp.config(show="*")
    b1 = Button(root, text="Login", command=lambda: chkpass(mp.get(), root))
    b1.grid(row=1, column=1, columnspan=2)

    root.mainloop()


def ChkFirstRun():
    print("data ", os.path.isfile("key.key"))
    if (os.path.exists("data.dat") or os.path.exists("data.txt")) or os.path.exists(
        "key.key"
    ):
        master()
    else:
        if os.path.exists("key.key"):
            pass
        else:
            key = Fernet.generate_key()
            with open("key.key", "wb") as key_file:
                key_file.write(key)
        root = Tk()
        root.title("First Run")
        root.geometry("480x240")
        root.configure(background="#2c3e50")
        root.resizable(False, False)
        mp = Entry(root, width=50)
        mp.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        mp.config(show="*")
        b1 = Button(
            root,
            text="Set Master Password",
            command=lambda: SetMasterPassword(mp.get()),
            width=20,
        )
        b2 = Button(root, text="Binary", command=lambda: Biget(), width=20)
        b3 = Button(root, text="Text", command=lambda: Textet(), width=20)
        b4 = Button(root, text="Database", command=lambda: Database(), width=20)
        b1.grid(row=1, column=0, padx=10, pady=10)
        b2.grid(row=1, column=1, padx=10, pady=10)
        b3.grid(row=2, column=0, padx=10, pady=10)
        b4.grid(row=2, column=1, padx=10, pady=10)
        root.mainloop()


ChkFirstRun()
