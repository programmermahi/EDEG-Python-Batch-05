total_sum = 0

# Loop through numbers from 50 to 1
for num in range(50, 0, -1):
    if num % 2 != 0:  # Check if the number is odd
        total_sum += num  # Add the odd number to the sum


print(f"The sum of odd numbers from 50 to 1 is: {total_sum}")
