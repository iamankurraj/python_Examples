# num=int(input("Enter the number:"))
# if num%2==0:
#     print("Number is even")
# else:
#     print("Given number is odd")

bill=0

height=int(input("Enter your height:\n"))
if height>=120:
    print("You are eligible for ride.")
    age=int(input("Enter your age"))
    if age<=12:
        bill=5
        print("child tickets are $5")
    elif age<=18:
        bill=12
        print("Teenage tickets are $12")
    elif age>=45 and age<=50:
        bill=0
        print("You dont have to pay!")
    else:
        bill=15
        print("adult tickets are 15")
        
    wants_photo=input("Do you want a photo taken? Type Y for yes and N for no:\n")
    if wants_photo=="Y":
        bill=bill+3
    print(f"Print yout final bill is{bill}.")

else:
    print("You need to grow taller.")
