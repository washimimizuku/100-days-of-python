student_heights = input("Input a list of student heights separated by spaces: ").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
    
total = 0
count = 0
for student_height in student_heights:
  total += student_height
  count += 1

print(total//count)