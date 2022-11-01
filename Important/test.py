import pickle
from  cryptography.fernet import Fernet as F 
with open('master.dat' ,'rb' ) as f:
    master = pickle.load(f)
print(master)
key = 'Raq7IMZ4QkqK2Oj7lKT3bxJTgwxeJFYx4ADjTqVKdQY='
fey = F(key)
print(fey.decrypt(master).decode('utf-8'))