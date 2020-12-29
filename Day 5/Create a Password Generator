#Password Generator Project

import random
import secrets
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

#password = ""

#for value_of_input in range(nr_letters):
#  password += secrets.choice(letters)

#for input_num in range(nr_numbers):
#  password += secrets.choice(numbers)

#for input_num in range(nr_symbols):
#  password += secrets.choice(symbols)

#print(password)

#########################################################################################
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password_list = []

for input in range(nr_letters):
  password_list += secrets.choice(letters)

for input in range(nr_numbers):
  password_list += secrets.choice(numbers)

for input in range(nr_symbols):
  password_list += secrets.choice(symbols)

random.shuffle(password_list)

final_pass = ""
for char in password_list:
  final_pass += char

print(f"Your password is: {final_pass}")
