"""
from rich.console import Console
from rich import Input 
Input = Input()
from rich.traceback import install
install()
console =Console()
from rich.prompt import Prompt
k = Input("hi",style='bold red')"""
#import csv
#from cryptography.fernet import Fernet
#key = input("Enter the key  ")
#fer = Fernet(key)
#f = open("spotify.csv","w")
#s = csv.writer(f)
#k = input("enter a para")
#o = s.writerow([k])
"""
f = open("spotify.csv",'r')
s = csv.reader(f)
for i in s :
    for j in i:
        m = fer.encrypt(j.encode()).decode()
        print("  ")
        print(m)

f = open("spotify.txt")
k =f.readline()
print(" ")
m = fer.encrypt(k.encode()).decode()
print(m)
"""
import pygame





