# Lambda function to concatenate first and last names
full_name = lambda first, last: f"{first} {last}"

# Get input from the user
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

# Call the lambda function and display the full name
print("Full name:", full_name(first_name, last_name))
