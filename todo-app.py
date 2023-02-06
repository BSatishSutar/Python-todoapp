todos = []

def add_todo(task):
    todos.append(task)

def view_todos():
    for i, todo in enumerate(todos):
        print(i+1, todo)

add_todo("Buy milk")
add_todo("Finish homework")
view_todos()
