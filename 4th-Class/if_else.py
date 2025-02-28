# Get a number from the user
number = int(input("Enter a number: "))

# Check if the number is even or odd
if number % 2 == 0:
    print("Number is Even")
else:
    print("Number is Odd")


# Get the age and name of the student
name = input("Enter your name: ")
age = int(input("Enter your age: "))

# Check if age is greater than 18
if age > 18:
    print(f"Name: {name}, Age: {age}")
else:
    print("Error: Age is not greater than 18")
