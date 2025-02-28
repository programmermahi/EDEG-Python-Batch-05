# Define the correct username and password
correct_username = "admin"
correct_password = "12345"

# Get username and password from the user
username = input("Enter your username: ")
password = input("Enter your password: ")

# Check if either the username or password is correct
if username == correct_username or password == correct_password:
    print("Partial access: Either the username or password is correct.")
else:
    print("Access denied. Both username and password are incorrect.")
