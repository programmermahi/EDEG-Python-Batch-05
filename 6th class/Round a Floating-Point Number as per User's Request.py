num = float(input("Enter a floating-point number: "))
decimal_places = int(input("Enter the number of decimal places to round to: "))

rounded_num = round(num, decimal_places)
print(f"Number rounded to {decimal_places} decimal places: {rounded_num}")
