queue = []

def is_empty():
    return len(queue) == 0 

def size():
    return len(queue)

def enqueue(item):
    queue.insert(0, item)

def dequeue():
    if is_empty():
        raise IndexError("dequeue from an empty queue")
    return queue.pop()

def list_queue():
    return queue

while True:
    command = input("Enter a command (enqueue, dequeue, size, is_empty, list, quit): ")
    
    if command == "enqueue":
        item = input("Enter an item to enqueue: ")
        enqueue(item)
        print(f"Enqueued: {item}")
    
    elif command == "dequeue":
        try:
            item = dequeue()
            print(f"Dequeued: {item}")
        except IndexError as e:
            print(e)
    
    elif command == "size":
        print(f"Queue size: {size()}")
    
    elif command == "is_empty":
        print(f"Is the queue empty? {is_empty()}")

    elif command == "list":
        print(f"Current queue: {list_queue()}")       
            
    elif command == "quit":
        print("Exiting the program.")
        break
    
    else:
        print("Invalid command. Please try again.")        