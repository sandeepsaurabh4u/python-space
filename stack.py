stack = []
def push(item):
    stack.append(item)

def pop():   
    return stack.pop()

def peek():    
    return stack[-1]

def is_empty():    
    return len(stack) == 0

def size():    
    return len(stack)   

while True:    
    command = input("Enter a command (push, pop, peek, is_empty, size, quit): ")
    if command == "push":
        item = input("Enter an item to push: ")
        push(item)
        print(f"'{item}' has been pushed onto the stack.")
    elif command == "pop":
        if is_empty():
            print("The stack is empty. Cannot pop an item.")
        else:
            item = pop()
            print(f"'{item}' has been popped from the stack.")
    elif command == "peek":
        item = peek()
        print(f"The top item on the stack is '{item}'.")
    elif command == "is_empty":
        if is_empty():
            print("The stack is empty.")
        else:
            print("The stack is not empty.")
    elif command == "size":
        print(f"The size of the stack is {size()}.")
    elif command == "quit":
        break
    else:
        print("Invalid command. Please try again.")
