# Tuple of student names
students = ("Alice", "Bob", "Charlie", "David", "Ella")

# Get the student name to search for from the user
student_to_find = input("Enter the student name to find: ")

# Check if the student name is in the tuple
if student_to_find in students:
    print(f"The student '{student_to_find}' is in the tuple.")
else:
    print(f"The student '{student_to_find}' is not in the tuple.")
