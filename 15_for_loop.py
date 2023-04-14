# fruits=["apple","banana","pears","berry"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit + "Pie")
# print(fruits)


student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

print(student_heights)


total_height=0
for height in student_heights:
    total_height+=height
print(total_height)

total_no_of_students=0
for students in student_heights:
    total_no_of_students+=1
print(total_no_of_students)

average=(total_height)/(total_no_of_students)
print(f"average height of given {total_no_of_students} students is {average}")