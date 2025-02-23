numbers=input("Enter the five number : ").split()
numbers=[int(num)for num in numbers]

if len(numbers)!=5:
    print("please Enter exactly five numbers:")
else:
    print(f"Minimum: {min(numbers)}")
    print(f"Maximum: {max(numbers)}")
    print(f"Sum: {sum(numbers)}") 