# Lambda function to add three numbers
add_three_numbers = lambda x, y, z: x + y + z

# Get input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Call the lambda function and display the result
print("Sum of the three numbers:", add_three_numbers(num1, num2, num3))
