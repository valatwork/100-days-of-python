# bill = input("What was the total bill?")
# percentage = input("How much tip would you linke to give? 10, 12, or 15?")
# people = input("How many people will split the bill?")

# bill_as_float = float(bill)
# percentage_as_int = int(percentage)
# people_as_int = int(people)
# tip = (round(((bill_as_float / people_as_int) * percentage_as_int / 10) , 2))

# print(f"Each person should pay {tip}")


print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill?"))

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)


# FAQ: How to round to 2 decimal places?

# Find the answer in the Q&A here: https://www.udemy.com/course/100-days-of-code/learn/lecture/17965132#questions/13315048


print(f"Each person should pay: ${final_amount}")