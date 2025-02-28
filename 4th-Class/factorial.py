number = int(input("Enter a positive integer: "))

if number < 0:
    print("Invalid input. Please enter a positive integer.")
else:
    # Initialize the factorial result to 1
    factorial = 1
    
    for i in range(1, number + 1):
        factorial *= i
    
    # Print the result
    print(f"The factorial of {number} is: {factorial}")
