print("Welcome to pythong pizza deliveries.")
size=input("Whats size pizza do you want? S,M,L \n")
add_pepperoni=input("Do you want Pepperoni? Y or N \n")
extra_cheese=input("Do you want extra cheeze? Y or N \n")

bill=0

if size=="S":
    bill+=15
    if add_pepperoni=="Y":
        bill+=2
elif size=="M":
    bill+=20
    if add_pepperoni=="Y":
        bill+=3
elif size=="L":
    bill+=25
    if add_pepperoni=="Y":
        bill+=3
if extra_cheese=="Y":
    bill+=1


print(f"Your final bill is {bill} $.")
