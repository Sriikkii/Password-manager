#import argparse
import rich
import colorama
from colorama import init
init()
from rich.console import Console
console = Console()
from rich.traceback import install
install()
from colorama import Fore, Back, Style
from rich import print 
from rich.tree import Tree
import os
import pickle
import csv                        
import os
try:
    import pandas as pd
except:
    os.system("pip install pandas")
import pandas as pd
try :
    import pyperclip
except:
    os.system("pip install pyperclip")

try :
    import cryptography
except:
    os.system('pip install cryptography')

import cryptography


try :
    import pwinput
except:
    os.system('pip install pwinput')


from cryptography.fernet import Fernet


def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


key = load_key()
fer = Fernet(key)

#I = open("passwords.txt","a")
#I.write("Username " + "|" + "Passwords" + "\n")
#I.close()

#J = open("pswd.txt","a")
#J.write("username " + "|" + " Password" + "\n")
#J.close()



def view():
    df = pd.read_csv("passwords.txt",sep='|')
    #print(df)
    #ch = input("you want to know your password ? pls enter y to continue ").lower()
    x = input(Fore.CYAN + "enter the Username you want to check ")
    y = df[df['Username ']== x ]
    print(f"[green]{y}[/green]")
    j = input(Fore.BLACK+"do you like the password to be in  clipboard (Y/N) ").upper()
    if j == 'Y':
        o = int(input(Fore.MAGENTA+"enter the index number "))
        u = df._get_value( o , 'Passwords')
        pyperclip.copy(u)
        print("[pink]Copied to your clipboard[/pink]")
        d = input(Fore.LIGHTYELLOW_EX+"you wish to decode the password (Y/N) ? ").lower()
        if d == 'y' :
            B = fer.decrypt(u.encode()).decode()
            pyperclip.copy(B)
            print("[pink]copied to your clipboard[/pink]")
        else:
            pass
    else:
        pass
    h = input(Fore.CYAN+"Do you wish to see the full table ? (Y/N) ").upper()

    if h  == 'Y':
        for i in range(1):
            q = pwinput.pwinput(Fore.LIGHTRED_EX+"enter the secondary master pswd ") 
            t = open("decryp",'r')
            r = t.read()
            t.close()
            if q == r :
                print(df)
            else:
                print(Fore.RED+"Incorrect password")
    
    """
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| Password:",
                  fer.encrypt(passw.encode()).decode())"""
def view2(): 
    print("[red]Note only clipboard option is only available for encrypted passwords[/red]")

    df = pd.read_csv("pswd.txt",sep='|')
    #print(df)
    #ch = input("you want to know your password ? pls enter y to continue ").lower()
    
    h = input(Fore.GREEN+"Do you wish to see the Contents  ? (Y/N) ").upper()

    
    for i in range(1):
        q = pwinput.pwinput(prompt=Fore.LIGHTRED_EX +"enter the secondary master pswd ",mask="*") 
        g = pwinput.pwinput(prompt=Fore.LIGHTBLUE_EX+"enter the master pswd ",mask="*")
        v = open("h.txt",'r')
        w = v.read()
        if g == w :
            t = open("decryp",'r')
            r = t.read()
            t.close()
            if q == r :
                y = input(Fore.CYAN+"You wish to see the full contents (Y/N) ? or specific username (S) ?  ").lower()
                if y == 'y':
                    print(df)
                elif y == 's':
                    b = input(Fore.WHITE +"enter the Username you want to check ")
                    a = df[df['username']== b ]
                    print(a)
            else:
                print("[red]Incorrect password[/red]")
                break
        else:
            print("[red]Incorrect Master password[/red]")
            break
        
    
                    
                    
    """  
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            f.write("User:", user, "| Password:",
                  fer.decrypt(passw.encode()).decode())"""
                     


def add():
    name = input('Account Name: ')
    pwd = pwinput.pwinput(prompt=Fore.MAGENTA +'Password  ', mask='*')
    with open("pswd.txt",'a') as h:
        h.write(name + "|" + pwd + "\n")

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")



def en_de():
    g = input(Fore.CYAN + "Do you want to encrypt or decrypt a file(f) or a message(m) ").lower()
    if g == 'm':
        k = input(Fore.BLUE+'enter the key')
        ch = input(Fore.LIGHTBLUE_EX +"Do you want to encrypt your message or decrypt your message ?(E/D)").upper()
        if ch == 'E' :
            fer = Fernet(k)
            M = input(Fore.GREEN+"enter your decrypted message ")
            K = fer.encrypt(M.encode()).decode()
            j = input(Fore.LIGHTMAGENTA_EX +" would you like to save this in a file (Y/N)").upper()
            if j == 'Y':
                f_name = input(Fore.WHITE+"enter the file name")
                choice = input(Fore.LIGHTCYAN_EX +"Choice of 1 for TEXT FILE  2 for CSV file 3 for BINARY FILE ")
                if choice == '1':
                    F = f_name + '.txt'
                    f = open(F,'a')
                    f.write(M + "|" + K+ "\n")
                    f.close()
                    pass
                elif choice == '2' :
                    L = f_name + '.csv'
                    l = open(L,'a')
                    sw = csv.writer(l,delimiter='|',lineterminator='\n')
                    sw.writerow(['Decrypted','Encrypted'])
                    t = [M,K]
                    sw.writerow(t)
                    l.close()
                    pass
                else:
                    p = []
                    b = f_name + '.dat'
                    s = open(b,'ab')
                    p.append([M,K])
                    pickle.dump(p,s)
                    pass
            else:
                print(K)

        else:
            fer = Fernet(k)
            G = input(Fore.LIGHTGREEN_EX+"enter your Encrypted message to Decrypt")
            V = fer.decrypt(G.encode()).decode()
            o = input(Fore.LIGHTBLUE_EX +" would you like to save this in a file (Y/N)").upper()
            if o == 'Y':
                e_name = input(Fore.WHITE+"enter the file name")
                choice = input(Fore.CYAN+"Choice of 1 for TEXT FILE  2 for CSV file 3 for BINARY FILE")
                if choice == '1':
                    u = e_name + '.txt'
                    y = open(u,'a')
                    y.write(G + "|" + V+ "\n")
                    y.close()
                elif choice == '2' :
                    i = e_name + '.csv'
                    I = open(i,'a')
                    sw = csv.writer(I,delimiter='|',lineterminator='\n')
                    sw.writerow(['Decrypted','Encrypted'])
                    d = [G,V]
                    sw.writerow(d)
                    I.close()
                else:
                    g = []
                    B = e_name + '.dat'
                    S = open(B,'ab')
                    g.append([G,V])
                    pickle.dump(g,S)
            else:
                print(V)
    elif g == 'f':
        for i in range(1):
            print("[red] we can only encrypt or decrypt TEXT FILE OR CSV FILE")
            q = input(Fore.LIGHTGREEN_EX+"Do you wish to encrypt(E) or decrypt your file(D) ").upper()
            if q == 'E':
                K = input(Fore.LIGHTMAGENTA_EX+"Enter the key: ")
                fer = Fernet(K)
                B = input(Fore.LIGHTYELLOW_EX+"Enter the file format T for TEXT FILE AND C FOR CSV FILE ").upper()
                if B == 'T':
                    r = input(Fore.MAGENTA+'Enter the file name')
                    textfile_name = r + '.txt'
                    txt = open(textfile_name,'r')
                    c = txt.readline()
                    L = fer.encrypt(c.encode()).decode()
                    print("[purple4]Succesfully encrypted[/purple4]")
                    qq = input(Fore.LIGHTWHITE_EX+'you want to save it in a file ? (Y/N ').upper()
                    if qq == 'Y':
                        A = input(Fore.LIGHTBLUE_EX+Style.DIM+'Enter a file name so we can store the data ')
                        E = A + '.txt'
                        T = open(E,'a')
                        T.write(L)
                        T.write('\n')
                        T.close()
                    else:
                        print("[slate_blue1]Thank you[/slate_blue1]")
                        break
                elif B == 'C':
                    a = input(Fore.LIGHTMAGENTA_EX+Style.DIM+'Enter the file name : ')
                    U = a + '.csv'
                    W = open(U,'r')
                    _p = csv.reader(W)
                    for ii in _p :
                        for jj in ii:
                            ww = fer.encrypt(jj.encode()).decode()
                            print("[purple4]Succesfully encrypted[/purple4]")
                            ee = input(Fore.LIGHTWHITE_EX+'you want to save it in a file ? (Y/N ').upper()
                            if ee == 'Y':
                                AA = input(Fore.LIGHTBLUE_EX+Style.DIM+'Enter a file name so we can store the data ')
                                EE = AA + '.csv'
                                TT = open(EE,'a')
                                RR = csv.writer(TT)
                                RR.writerow([ww])
                                print(f'[dark_olive_green2]Succesfully created the file {EE} ')
                            else:
                                print("[slate_blue1]Thank you[/slate_blue1]")
                                break
                else:
                    print("[red]Invalid choice[/red]")
            elif q == 'D':
                
                BB = input(Fore.LIGHTYELLOW_EX+"Enter the file format T for TEXT FILE AND C FOR CSV FILE ").upper()
                if BB == 'T':
                    K1 = input(Fore.YELLOW+Style.BRIGHT+'Enter the key: ')
                    fer = Fernet(K1)
                    rr = input(Fore.MAGENTA+'Enter the file name ')
                    textfile_name1 = rr + '.txt'
                    TXT = open(textfile_name1,'r')
                    X = TXT.readline()
                    O = fer.decrypt(X.encode()).decode()
                    print("[purple4]Succesfully Decrypted[/purple4]")
                    CC = input(Fore.LIGHTWHITE_EX+'you want to save it in a file ? (Y/N ').upper()
                    if CC == 'Y':
                        aa = input(Fore.LIGHTBLUE_EX+Style.DIM+'Enter a file name so we can store the data ')
                        mm = aa + '.txt'
                        xx = open(mm,'a')
                        xx.write(O)
                        xx.write('\n')
                        xx.close()
                        print(f'[dark_olive_green2]Succesfully created the file {mm} ')
                    else:
                        print("[slate_blue1]Thank you[/slate_blue1]")
                        break
                elif BB == 'C':
                    _a = input(Fore.LIGHTMAGENTA_EX+Style.DIM+'Enter the file name: ')
                    _U = _a + '.csv'
                    _W = open(_U,'r')
                    __p = csv.reader(W)
                    for ki in __p :
                        for kj in i:
                            _ww = fer.decrypt(kj.encode()).decode()
                            print("[purple4]Succesfully Decrypted[/purple4]")
                            _ee = input(Fore.LIGHTWHITE_EX+'you want to save it in a file ? (Y/N ').upper()
                            if _ee == 'Y':
                                _AA = input(Fore.LIGHTBLUE_EX+Style.DIM+'Enter a file name so we can store the data')
                                _EE = _AA + '.csv'
                                _TT = open(_EE,'a')
                                _RR = csv.writer(_TT)
                                _RR.writerow([_ww])
                                print(f'[dark_olive_green2]Succesfully created the file {_EE} ')
                            else:
                                print("[slate_blue1]Thank you[/slate_blue1]")
                                break

def create ():
    print('Your creating your own Encrypted message')
    print("[red]If you want to save it in a File ,  Only Text file is supported[/red]")
    key = Fernet.generate_key()
    Q = input("enter a name so that we can store your key ")
    k = Q + '.key'
    key_file = open(k,"wb")
    key_file.write(key)
    key_file.close()
    file = open(k,'rb')
    Key = file.read()
    file.close()
    key = Key
    fer = Fernet(key)
    O = input(Fore.MAGENTA+Style.BRIGHT+'Do you want to encode a file(f) or a small message(m)').lower()
    if O  == 'm':
        j = input(Fore.BLUE+'enter a message ')
        m = fer.encrypt(j.encode()).decode()
        print("[purple3]Succesfully Encrypted your data [/purple3]")
        u = input(Fore.GREEN+Style.BRIGHT+'Do you want to copy it your clipboard (y/n) : ')
        if u == 'y':
            pyperclip.copy(m)
        else:
            pass
        h = input(Fore.LIGHTWHITE_EX+Style.BRIGHT+"Do you want to save it in a file (Y/N) : ").upper()
        if h == 'Y':
            y = input(Fore.CYAN+"enter a  file name so that we can store the data: ")
            f = y + '.txt'
            t = open(f,'a')
            t.write(m)
            t.write('\n')
            t.close()
            print(f"[violet]Succesfully stored your encrpyted data in {f}[/violet]")
        else:
            print("[gold3] Thank you [/gold3]")
    elif O == 'f' :
            l = input(Fore.LIGHTYELLOW_EX+Style.DIM+'Enter the file name : ')
            M = fer.encrypt(l.encode()).decode()
            print("[purple3]Succesfully Encrypted your data [/purple3]")
            g = input(Fore.LIGHTWHITE_EX+Style.BRIGHT+"Do you want to save it in a file (Y/N) : ").upper()
            if g == 'Y':
                Y = input(Fore.CYAN+"enter a name in which we can store the data: ")
                r = Y + '.txt'
                T = open(f,'a')
                T.write(m)
                T.write('\n')
                T.close()
                print(f"[violet]Succesfully stored your encrpyted data in {Y}[/violet]")
            else:
                print("[gold3] Thank you [/gold3]")
    else:
        pass
"""
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('option', help='add / view / Encrypt & Decrypt')
    parser.add_argument("-add", type = str, help = "add your password and username")
    parser.add_argument("-view",type = str, help = "view your data")
    parser.add_argument("-view2",type = str , help = "view your data in decrypted form")
    parser.add_argument("-ed",type = str ,help = "encode or decode your message")
    

    args = parser.parse_args()
    print(args.add)
    print(args.view)
    print(args.view2)
    print(args.ed)

    if args.option == "add":
        add()
    elif args.option == "view":
        view()
    elif args.option == "view2":
        view2()
    elif args.option == "ed":
        en_de()"""

while True:
    j = open("h.txt",'r')
    o = j.read()
    j.close()
    Master_Pswd = pwinput.pwinput(prompt=Fore.LIGHTBLUE_EX+'Master pswd ' , mask='*')
    if Master_Pswd == o :
        print('[green]Good To Go[/green]')
        

        tree = Tree("[turquoise2]Password Manager and decryption[turquoise2]")
        tree.add("[violet]Add your passowrd [/violet]")
        tree.add("[green]View your passwords [/green]")
        tree.add("[green3]Encrypt your data[/green3]").add("[chartreuse]Encrypt your file[/chartreuse]")
        tree.add("[blue]Decrypt your data[/blue]").add("[sky_blue1]Decrypt your data[/sky_blue1]")
        tree.add("[gold3]Create your data[/gold3]")

        print("[deep_pink4]The options are : [/deep_pink4]")
        print(tree)


        
    else:  
        print('[red]Wrong Password[/red]') 
        break

    mode = input(Fore.CYAN+
        "Would you like to add a new password or view existing ones (view, add), Encrypt or Decrypt your data (ed), Create your own encrypted data(Note no need of key instead we will provide you one) (c) ,press q to quit? ").lower()
    if mode == "q":
        break

    if mode == "view":
        ch = input(Fore.MAGENTA+"Would You like to see the encoded or decoded pswd ? for encrypted pswd enter 'E' or for dercrypted pswd enter 'D'").upper()
        if ch == 'E':
            view()
        else:
            l = open("decryp",'r')
            d = l.read()
            l.close()
            view2()
              
    elif mode == "add":
        add()
    elif mode == 'ed':
        en_de()
    elif mode == 'c':
        create()
    else:
        print(Fore.RED+"Invalid mode.")
        continue




"""alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char
  print(f"Here's the {cipher_direction}d result: {end_text}")
should_end = False
while not should_end:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
 
  shift = shift % 26
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if restart == "no":
    should_end = True
    print("Goodbye") """