# Define the correct username and password
correct_username = "admin"
correct_password = "12345"

# Get username and password from the user
username = input("Enter your username: ")
password = input("Enter your password: ")

# Check if both username and password are correct
if username == correct_username and password == correct_password:
    print("Access granted. Welcome!")
else:
    print("Access denied. Invalid username or password.")
