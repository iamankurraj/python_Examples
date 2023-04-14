age=int(input("Enter your age:"))
#assuming living age to be 90years
yearsleft= 90-age
months=yearsleft*12
weeksleft=yearsleft*52
daysleft=weeksleft*7
print(f"You have{daysleft}days,{weeksleft}weeks,{months}months left.")
