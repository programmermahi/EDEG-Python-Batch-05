
colors = ['red', 'blue', 'green', 'blue', 'yellow', 'blue', 'black']

# Get the color to check from the user
color_to_find = input("Enter the color to find its occurrence: ").lower()

# Find the occurrence of the color in the list
occurrence = colors.count(color_to_find)


if occurrence > 0:
    print(f"The color '{color_to_find}' occurs {occurrence} times in the list.")
else:
    print(f"The color '{color_to_find}' is not in the list.")
