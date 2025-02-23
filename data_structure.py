# Stack implementation without functions

stack = []  # Initialize an empty list to represent the stack

# Push items onto the stack
stack.append(10)
print(f"Pushed 10 to stack. Current stack: {stack}")
stack.append(20)
print(f"Pushed 20 to stack. Current stack: {stack}")

# Pop an item from the stack with error handling
if len(stack) == 0:
    print("Error: Cannot pop from an empty stack.")
else:
    popped_item = stack.pop()
    print(f"Popped {popped_item} from stack. Current stack: {stack}")

# Attempting to pop again to show error handling on empty stack
if len(stack) == 0:
    print("Error: Cannot pop from an empty stack.")
else:
    popped_item = stack.pop()
    print(f"Popped {popped_item} from stack. Current stack: {stack}")

# Another pop attempt on an empty stack to demonstrate error handling
if len(stack) == 0:
    print("Error: Cannot pop from an empty stack.")
else:
    popped_item = stack.pop()
    print(f"Popped {popped_item} from stack. Current stack: {stack}")
