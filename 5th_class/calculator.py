
def calculate_percentage(marks_obtained, total_marks):
    return (marks_obtained / total_marks) * 100

marks_obtained = float(input("Enter the marks obtained: "))
total_marks = float(input("Enter the total marks: "))

print("Percentage:", calculate_percentage(marks_obtained, total_marks), "%")
