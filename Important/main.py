from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from cryptography.fernet import Fernet
import mysql.connector as m
import pickle
import os
import string
import random


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
    Name.grid(row=0, column=1, padx=20)
    Password = Entry(root, width=30)
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
            with open("binary.dat", "rb") as f:
                try:
                    y = pickle.load(f)
                except EOFError:
                    y = []
            y.append(Name)
            y.append(fer.encrypt(Password).encode())
            with open("binary.dat", "wb") as f:
                pickle.dump(y, f)
        elif x == "Text":
            with open("text.txt", "a") as f:
                f.write(
                    Name + ":" + fer.encrypt(Password.encode()).decode("UTF-8") + "\n"
                )
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


def ViewPassword():
    # Show the deatils in a tree
    root = Tk()
    root.title("View Password")
    root.geometry("202x230")
    root.configure(background="#2c3e50")
    root.resizable(False, False)
    treee = Treeview(root)
    treee["columns"] = ("one", "two")
    treee.column("#0", width=0, stretch=NO)
    treee.column("one", anchor=W, width=100)
    treee.column("two", anchor=W, width=100)
    treee.heading("one", text="Name", anchor=W)
    treee.heading("two", text="Password", anchor=W)
    treee.grid(row=0, column=0, columnspan=2)
    with open("key.key", "r") as r:
        k = r.read()
    fer = Fernet(k)

    with open("preferiti.txt", "r") as f:
        x = f.readline()
        if x == "Binary":
            with open("binary.dat", "rb") as f:
                try:
                    y = pickle.load(f)
                except EOFError:
                    y = []
            for i in range(0, len(y), 2):
                treee.insert(
                    "",
                    0,
                    text="",
                    values=(y[i], fer.decrypt(y[i + 1].encode()).decode("UTF-8")),
                )
        elif x == "Text":
            with open("text.txt", "r") as f:
                for line in f:
                    (key, val) = line.split(":")
                    treee.insert(
                        "",
                        0,
                        text="",
                        values=(key, fer.decrypt(val.encode()).decode("UTF-8")),
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
                    values=(i[1], fer.decrypt(i[2].encode()).decode("UTF-8")),
                )
    root.mainloop()


def Encryptdata():
    with open("key.key", "rb") as r:
        k = r.read()
        key = k
        fer = Fernet(key)
        o = input()

        E = fer.encrypt().decode("UTF-8")
        with open("key.key", "wb") as f:
            pickle.dump(E, f)


def DecFile(f, k):
    key = k
    fer = Fernet(key)

    with open(f) as x:
        y = x.readline()
        m = fer.decrypt(y).decode("UTF-8")
        messagebox.showinfo("Decrypted", m)


def DecData(f, k):
    fer = Fernet(k)
    ll = fer.decrypt(f).decode("UTF-8")
    messagebox.showinfo("Decrypted", ll)


def Decryptdata():
    root = Tk()
    root.title("Decrypt Data")
    root.geometry("480x240")
    root.configure(background="#2c3e50")
    root.resizable(False, False)
    DataFile = Entry(root, width=30)
    DataFile.grid(row=0, column=1, padx=20)
    Keyyyyy = Entry(root, width=30)
    Keyyyyy.grid(row=1, column=1, padx=20)
    Bfile = Button(
        root, text="FileMode", command=lambda: DecFile(DataFile.get(), Keyyyyy.get())
    )
    Bfile.grid(row=2, column=1, padx=20)
    Bdata = Button(
        root, text="DataMode", command=lambda: DecData(DataFile.get(), Keyyyyy.get())
    )
    Bdata.grid(row=3, column=1, padx=20)


def GeneratePassword(root):
    k = "".join(
        [
            random.choice(string.ascii_letters + string.digits + string.punctuation)
            for n in range(8, 17)
        ]
    )
    messagebox.showinfo("Password", k)


def main():
    root = Tk()
    root.title("Password Manager")
    root.geometry("572x50")
    root.configure(background="#2c3e50")
    root.resizable(False, False)
    B1 = Button(root, text="Add Password", command=lambda: AddPassword(), width=30)
    B2 = Button(root, text="View Passwords", command=lambda: ViewPassword(), width=30)
    B3 = Button(root, text="Encrypt Data", command=lambda: Encryptdata(), width=30)
    B4 = Button(root, text="Decrypt Data", command=lambda: Decryptdata(), width=30)
    B5 = Button(
        root, text="Generate Password", command=lambda: GeneratePassword(root), width=30
    )
    B6 = Button(root, text="Exit", command=lambda: root.destroy(), width=30)
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

    with open("master.dat", "rb") as f:
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
    mp = Entry(root, width=50)
    mp.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
    mp.config(show="*")
    b1 = Button(root, text="Login", command=lambda: chkpass(mp.get(), root))
    b1.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

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
