import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',\
     'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', '\
    z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',\
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to password generator.")
len_of_pass=int(input("How many letters would you like in your password?:\n"))
no_of_symb=int(input("How many symbols would you like in your password:\n"))
no_of_num=int(input("How many numbers would you like in your password:\n"))

password=""

# for char in range(1,len_of_pass+1):
#     password+=random.choice(letters)

# for char in range(1,no_of_symb+1):
#     password+=random.choice(symbols)

# for char in range(1,no_of_num+1):
#     password+=random.choice(numbers)

# random.shuffle(password)

# print(password)

password_list=[]

for char in range(1,len_of_pass+1):
    password_list.append(random.choice(letters))

for char in range(1,no_of_symb+1):
    password_list.append(random.choice(symbols))

for char in range(1,no_of_num+1):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)

for char in password_list:
    password+=char

print(f"Your password is {password}")