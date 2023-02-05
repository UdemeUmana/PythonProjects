#Creating a simple python generator

#Importing a python library-random
import random
#Creating alist of random words and storing thrm to a variable
Chars = "abcdefgh554ijklmnopqrstuv1wx@#y33zABC4DEFGHIJKLMetNOPQRSTUVWXewYZ123456789!@#$%^&*()"
while 1:
    password_len = int(input("What length would you like your password to be : "))
    password_count = int(input("How many passwords would you like : "))
    for x in range(password_count):
        password = ""
        for x in range(password_len):
            password_char = random.choice(Chars)
            password = password + password_char
        print("Here is your random password : ", password)
        