marks1 = float(input("Enter marks for subject 1: "))
marks2 = float(input("Enter marks for subject 2: "))
marks3 = float(input("Enter marks for subject 3: "))

total = marks1 + marks2 + marks3
average = total / 3
percentage = (total / 300) * 100  # Assuming each subject is out of 100

print(f"Total marks: {total}")
print(f"Average marks: {average:.2f}")
print(f"Percentage: {percentage:.2f}%")
