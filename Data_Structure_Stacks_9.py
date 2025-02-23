stack = []

# Menu for stack operations
while True:
    print("\nChoose an operation:")
    print("1. Push an element onto the stack")
    print("2. Pop an element from the stack")
    print("3. Display the stack")
    print("4. Exit")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        element = input("Enter the element to push: ")
        stack.append(element)
        print(f"{element} has been added to the stack.")
    elif choice == "2":
        if stack:
            popped = stack.pop()
            print(f"Popped element: {popped}")
        else:
            print("Error: The stack is empty.")
    elif choice == "3":
        print("Current stack:", stack)
    elif choice == "4":
        print("The program exit")
        break
    else:
        print("Invalid choice. Please try again.")
