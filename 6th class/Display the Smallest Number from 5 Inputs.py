numbers = []
for i in range(5):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)

smallest_number = min(numbers)
print("Smallest number is:", smallest_number)
