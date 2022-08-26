from operator import index


a=[2,4,5,6,7,9]
b=[3,6,7,8,9,2]

sum_list=[]
for i in range(0,len(a)):
    sum_list.append(a[i]+b[i]) #adding corresponding elements one by one
print(sum_list) # making a list of corresponding sums so that its easy to bring out max value
index=(sum_list.index(max(sum_list))) # finding the index number of maximum value

print(f"Maximum value of sum of corresponding list element is {max(sum_list)} and index value of elements is\
    {index} and elements are {a[index]} and {b[index]}.")
# {max(sum_list)} gives highest value of addition of corresponding elements from both lists

print(sum_list.index(max(sum_list)))