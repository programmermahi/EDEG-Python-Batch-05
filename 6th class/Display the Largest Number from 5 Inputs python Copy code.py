numbers = []
for i in range(5):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)

largest_number = max(numbers)
print("Largest number is:", largest_number)
