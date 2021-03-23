import os

LOCATION = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
FILENAME1 = "file1.txt"
FILENAME2 = "file2.txt"
FULL_PATH1 = os.path.join(LOCATION, FILENAME1)
FULL_PATH2 = os.path.join(LOCATION, FILENAME2)

with open(FULL_PATH1) as file1:
    file1_list = [int(number.strip()) for number in file1.readlines()]

with open(FULL_PATH2) as file2:
    file2_list = [int(number.strip()) for number in file2.readlines()]

result = [number for number in file1_list if number in file2_list]
print(result)