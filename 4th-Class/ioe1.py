# Get two numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Check if they are the same object using the `is` operator
if num1 is num2:
    print("The two numbers are the same object.")
else:
    print("The two numbers are not the same object.")
