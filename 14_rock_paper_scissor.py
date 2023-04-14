
import random

value=int(input("Press 1 for rock 2 for scissor and 3 for paper:\n"))
a=random.randint(1, 3)

if value==1:
    print("You chose rock.")
    if a==1:
        print("Computer chose rock and its draw.")
    elif a==2:
        print("Computer chose scissor and you won.")
    elif a==3:
        print("Computer chose paper and you lose.")
if value==2:
    print("You chose paper.")
    if a==1:
        print("Computer chose rock and you win.")
    elif a==2:
        print("Computer chose scissor and you lose.")
    elif a==3:
        print("Computer chose paper and its draw.")
if value==3:
    print("You chose paper.")
    if a==1:
        print("Computer chose rock and you win.")
    elif a==2:
        print("Computer chose scissor and you lose.")
    elif a==3:
        print("Computer chose paper and its draw.")
    