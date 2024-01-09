for number in range(1, 11):
    print(number)
    
total = 0

for mnumber in range(1, 101):
    total += mnumber
print(total)


target = int(input()) # Enter a number between 0 and 1000
# Do not change the code above 

# Write your code here 

even_sum = 0
for number in range(2, target + 1, 2):
    even_sum += number
print(even_sum)

# or

# alternative_sum = 0
# for number in range(1, target + 1):
#   if number % 2 == 0:
#     alternative_sum += number
# print(alternative_sum)

## buzz

target = 100
for number in range(1, target + 1):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)
