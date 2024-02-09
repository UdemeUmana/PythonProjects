#The goal is to build a password generator. The passwords will be generated using random words

#importing the libraries we need
import random
import string

#prompting the user to enter the length of the password
length = int(input("Enter length: "))

#concatenating the ascii_letters,digits and punctuation together

char = string.ascii_letters
char += string.digits
char += string.punctuation

#creating the password variable being an empty string
password = ""

#creating a loop to run length for a particular number of time for the length number of characters for the password
for i in range (length):
    password  += random.choice(char)

print("Your random password is: ", password)