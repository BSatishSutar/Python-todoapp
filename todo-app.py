todo_list = []

def add_task(task):
    todo_list.append(task)
    print("Task added: ", task)

def view_tasks():
    print("Current Tasks: ")
    for i, task in enumerate(todo_list):
        print(f"{i+1}: {task}")

def remove_task(index):
    try:
        task = todo_list.pop(index-1)
        print("Task removed: ", task)
    except IndexError:
        print("Error: Invalid task index")

while True:
    user_input = input("What would you like to do? (add/view/remove/quit): ")
    if user_input == "add":
        task = input("Enter task: ")
        add_task(task)
    elif user_input == "view":
        view_tasks()
    elif user_input == "remove":
        task_index = int(input("Enter task index: "))
        remove_task(task_index)
    elif user_input == "quit":
        break
    else:
        print("Error: Invalid command")
