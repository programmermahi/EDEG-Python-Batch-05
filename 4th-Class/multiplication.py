# Get a number from the user
# number = int(input("Enter a number to generate its multiplication table: "))

# # Generate and print the multiplication table up to 12
# print(f"Multiplication table for {number}:")
# for i in range(1, 13):
#     result = number * i
#     print(f"{number} x {i} = {result}")


# Get the student's score as input
score = float(input("Enter the student's score: "))

# Check the grade based on the score
if 90 <= score <= 100:
    grade = 'A'
elif 80 <= score < 90:
    grade = 'B'
elif 70 <= score < 80:
    grade = 'C'
elif 60 <= score < 70:
    grade = 'D'
elif 0 <= score < 60:
    grade = 'F'
else:
    grade = 'Invalid'

# Display the result
if grade != 'Invalid':
    print(f"The student's grade is: {grade}")
else:
    print("Invalid score. Please enter a score between 0 and 100.")
