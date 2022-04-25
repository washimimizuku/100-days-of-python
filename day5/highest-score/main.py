student_scores = input("Input a list of student scores separated by spaces: ").split()

for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

highest = 0
for student_score in student_scores:
    if highest < student_score:
        highest = student_score

print(f'The highest score in the class is: {highest}')
