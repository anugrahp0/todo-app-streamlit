def add_task(tasks):
    
    with open("todos.txt", "w") as file:
        newtasks = [t + '\n' for t in tasks]
        file.writelines(newtasks)
    return tasks

def view_tasks():
    with open("todos.txt") as file:
        todos = file.readlines()
    if not todos:
       
        return []
    else:
        newTodos = [todo.strip('\n') for todo in todos]
        
        return newTodos

def remove_task(tasks):
    if not tasks:
        print("No tasks to remove.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
        try:
            task_num = int(input("Enter the task number to remove: "))
            if 1 <= task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                with open("todos.txt", "w") as file:
                    newtasks = [t + '\n' for t in tasks]
                    file.writelines(newtasks)
                print(f'Task "{removed_task}" removed.')
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")
    return tasks

def edit_task(tasks):
    if not tasks:
        print("No tasks to edit.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
        try:
            task_num = int(input("Enter the task number to edit: "))
            if 1 <= task_num <= len(tasks):
                new_task = input("Enter the new task: ")
                tasks[task_num - 1] = new_task
                with open("todos.txt", "w") as file:
                    newtasks = [t + '\n' for t in tasks]
                    file.writelines(newtasks)
                print(f'Task "{task_num}" edited to "{new_task}".')
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")
    return tasks
