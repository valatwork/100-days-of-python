# num_char = len(input("What is your name?"))
# # print(type(num_char))
# new_num_char = str(num_char)
# print("Your name has " + new_num_char + " characters")

two_digit_number = input()

first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])

two_digit_number = first_digit + second_digit

print(two_digit_number)


## BMI calculator

height = input()
weight = input()
# Your code below this line 
weight_as_int = int(weight)
height_as_float = float(height)
bmi = weight_as_int / (height_as_float * height_as_float)
bmi_as_int = int(bmi)
print(bmi_as_int)