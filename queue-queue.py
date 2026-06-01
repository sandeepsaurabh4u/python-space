import queue

queue = queue.Queue()

def is_empty():
    return queue.empty()

def size():
    return queue.qsize()

def enqueue(item):
    queue.put(item)

def dequeue():
    try:
        return queue.get_nowait()
    
    except queue.Empty as e:
        print(e)    

def list_queue():
    return list(queue.queue)

while True:
    command = input("Enter a command (enqueue, dequeue, size, is_empty, list, quit): ")
    
    if command == "enqueue":
        item = input("Enter an item to enqueue: ")
        enqueue(item)
        print(f"Enqueued: {item}")
    
    elif command == "dequeue":
        item = dequeue()
        if item is not None:
            print(f"Dequeued: {item}")
    
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