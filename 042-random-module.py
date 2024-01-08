import random

# random_integer = random.randint(1, 10)
# print (random_integer)


head_tails = random.randint(0, 1)

if head_tails == 1:
    print("Heads")
else:
    print("Tails")
    

## list random

names_string = "Angela, Ben, Jenny, Michael, Chloe"
names = names_string.split(", ")

# Get the total number of items in list.
num_items = len(names)
# Generate random numbers between 0 and the last index. 
random_choice = random.randint(0, num_items - 1)
# Choose and print a random name.
print(names[random_choice])