# Get a number from the user
num = int(input("Enter a number: "))

# Number of positions to shift
shift_count = int(input("Enter the number of positions to shift: "))

# Perform right and left shift operations
right_shift = num >> shift_count
left_shift = num << shift_count

# Display the results
print(f"Right shift of {num} by {shift_count} positions is: {right_shift}")
print(f"Left shift of {num} by {shift_count} positions is: {left_shift}")
