student_score=input("Enter the list of score: ").split()
for n in range(0, len(student_score)):
    student_score[n]=int(student_score[n])
print(student_score)

highest_score=0
for score in student_score:
    if score > highest_score:
        highest_score=score

print(f"The highest score in class is: {highest_score}")

