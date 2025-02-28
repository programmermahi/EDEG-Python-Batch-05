# Get the name from the user
name = input("Enter your name: ")

# Check if the name is between 5 and 10 characters and starts with 'a'
if len(name) >= 5 and len(name) <= 10:
    if name[0].lower() == 'a':
        print("Name is valid")
    else:
        print("Name should start with 'a'")
else:
    print("Name should contain 5 or more and less than 10 characters")


# Get age and marks from the user
age = int(input("Enter your age: "))
marks = float(input("Enter your marks: "))

# Check if the user meets the conditions
if age >= 18:
    if 90 < marks < 100:
        print("You are selected")
    else:
        print("Marks should be greater than 90 and less than 100")
else:
    print("Age should be 18 or greater")
