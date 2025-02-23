import random

random_numbers = [random.randint(1, 100) for _ in range(10)]

# Print the list of random numbers
print("Random numbers:", random_numbers)

# Find and print the maximum, minimum, and average
print("Maximum value:", max(random_numbers))
print("Minimum value:", min(random_numbers))
print("Average value:", sum(random_numbers) / len(random_numbers))