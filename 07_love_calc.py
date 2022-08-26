print("Welcome to love calculator!")
name1=input("What is your name:\n")
name2=input("What is their name:\n")
combined_str=name1+name2
lower_case_string=combined_str.lower()
t=lower_case_string.count("t")
r=lower_case_string.count("r")
u=lower_case_string.count("u")
e=lower_case_string.count("e")
l=lower_case_string.count("l")
o=lower_case_string.count("o")
v=lower_case_string.count("v")
e=lower_case_string.count("e")
final_score=(str((t+r+u+e))+str((l+o+v+e)))
print("Your name:" , name1)
print("Their name:", name2)
print("Your love score is:", final_score)


