# Tuple of student names
students = ('Alice', 'Bob', 'Charlie', 'Alice', 'David', 'Alice')

# Get the student name to check from the user
student_name = input("Enter the student name to find its occurrence: ").capitalize()

# Find the occurrence of the student name in the tuple
occurrence = students.count(student_name)

# Display the result
if occurrence > 0:
    print(f"The student '{student_name}' appears {occurrence} times in the tuple.")
else:
    print(f"The student '{student_name}' is not in the tuple.")
