# Get two numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Find and display the greater number
if num1 > num2:
    print(f"The greater number is {num1}.")
elif num2 > num1:
    print(f"The greater number is {num2}.")
else:
    print("Both numbers are equal.")
