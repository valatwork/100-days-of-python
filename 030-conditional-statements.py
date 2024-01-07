print("Welcome to the rollercostaer!")
height = int(input("What is your heigt in cm?"))

if height >= 120: 
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?"))
    if age < 12:
        print("Please pay $2")
    elif age <= 18:
        print("Please pay $7")
    else:
        print("Please pay $12")
else:
    print("Sorry, you have to grow taller before you can ride.")
    
    
    

# Which year do you want to check?
year = int(input())

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not leap year")
    else:
        print("Leap year")
else:
  print("Not leap year")
  
  
  
print("Welcome to the rollercostaer!")
height = int(input("What is your heigt in cm?"))
bill = 0

if height >= 120: 
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?"))
    if age < 12:
        bill = 5
        print("Please pay $2")
    elif age <= 18:
        bill = 7
        print("Please pay $7")
    else:
        bill = 12
        print("Please pay $12")
    wants_photo = input("Do you want a photo taken?")
    if wants_photo == "Y":
       bill += 3 
    
    print(f"Your final bill is {bill}")
    
else:
    print("Sorry, you have to grow taller before you can ride.")
    