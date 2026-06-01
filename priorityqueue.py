import queue
q = queue.PriorityQueue()

def add_task(task, priority):
    q.put((priority, task))

def get_task():
    return q.get()[1]

def is_empty():
    return q.empty()

def size():
    return q.qsize()

def list_tasks():
    return list(q.queue)    


while True:
    command = input("Enter command (add/get/list/exit): ")
    if command == "add":
        task = input("Enter task: ")
        priority = int(input("Enter priority (lower number means higher priority): "))
        add_task(task, priority)
        print(f"Task '{task}' added with priority {priority}.")
    elif command == "get":
        if not is_empty():
            task = get_task()
            print(f"Retrieved task: {task}")
        else:
            print("No tasks in the queue.")

    elif command == "list":
        tasks = list_tasks()
        if tasks:
            print("Tasks in the queue:")
            for priority, task in tasks:
                print(f"Priority: {priority}, Task: {task}")
        else:
            print("No tasks in the queue.")

    elif command == "exit":
        print("Exiting...")
        break
    
    else:
        print("Invalid command. Please enter 'add', 'get', 'list'  or 'exit'.")    