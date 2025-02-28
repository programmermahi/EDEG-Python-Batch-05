
def validate_username(username):
    if username.isalnum() and 8 <= len(username) <= 20:
        return True
    else:
        return False

# Get input from the user
username = input("Enter a username (8-20 characters, only alphanumeric): ")

# Call the function and display the result
if validate_username(username):
    print("Username is valid.")
else:
    print("Invalid username. It must be 8-20 characters and only contain alphanumeric characters.")
