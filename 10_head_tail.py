import random
# coin_sides=random.randint(0,1)
# if coin_sides==0:
#     print("Heads")
# else:
#     print("Tails")

payer=input("Enter the names\n")
a=payer.split(", ")
print(a)
b=random.randint(0,len(a)-1)
print(a[b])
