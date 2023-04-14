n=input("Enter the numbers with one space : ").split() #split stores data in list 
for i in range(0,len(n)):
    n[i]=int(n[i])   # since stored in list is string we use  loop to change to int

print(n) # this is our list with int values

sum=0
for i in range(0,len(n)+1):
    sum+=i
print(sum)
average=sum/len(n)+1
print(average)


# def average():
#     n=input("Enter the ten numbers : ").split()
#     for i in range(0,len(n)):
#         n[i]=int(n[i])
#     sum=0
#     for i in range(0,len(n)+1):
#         sum+=i
#     average=(sum/len(n)+1)
    


