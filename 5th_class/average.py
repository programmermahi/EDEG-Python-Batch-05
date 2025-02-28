
def calculate_average(numbers):
    return sum(numbers) / len(numbers)

# Get input from the user
num_list = list(map(float, input("Enter numbers separated by spaces: ").split()))

# Call the function and display the result
print("Average of the given numbers:", calculate_average(num_list))
