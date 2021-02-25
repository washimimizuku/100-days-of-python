import math

def paint_calc(height, width, cover):
    number_of_cans = math.ceil(height * width / cover)
    return number_of_cans

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5

number_of_cans = paint_calc(height=test_h, width=test_w, cover=coverage)    
print(f"You'll need {number_of_cans} cans of paint.")  
