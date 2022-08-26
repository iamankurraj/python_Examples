import colorama
from colorama import Fore
print("Welcome to treasure island, you have to find the chest!")
d1=input("Choose left or right:\n").lower()
if d1=="left":
    d2=input("swim or boat:\n").lower()
    if d2==("boat"):
        d3=input("Which door:blue/yellow/red\n").lower()
        if d3==("yellow"):
            print("You Win!")
        else:
            print("Game Over.")
    else:
        print("Game Over")
else:
    print(Fore.BLUE+"Game Over")
    
    
