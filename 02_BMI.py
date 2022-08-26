


h=eval(input("Enter your height in metres:"))
w=eval(input("Enter you weight in Kgs:"))
bmi=round((w/(h**2)))
if bmi<18.5:
    print(f"Your BMI is {bmi}, and you are UNDEWEIGHT.")
elif bmi<25:
    print(f"Your BMI is {bmi}, and you are NORMAL WEIGHT")
elif bmi<30:
    print(f"Your BMI is {bmi}, and you are OVER WEIGHT")
elif bmi<35:
    print(f"Your BMI is {bmi}, and you are OBESE")
else:
    print(f"Your BMI is {bmi}, and you are CLINICALLY OBESE")