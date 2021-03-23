student_dict = {
    "student": ["Alex", "Nuno", "Angela"],
    "score": [56, 76, 98]
}

# Loop through dictionaries
for (key, value) in student_dict.items():
    print(key)
    print(value)

import pandas
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# Loop through a data frame
for (key, value) in student_data_frame.items():
    print(key)
    print(value)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    print(index)
    print(row)
    print(row.student)
    print(row.score)
    