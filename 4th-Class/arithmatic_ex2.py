
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
num4 = float(input("Enter the fourth number: "))

# Subtract the first two numbers and add the last two
result1 = num1 - num2
result2 = num3 + num4

# Find the multiplication of both results
final_result = result1 * result2

# Display results
print(f"Subtraction of first two numbers ({num1} - {num2}) = {result1}")
print(f"Addition of last two numbers ({num3} + {num4}) = {result2}")
print(f"Multiplication of both results ({result1} * {result2}) = {final_result}")
