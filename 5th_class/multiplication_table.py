def print_reverse_table(num):
    print(f"Multiplication table of {num} in reverse order:")
    for i in range(10, 0, -1):
        print(f"{num} x {i} = {num * i}")

number = int(input("Enter a number to display its multiplication table: "))

print_reverse_table(number)
